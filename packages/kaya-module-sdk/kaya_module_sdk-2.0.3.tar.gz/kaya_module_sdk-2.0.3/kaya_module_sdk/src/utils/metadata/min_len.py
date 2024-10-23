from kaya_module_sdk.src.utils.metadata.abstract_metadata import KMetadata
from kaya_module_sdk.src.utils.metadata.abstract_validation import KValidation


class MinLen(KMetadata, KValidation):
    def __init__(self, value: float) -> None:
        self._data = {
            "min_len": value,
        }

    def __str__(self) -> str:
        return f'minlen:{self._data["min_len"]}'

    def load(self, str_repr: str) -> dict:
        segmented = str_repr.split(":")
        if not len(segmented) == 2 or segmented[0] != "minlen":
            return
        self._data["min_len"] = float(segmented[1])
        return self._data
