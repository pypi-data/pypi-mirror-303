import logging
from abc import ABC, abstractmethod
from typing import Annotated, Any, get_type_hints

from kaya_module_sdk.src.utils.constraints.min_len import kminlen
from kaya_module_sdk.src.utils.metadata.display_description import \
    DisplayDescription
from kaya_module_sdk.src.utils.metadata.display_name import DisplayName
from kaya_module_sdk.src.utils.metadata.min_len import MinLen

log = logging.getLogger(__name__)


class Rets(ABC):
    _results: Annotated[
        list,
        DisplayName("Result"),
        DisplayDescription("Module computation results."),
        MinLen(1),
    ]
    _errors: Annotated[
        list,
        DisplayName("Errors"),
        DisplayDescription("Collection of things that went very, very wrong."),
    ]

    @property
    def results(self) -> None:
        return self._result

    @property
    def errors(self) -> None:
        return self._errors

    @kminlen(1)
    def set_results(self, *values: Any) -> None:
        self._result += list(values)

    def set_errors(self, *values: Any) -> None:
        self._errors += list(values)

    def metadata(self) -> None:
        return get_type_hints(self, include_extras=True)
