from abc import ABC, abstractmethod


class KMetadata(ABC):
    _data: dict

    def __repr__(self) -> str:
        return self.__str__()
