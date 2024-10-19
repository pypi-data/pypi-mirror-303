from bs4 import (
    BeautifulSoup,
)
from copy import (
    deepcopy,
)
from fluid_sbom.artifact.relationship import (
    Relationship,
)
from fluid_sbom.file.location_read_closer import (
    LocationReadCloser,
)
from fluid_sbom.file.resolver import (
    Resolver,
)
from fluid_sbom.pkg.cataloger.generic.parser import (
    Environment,
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


def parse_csproj(
    _resolver: Resolver | None,
    _env: Environment | None,
    reader: LocationReadCloser,
) -> tuple[list[Package], list[Relationship]]:
    packages: list[Package] = []
    root = BeautifulSoup(reader.read_closer.read(), features="html.parser")
    for pkg in root.find_all("packagereference", recursive=True):
        line = pkg.sourceline
        name: str | None = pkg.get("include")
        version: str | None = pkg.get("version")

        if not name or not version:
            continue

        location = deepcopy(reader.location)
        if location.coordinates:
            location.coordinates.line = line

        try:
            packages.append(
                Package(
                    name=name,
                    version=version,
                    locations=[location],
                    language=Language.DOTNET,
                    licenses=[],
                    type=PackageType.DotnetPkg,
                    metadata=None,
                    p_url=PackageURL(
                        type="nuget",
                        namespace="",
                        name=name,
                        version=version,
                        qualifiers={},
                        subpath="",
                    ).to_string(),
                )
            )
        except ValidationError as ex:
            LOGGER.warning(
                "Malformed package. Required fields are missing or data types "
                "are incorrect.",
                extra={
                    "extra": {
                        "exception": ex.errors(include_url=False),
                        "location": location.path(),
                    }
                },
            )
            continue

    return packages, []
