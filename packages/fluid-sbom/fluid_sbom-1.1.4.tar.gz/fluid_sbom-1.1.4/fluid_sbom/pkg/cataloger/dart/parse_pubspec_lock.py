from copy import (
    deepcopy,
)
from fluid_sbom.artifact.relationship import (
    Relationship,
)
from fluid_sbom.file.location import (
    Location,
)
from fluid_sbom.file.location_read_closer import (
    LocationReadCloser,
)
from fluid_sbom.file.resolver import (
    Resolver,
)
from fluid_sbom.internal.collection.types import (
    IndexedDict,
    Position,
)
from fluid_sbom.internal.collection.yaml import (
    parse_yaml_with_tree_sitter,
)
from fluid_sbom.pkg.cataloger.generic.parser import (
    Environment,
)
from fluid_sbom.pkg.dart import (
    DartPubspecLickEntry,
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
from typing import (
    cast,
    ItemsView,
)
from urllib3.util import (
    parse_url,
)

LOGGER = logging.getLogger(__name__)


def get_hosted_url(entry: IndexedDict) -> str:
    hosted: str | None = entry.get("hosted")
    description: dict[str, str] | None = entry.get("description")

    if (
        hosted == "hosted"
        and description
        and description["url"] != "https://pub.dartlang.org"
    ):
        if host := parse_url(description["url"]).host:
            return host

        return description["url"]

    return ""


def get_vcs_url(entry: IndexedDict) -> str:
    source: str | None = entry.get("source")
    description: dict[str, str] | None = entry.get("description")

    if description and source == "git":
        if description.get("path") == ".":
            return f'{description["url"]}@{description["resolved-ref"]}'
        return (
            description["url"]
            + f'@{description["resolved-ref"]}'
            + f'#{description["path"]}'
        )
    return ""


def package_url(entry: DartPubspecLickEntry) -> str:
    qualifiers = {}
    if entry.hosted_url:
        qualifiers["hosted_url"] = entry.hosted_url
    elif entry.vcs_url:
        qualifiers["vcs_url"] = entry.vcs_url

    return PackageURL(  # type: ignore
        type="pub",
        namespace="",
        name=entry.name,
        version=entry.version,
        qualifiers=qualifiers,
        subpath="",
    ).to_string()


def parse_pubspec_lock(
    _: Resolver | None,
    __: Environment | None,
    reader: LocationReadCloser,
) -> tuple[list[Package], list[Relationship]]:
    package_yaml: IndexedDict = cast(
        IndexedDict, parse_yaml_with_tree_sitter(reader.read_closer.read())
    )
    packages: list[Package] = []
    relationships: list[Relationship] = []
    yaml_packages: IndexedDict = package_yaml["packages"]
    items: ItemsView[str, IndexedDict] = yaml_packages.items()
    for package_name, package_value in items:
        version: str | None = package_value.get("version")

        if not package_name or not version:
            continue

        current_location: Location = deepcopy(reader.location)
        if current_location.coordinates:
            position: Position = yaml_packages.get_key_position(package_name)
            current_location.coordinates.line = position.start.line
        metadata = DartPubspecLickEntry(
            name=package_name,
            version=version,
            hosted_url=get_hosted_url(package_value),
            vcs_url=get_vcs_url(package_value),
        )
        try:
            packages.append(
                Package(
                    name=package_name,
                    version=version,
                    locations=[current_location],
                    language=Language.DART,
                    licenses=[],
                    type=PackageType.DartPubPkg,
                    p_url=package_url(metadata),
                    metadata=metadata,
                )
            )
        except ValidationError as ex:
            LOGGER.warning(
                "Malformed package. Required fields are missing or data types "
                "are incorrect.",
                extra={
                    "extra": {
                        "exception": ex.errors(  # type: ignore
                            include_url=False,
                        ),
                        "location": current_location.path(),
                    }
                },
            )
            continue

    return packages, relationships
