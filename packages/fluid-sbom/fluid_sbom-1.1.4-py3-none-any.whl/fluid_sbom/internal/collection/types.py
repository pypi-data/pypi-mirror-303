from collections import (
    UserDict,
    UserList,
)
from pydantic import (
    BaseModel,
    ConfigDict,
)
from tree_sitter import (
    Node,
)
from typing import (
    Any,
)


class FileCoordinate(BaseModel):
    line: int
    column: int
    model_config = ConfigDict(frozen=True)


class Position(BaseModel):
    start: FileCoordinate
    end: FileCoordinate
    model_config = ConfigDict(frozen=True)


class IndexedDict(UserDict):
    def __init__(self, root_node: Node | None = None):
        self.position_value_index: dict[str, Position] = {}
        self.position_key_index: dict[str, Position] = {}
        data: dict[tuple[str, Position], tuple[Any, Position]] = {}
        if root_node:
            self.position = Position(
                start=FileCoordinate(
                    line=root_node.start_point[0] + 1,
                    column=root_node.start_point[1] + 1,
                ),
                end=FileCoordinate(
                    line=root_node.end_point[0] + 1,
                    column=root_node.end_point[1] + 1,
                ),
            )
        super().__init__(data)

    def __setitem__(  # type: ignore
        self,
        key: tuple[Any, Position | Node],
        item: tuple[Any, Position | Node],
    ) -> None:
        if not isinstance(item, tuple):
            raise ValueError(
                "The value must be a tuple that"
                " contains the value and the position"
            )
        key_value, key_position = key
        value_value, value_position = item
        if isinstance(key_position, Node):
            key_position = Position(
                start=FileCoordinate(
                    line=key_position.start_point[0] + 1,
                    column=key_position.start_point[1] + 1,
                ),
                end=FileCoordinate(
                    line=key_position.end_point[0] + 1,
                    column=key_position.end_point[1] + 1,
                ),
            )
        if isinstance(value_position, Node):
            value_position = Position(
                start=FileCoordinate(
                    line=value_position.start_point[0] + 1,
                    column=value_position.start_point[1] + 1,
                ),
                end=FileCoordinate(
                    line=value_position.end_point[0] + 1,
                    column=value_position.end_point[1] + 1,
                ),
            )
        self.position_key_index[key_value] = key_position
        self.position_value_index[key_value] = value_position
        return super().__setitem__(key_value, value_value)

    def get_value_position(self, key: str) -> Position:
        return self.position_value_index[key]

    def get_key_position(self, key: str) -> Position:
        return self.position_key_index[key]


class IndexedList(UserList):
    def __init__(self, node: Node):
        self.position_index: dict[int, Position] = {}
        data: list[tuple[Any, Position]] = []
        self.position = Position(
            start=FileCoordinate(
                line=node.start_point[0] + 1,
                column=node.start_point[1] + 1,
            ),
            end=FileCoordinate(
                line=node.end_point[0] + 1,
                column=node.end_point[1] + 1,
            ),
        )
        super().__init__(data)

    def __setitem__(  # type: ignore
        self,
        index: int,
        value: tuple[Any, Position],
    ) -> None:
        if not isinstance(value, tuple):
            raise ValueError(
                "The value must be a tuple that"
                " contains the value and the position"
            )
        self.position_index[index] = value[1]
        return super().__setitem__(index, value[0])

    def append(  # type: ignore
        self,
        item: tuple[Any, Position | Node],
    ) -> None:
        value, position = item
        if isinstance(position, Node):
            position = Position(
                start=FileCoordinate(
                    line=position.start_point[0] + 1,
                    column=position.start_point[1] + 1,
                ),
                end=FileCoordinate(
                    line=position.end_point[0] + 1,
                    column=position.end_point[1] + 1,
                ),
            )
        self.position_index[len(self.data)] = position
        return super().append(value)

    def get_position(self, index: int) -> Position:
        return self.position_index[index]


def index_serializer(obj: Any) -> dict[str, Any] | list[Any]:
    if isinstance(obj, UserList):
        return list(obj)
    if isinstance(obj, UserDict):
        return dict(obj)
    raise TypeError(f"Type {type(obj)} not serializable")
