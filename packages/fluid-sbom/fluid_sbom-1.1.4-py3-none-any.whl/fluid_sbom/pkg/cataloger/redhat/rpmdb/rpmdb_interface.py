import abc
from typing import (
    Generator,
    Type,
)


class RpmDBInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(
        cls: Type["RpmDBInterface"], subclass: object
    ) -> bool:
        return (
            hasattr(subclass, "read")
            and callable(subclass.read)
            or NotImplemented
        )

    @abc.abstractmethod
    def read(
        self,
    ) -> Generator[bytes, None, None]:
        """Read entry bytes"""
        raise NotImplementedError
