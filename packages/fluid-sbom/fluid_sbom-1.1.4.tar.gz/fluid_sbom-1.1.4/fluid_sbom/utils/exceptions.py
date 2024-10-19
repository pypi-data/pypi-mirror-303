from cyclonedx.validation import (
    ValidationError as CycloneDXError,
)
from jsonschema import (
    ValidationError as JSONSchemaError,
)
from spdx_tools.spdx.validation.validation_message import (
    ValidationMessage,
)
from tree_sitter import (
    Node,
)


class CustomBaseException(Exception):
    """Base exception class for custom exceptions."""


class CycloneDXValidationError(CustomBaseException):
    """Exception for CycloneDX validation errors."""

    def __init__(self, error: CycloneDXError) -> None:
        """Constructor"""
        header = "Exception - CycloneDx validation error\n"
        msg = f"❌ {header}{error}"
        super().__init__(msg)


class DuplicatedKey(Exception):
    """Exception raised for duplicated keys."""


class ForbiddenModuleImported(Exception):
    """Exception raised when a forbidden module is imported."""


class FluidJSONValidationError(CustomBaseException):
    """Exception for Fluid JSON validation errors."""

    def __init__(self, error: JSONSchemaError) -> None:
        """Constructor"""
        header = "Exception - Fluid JSON validation error\n"
        msg = f"❌ {header}{error}"
        super().__init__(msg)


class InvalidDocumentKeyPair(CustomBaseException):
    """Exception raised for invalid document key pairs."""


class InvalidType(CustomBaseException):
    """Exception raised for invalid types."""


class InvalidMetadata(CustomBaseException):
    """Exception raised for when metadata is invalid"""

    def __init__(self, error_message: str):
        message = error_message
        super().__init__(message)


class SPDXValidationError(CustomBaseException):
    """Exception for SPDX validation errors."""

    def __init__(self, error_messages: list[ValidationMessage]) -> None:
        """Constructor"""
        header = "Exception - SPDX validation error\n"
        error_details = "\n".join(
            (
                f"Validation error: {message.validation_message}\n"
                f"Context: {message.context}"
            )
            for message in error_messages
        )
        msg = f"❌ {header}{error_details}"
        super().__init__(msg)


class UnexpectedException(CustomBaseException):
    """Exception for unexpected errors encountered during SBOM execution."""

    def __init__(self, error: Exception) -> None:
        """Constructor"""
        header = (
            "Exception - An unexpected exception was encountered "
            "during SBOM execution. The process will be terminated to prevent "
            "potential inconsistencies.\n"
        )
        msg = f"❌ {header}{error}"
        super().__init__(msg)


class UnexpectedNode(CustomBaseException):
    """Exception raised for unexpected nodes."""

    def __init__(self, node: Node | str) -> None:
        type_name = node.type if isinstance(node, Node) else node
        value = node.text.decode("utf-8") if isinstance(node, Node) else None
        if value:
            super().__init__(
                f"Unexpected node type {type_name} with value {value}"
            )
        else:
            super().__init__(f"Unexpected node type {type_name}")


class UnexpectedNodeType(CustomBaseException):
    """Exception raised for unexpected node types."""

    def __init__(
        self, node: Node | str, expected_type: str | None = None
    ) -> None:
        type_name = node.type if isinstance(node, Node) else node
        if expected_type:
            super().__init__(
                f"Unexpected node type {type_name} for {expected_type}"
            )
        else:
            super().__init__(f"Unexpected node type {type_name}")


class UnexpectedValueType(CustomBaseException):
    """Exception raised for unexpected value types."""


class UnexpectedChildrenLength(CustomBaseException):
    """Exception raised for nodes with unexpected number of children."""

    def __init__(self, node: Node | str, expected_length: int) -> None:
        type_name = node.type if isinstance(node, Node) else node
        super().__init__(
            f"Unexpected node type {type_name} for {expected_length} children"
        )
