import importlib
import inspect
import logging
import heapq
import pysnooper

from abc import ABC, abstractmethod
from typing import (Annotated, Any, Dict, Type, Union, get_args, get_origin,
                    get_type_hints)

from kaya_module_sdk.src.exceptions.kunimplemented import \
    KayaUnimplementedException
from kaya_module_sdk.src.module.arguments import Args
from kaya_module_sdk.src.module.config import KConfig
from kaya_module_sdk.src.module.returns import Rets
from kaya_module_sdk.src.utils.metadata.abstract_metadata import KMetadata
from kaya_module_sdk.src.utils.metadata.abstract_validation import KValidation
from kaya_module_sdk.src.utils.metadata.display_description import \
    DisplayDescription
from kaya_module_sdk.src.utils.metadata.display_name import DisplayName

log = logging.getLogger(__name__)


class Config(KConfig):
    def __init__(self):
        super().__init__()


class Module(ABC):
    """[ DESCRIPTION ]: Kaya Strategy Module Template.

    [ MANIFEST ]: {
        "moduleName": "string",         -- Name of the module
        "moduleDisplayLabel": "string", -- Display label for this module in the frontend
        "moduleCategory": "enum",       -- Category of the module. An ENUM defined by the NeptuneAPI smithy model.
        "moduleDescription": "string",  -- Description of the module
        "author": "kaya_id(user)",      -- UserID of the User vertex that owns this module.
        "inputs": [{
            "name": "string",           -- Name of the input field in the request object
            "label": "string",          -- Display label for this input in the frontend
            "type": "kaya_id(value)",   -- VertexID of the value that represents this input datatype
            "description": "string",    -- Description of the INPUT
            "validations": [
                "validation_pattern"    -- An array of validation queries to run against the inputs.
            ]}
        ],
        "outputs": [{
            "name": "string",           -- Name of the output field in the returned structure
            "label": "string",          -- Display label for this output in the frontend
            "type": "kaya_id(value)",   -- VertexID of the value that represents this output datatype
            "description": "string"     -- Description of the output
            "validations": [
                "validation_pattern"    -- An array of validation queries to run against the inputs.
            ]}
        ]
    }
    """

    config: KConfig
    subclasses: list = []
    modules: dict = {}
    _manifest: dict = {}
    _recompute_manifest: bool = True

    def __init__(self) -> None:
        self.config = Config()
        self.import_subclasses()
        self.modules = {item.__class__.__name__: item for item in self.subclasses}

    #   @pysnooper.snoop()
    def import_subclasses(self) -> list:
        module_name = self.__module__
        package = importlib.import_module(module_name).__package__
        if not package:
            return self.subclasses
        try:
            module = importlib.import_module(f"{package}.module")
        except Exception as e:
            return self.subclasses
        for cls_name, obj in inspect.getmembers(module):
            if (
                inspect.isclass(obj)
                and issubclass(obj, Module)
                and obj not in [Module, Args, Rets, KConfig, KMetadata, KValidation]
                and cls_name != "KayaStrategyModule"
            ):
                subclass_instance = obj()
                self.subclasses.append(subclass_instance)
        return self.subclasses

    @pysnooper.snoop()
    def _extract_manifest(self) -> Dict[str, Any]:
        main_method = self.main
        type_hints = get_type_hints(main_method)
        args_hints = {
            param: type_hint
            for param, type_hint in type_hints.items()
            if param != "return"
        }
        return_hint = type_hints.get("return", None)
        signature = inspect.signature(main_method)
        params_metadata = {}
        for param_name, param in signature.parameters.items():
            expected_type = args_hints.get(param_name, "Any")
            params_metadata[param_name] = {
                "expected_type": expected_type,
                "annotation": param.annotation,
                "details": self._get_class_metadata(expected_type)
                if inspect.isclass(expected_type)
                else None,
            }
        return_metadata = {
            "expected_type": return_hint,
            "annotation": signature.return_annotation,
            "details": self._get_class_metadata(return_hint)
            if inspect.isclass(return_hint)
            else None,
        }
        metadata = {
            "moduleName": str(self.config.name),
            "moduleVersion": str(self.config.version),
            "moduleDisplayLabel": str(self.config.display_label),
            "moduleCategory": str(self.config.category),
            "moduleDescription": str(self.config.description),
            "author": str(self.config.author),
            "inputs": [],
            "outputs": [],
        }
        metadata["inputs"] += self._order_records_by_priority(
            *self._extract_metadata(params_metadata["args"]["details"])
        )
        metadata["outputs"] += self._order_records_by_priority(
            *self._extract_metadata(return_metadata["details"])
        )
        return metadata

    #   @pysnooper.snoop()
    def _extract_metadata(self, details: dict) -> list:
        metadata = []
        if not details:
            return metadata
        for detail in details:
            unpacked = self._unpack_annotated(details[detail]["type"])
            record = {
                "name": detail.strip('_'),
                "label": detail,
                "type": str(unpacked[0]).split("'")[1],
                "description": None,
                "validations": [],
            }
            for item in unpacked[1]:
                if not isinstance(item, KMetadata):
                    continue
                segmented = str(item).split(":")
                if isinstance(item, DisplayName):
                    record["label"] = segmented[1]
                elif isinstance(item, DisplayDescription):
                    record["description"] = segmented[1]
                elif isinstance(item, KValidation):
                    record["validations"].append(str(item))
            metadata.append(record)
        return metadata

#   @pysnooper.snoop()
    def _order_records_by_priority(self, *records: dict):
        ordered, priority_queue, to_order, leftover = [], [], [], []
        for record in records:
            position = [
                int(item.split(':')[1]) for item in record.get('validations', [])
                if item.startswith('position:')
            ]
            if not position:
                leftover.append(record)
                continue
            to_order.append((position[0], record,))
        for record in to_order:
            heapq.heappush(priority_queue, record)
        while priority_queue:
            _, record = heapq.heappop(priority_queue)
            ordered.append(record)
        ordered += leftover
        return ordered

    #   @pysnooper.snoop()
    def _unpack_annotated(self, annotated_type):
        # Check if the type is an Annotated type
        if get_origin(annotated_type) is Annotated:
            base_type, *metadata = get_args(annotated_type)
            # Check if the base type is another Annotated type
            if get_origin(base_type) is Annotated:
                return self._unpack_annotated(base_type)
            return base_type, metadata
        # If the type is a list, we need to unpack its inner type
        elif get_origin(annotated_type) is list:
            inner_type = get_args(annotated_type)[0]
            return self._unpack_annotated(inner_type)
        return annotated_type, []

    #   @pysnooper.snoop()
    def _get_class_metadata(self, cls: Type) -> Dict[str, Any]:
        """Recursively fetch the metadata for class attributes with type
        annotations."""
        if not hasattr(cls, "__annotations__"):
            return {}
        class_metadata = {}
        for attr_name, attr_type in cls.__annotations__.items():
            class_metadata[attr_name] = {
                "type": attr_type,
                "details": self._get_class_metadata(attr_type)
                if inspect.isclass(attr_type)
                else None,
            }
        return class_metadata

    @property
    def manifest(self) -> dict:
        """
        [ RETURN ]: {
            "moduleName": "string",
            "moduleVersion": "2.0",
            "moduleDisplayLabel": "string",
            "moduleCategory": "enum",
            "moduleDescription": "string",
            "author": "kaya_id(user)",
            "inputs": [
                {
                "name": "string",
                "label": "string",
                "type": "kaya_id(value)",
                "description": "string",
                "validations": [
                    "validation_pattern"
                ]
                }
            ],
            "outputs": [
                {
                "name": "string",
                "label": "string",
                "type": "kaya_id(value)",
                "description": "string"
                }
            ]
        }
        """
        if self._manifest and not self._recompute_manifest:
            return self._manifest
        self._manifest = self._extract_manifest()
        return self._manifest

    @abstractmethod
    def main(self, args: Args) -> Rets:
        pass

# CODE DUMP

