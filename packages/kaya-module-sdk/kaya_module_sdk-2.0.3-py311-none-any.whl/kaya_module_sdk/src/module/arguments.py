import logging
from abc import ABC, abstractmethod
from typing import Annotated, Any, get_type_hints

from kaya_module_sdk.src.utils.constraints.minimum import kmin
from kaya_module_sdk.src.utils.metadata.display_description import \
    DisplayDescription
from kaya_module_sdk.src.utils.metadata.display_name import DisplayName
from kaya_module_sdk.src.utils.metadata.minimum import Min

log = logging.getLogger(__name__)


class Args(ABC):
    _errors: Annotated[
        list,
        DisplayName("Errors"),
        DisplayDescription("Collection of things that went very, very wrong."),
    ]

    @property
    def errors(self) -> None:
        return self._errors

    def set_errors(self, *values: Any) -> None:
        self._errors += list(values)

    def metadata(self):
        return get_type_hints(self, include_extras=True)
