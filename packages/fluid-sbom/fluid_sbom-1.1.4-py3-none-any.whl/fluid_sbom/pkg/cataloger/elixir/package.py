from fluid_sbom.file.location import (
    Location,
)
from fluid_sbom.pkg.elixir import (
    ElixirMixLockEntry,
)
from fluid_sbom.pkg.language import (
    Language,
)
from fluid_sbom.pkg.package import (
    Package,
)
from fluid_sbom.pkg.type import (
    PackageType,
)
import logging
from packageurl import (
    PackageURL,
)
from pydantic import (
    ValidationError,
)

LOGGER = logging.getLogger(__name__)


def new_package(
    entry: ElixirMixLockEntry, locations: Location
) -> Package | None:
    name = entry.name
    version = entry.version

    if not name or not version:
        return None

    try:
        return Package(
            name=name,
            version=version,
            type=PackageType.HexPkg,
            locations=[locations],
            p_url=package_url(name, version),
            metadata=entry,
            language=Language.ELIXIR,
            licenses=[],
        )
    except ValidationError as ex:
        LOGGER.warning(
            "Malformed package. Required fields are missing or data types "
            "are incorrect.",
            extra={
                "extra": {
                    "exception": ex.errors(include_url=False),
                    "location": locations.path(),
                }
            },
        )
        return None


def package_url(name: str, version: str) -> str:
    return PackageURL(
        type="hex",
        namespace="",
        name=name,
        version=version,
        qualifiers=None,
        subpath="",
    ).to_string()
