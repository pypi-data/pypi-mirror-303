import importlib
import logging
import socket

import mypy.api as mypy_api
import pysnooper
from flake8.api import legacy as flake8
from kaya_module_sdk.src.exceptions.module_not_found import \
    ModuleNotFoundException
from kaya_module_sdk.src.utils.metadata.equal import EQ
from kaya_module_sdk.src.utils.metadata.greater import GT
from kaya_module_sdk.src.utils.metadata.greater_or_equal import GTE
from kaya_module_sdk.src.utils.metadata.less import LT
from kaya_module_sdk.src.utils.metadata.less_or_equal import LTE
from kaya_module_sdk.src.utils.metadata.max_len import MaxLen
from kaya_module_sdk.src.utils.metadata.maximum import Max
from kaya_module_sdk.src.utils.metadata.min_len import MinLen
from kaya_module_sdk.src.utils.metadata.minimum import Min
from kaya_module_sdk.src.utils.metadata.value_range import ValueRange
from kaya_module_sdk.src.utils.shell import shell_cmd

log = logging.getLogger(__name__)


class KVLE:
    """[ KVL(E)xecuter ]: Responsibilities -

    * Runs all linters and checkers on the source code files
        [ Ex ]: pylint, flake8, mypy
    * Imports all modules found in source code files
    * Attempts extraction of Manifest from imported modules
    * Verifies that required module metadata is properly set
    * Checks module specific input data validators are properly set
    * Collects all validation results in a easy to handle manner
    """

    check: dict
    context: dict

    def __init__(self, **kvlh_context):
        self.context = kvlh_context
        self.check = {
            "rules": {
                "ok": [],
                "nok": [],
            },
            "meta": {
                "ok": [],
                "nok": [],
            },
            "source": {
                "ok": [],
                "nok": [],
            },
        }

    # UTILS

    # @pysnooper.snoop()
    def check_package_installed(self, test: dict) -> bool:
        try:
            importlib.util.find_spec(test["package"])
        except Exception as e:
            return ModuleNotFoundException(
                f'Package {test["package"]} is not installed!'
            )
        return True

    # @pysnooper.snoop()
    def load_constraint_rules(self, *rules: str) -> list:
        matches, metadata_classes = [], [
            EQ,
            GT,
            GTE,
            LT,
            LTE,
            MaxLen,
            Max,
            MinLen,
            Min,
            ValueRange,
        ]
        for rule in rules:
            for cls in metadata_classes:
                try:
                    if ";" in rule:
                        instance = cls(None, None)
                    else:
                        instance = cls(None)
                    instance.load(rule)
                except Exception as e:
                    continue
                matches.append(instance)
        formatted_matches = {
            item.__class__.__name__: item
            for item in matches
            if None not in item._data.values()
        }
        return {} if rules and not formatted_matches else formatted_matches

    # ACTIONS

    # @pysnooper.snoop()
    def check_rules(self, module_data: dict, report: bool = True) -> dict:
        """
        [ RETURN ]: {
            'ok': [{
                'package': 'dummy_package',
                'module': 'Dummy1',
                'functions': {
                    'main': [{
                        'name': 'Large Window Rule',
                        'verb': 'gte',
                        'rule': ['window', 'data.length']
                    },
                    {
                        'name': 'Single Data Point',
                        'verb': 'eq',
                        'rule': ['single_window', 1],
                    }],
                },
            }],
            'nok': [],
        }
        """
        package = self.context["_module_package"]["instance"]
        package_name, package_version = package.config.name, package.config.version
        submodules = package.modules
        for module_name in submodules:
            nok_flag, module_record = False, {
                "package": package_name,
                "module": module_name,
                "functions": {"main": []},
            }
            manifest = submodules[module_name].manifest
            if not manifest:
                nok_flag = True
                module_report.update({"manifest": {"required": True, "set": False}})
                continue
            if (
                manifest
                and not isinstance(manifest, dict)
                or not manifest.get("inputs")
                or not manifest.get("outputs")
            ):
                nok_flag = True
                module_report.update(
                    {
                        "manifest": {
                            "required": True,
                            "set": True,
                            "valid": False,
                            "value": manifest,
                        }
                    }
                )
                continue
            for arg in manifest["inputs"]:
                if not arg["validations"]:
                    continue
                loaded = self.load_constraint_rules(*arg["validations"])
                if arg["validations"] and not loaded:
                    nok_flag = True
                for constraint_name in loaded:
                    values = list(loaded[constraint_name]._data.values())
                    if len(values) == 1:
                        values = values[0]
                    module_record["functions"]["main"].append(
                        {
                            "name": constraint_name,
                            "target": "inputs",
                            "verb": constraint_name.lower(),
                            "field": arg["label"],
                            "rule": [constraint_name, values],
                        }
                    )
            for ret in manifest["outputs"]:
                if not ret["validations"]:
                    continue
                loaded = self.load_constraint_rules(*ret["validations"])
                if ret["validations"] and not loaded:
                    nok_flag = True
                for constraint_name in loaded:
                    values = list(loaded[constraint_name]._data.values())
                    if len(values) == 1:
                        values = values[0]
                    module_record["functions"]["main"].append(
                        {
                            "name": constraint_name,
                            "target": "outputs",
                            "verb": constraint_name.lower(),
                            "field": arg["label"],
                            "rule": [constraint_name, values],
                        }
                    )
            if nok_flag:
                self.check["rules"]["nok"].append(module_record)
                continue
            self.check["rules"]["ok"].append(module_record)
        return (
            self.check["rules"]
            if report
            else (True if not self.check["rules"]["nok"] else False)
        )

    # @pysnooper.snoop()
    def check_meta(self, module_data: dict, report: bool = True) -> dict:
        """
        [ RETURN ]: {
            'ok': [],
            'nok': [{
                'package': 'dummy_package',
                'module': 'Dummy1',
                'version': {
                    'required': True,
                    'set': True,
                    'valid': True,
                    'value': '1.0.1',
                },
                'category': {
                    'required': True,
                    'set': True,
                    'valid': True,
                    'value': 'INDICATOR',
                },
                'type': {
                    'required': True,
                    'set': True,
                    'valid': False,
                    'value': 'NotAValidType'
                },
            }],
        }
        """
        package = self.context["_module_package"]["instance"]
        package_name, package_version = package.config.name, package.config.version
        submodules = package.modules
        for module_name in submodules:
            nok_flag, module_report = False, {
                "package": package_name,
                "package_version": package_version,
                "module": module_name,
            }
            if not submodules[module_name].config:
                nok_flag = True
                module_report.update({"config": {"required": True, "set": False}})
            for key in submodules[module_name].config._mandatory:
                if not submodules[module_name].config.__dict__.get(key):
                    nok_flag = True
                    module_report.update({key: {"required": True, "set": False}})
                    continue
                if (
                    key != "version"
                    and not type(submodules[module_name].config.__dict__[key])
                    not in (str,)
                ) or (
                    key == "version"
                    and type(submodules[module_name].config.__dict__[key])
                    not in (str, float)
                ):
                    nok_flag = True
                    module_report.update(
                        {
                            key: {
                                "required": True,
                                "set": True,
                                "valid": False,
                                "value": submodules[module_name].config.__dict__[key],
                            }
                        }
                    )
                    continue
                module_report.update(
                    {
                        key: {
                            "required": True,
                            "set": True,
                            "valid": True,
                            "value": submodules[module_name].config.__dict__[key],
                        }
                    }
                )

            manifest = submodules[module_name].manifest
            if not manifest:
                nok_flag = True
                module_report.update(
                    {
                        "manifest": {
                            "required": True,
                            "set": False,
                            "valid": False,
                            "value": manifest,
                        }
                    }
                )

            if manifest and not isinstance(manifest, dict):
                nok_flag = True
                module_report.update(
                    {
                        "manifest": {
                            "required": True,
                            "set": True,
                            "valid": False,
                            "value": manifest,
                        }
                    }
                )
            if nok_flag:
                self.check["meta"]["nok"].append(module_report)
                continue
            self.check["meta"]["ok"].append(module_report)
        return (
            self.check["meta"]
            if report
            else (True if not self.check["meta"]["nok"] else False)
        )

    # @pysnooper.snoop()
    def check_source(self, loaded_files: dict, report=True) -> dict:
        """
        [ RETURN ]: {
            'ok': [{
                'path': './src',
                'errors': [],
                'result': 'OK',
            }],
            'nok': [],
        }
        """
        for file_path, file_lines in loaded_files.items():
            errors = []
            style_guide = flake8.get_style_guide()
            flake8_report = style_guide.check_files([file_path])
            if flake8_report.total_errors > 0:
                flake8_output = [
                    {
                        error[0]: [error[1], error[2]]
                        for error in flake8_report._application.file_checker_manager.results
                    }
                ]
                errors.append({"tool": "flake8", "output": flake8_output})
            mypy_result = mypy_api.run([file_path])
            mypy_stdout, mypy_stderr, mypy_exit_status = mypy_result
            if mypy_stderr or mypy_exit_status:
                errors.append(
                    {
                        "tool": "mypy",
                        "output": mypy_stdout + mypy_stderr,
                        "exit": mypy_exit_status,
                    }
                )
            if errors:
                self.check["source"]["nok"].append(
                    {"path": file_path, "errors": errors, "result": "NOK"}
                )
            else:
                self.check["source"]["ok"].append(
                    {"path": file_path, "errors": [], "result": "OK"}
                )
        return (
            self.check["source"]
            if report
            else (True if not self.check["source"]["nok"] else False)
        )


# CODE DUMP
