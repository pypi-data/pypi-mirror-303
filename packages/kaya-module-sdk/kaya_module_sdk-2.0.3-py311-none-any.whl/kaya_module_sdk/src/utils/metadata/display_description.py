import pkg_resources

from kaya_module_sdk.src.utils.metadata.abstract_metadata import KMetadata


def load_markdown(location_of, file_name):
    file_path = pkg_resources.resource_filename(location_of, f'/{file_name}')
    with open(file_path, 'r') as file:
        content = file.read()
    return content


class DisplayDescription(KMetadata):
    def __init__(self, description: str) -> None:
        self._data = {
            "description": description,
        }

    def __str__(self) -> str:
        return f'description:{self._data["description"]}'

    def load(self, str_repr: str) -> dict:
        segmented = str_repr.split(":")
        if not len(segmented) == 2 or segmented[0] != "description":
            return
        self._data["description"] = segmented[1]
        return self._data
