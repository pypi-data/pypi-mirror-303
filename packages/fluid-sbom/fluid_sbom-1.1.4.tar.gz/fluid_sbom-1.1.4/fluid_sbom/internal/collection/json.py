from fluid_sbom.internal.collection.types import (
    IndexedDict,
    IndexedList,
)
from fluid_sbom.utils.exceptions import (
    UnexpectedNode,
)
import logging
import os
from tree_sitter import (
    Language,
    Node,
    Parser,
)
from typing import (
    Any,
)

LOGGER = logging.getLogger(__name__)


def _handle_array_node(node: Node) -> tuple[Node, IndexedList]:
    data = IndexedList(node)
    for child in node.children:
        if child.type not in ("[", "]", ","):
            value_node, value = handle_json_node(child)
            data.append((value, value_node))
    return node, data


def _handle_object_node(node: Node) -> tuple[Node, IndexedDict]:
    data = IndexedDict(node)
    for child in node.children:
        if child.type == "pair":
            key_n, _, value_n = child.children
            key = key_n.text[1:-1].decode("utf-8")
            value_node, value_value = handle_json_node(value_n)
            data[(key, key_n)] = (value_value, value_node)
    return node, data


def handle_json_node(node: Node) -> tuple[Node, Any]:
    value: Any | None = None
    match node.type:
        case "array":
            value = _handle_array_node(node)
        case "object":
            value = _handle_object_node(node)
        case "string":
            value = node, node.text[1:-1].decode("utf-8")
        case "number":
            try:
                value = node, int(node.text.decode("utf-8"))
            except ValueError:
                value = node, float(node.text.decode("utf-8"))
        case "true":
            value = node, True
        case "false":
            value = node, False
        case "null":
            value = node, None
        case _:
            raise UnexpectedNode(node)
    return value


def parse_json_with_tree_sitter(json: str) -> IndexedDict | IndexedList:
    parser = Parser()
    parser.set_language(
        Language(
            os.path.join(
                os.environ["TREE_SITTETR_PARSERS_DIR"],
                "json.so",
            ),
            "json",
        )
    )

    result = parser.parse(json.encode("utf-8"))
    value: IndexedDict | IndexedList | None = None
    for child in result.root_node.children:
        try:
            _, value = handle_json_node(child)
        except UnexpectedNode:
            LOGGER.exception(
                "Unexpected node",
                extra={
                    "extra": {
                        "result": result,
                        "node": child.type,
                        "json": json,
                    },
                },
            )
            break
    if not value:
        raise ValueError("Could not parse json")

    return value
