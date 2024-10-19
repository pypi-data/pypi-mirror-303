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
)
from fluid_sbom.internal.collection.yaml import (
    parse_yaml_with_tree_sitter,
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
from packageurl import (
    PackageURL,
)
from typing import (
    cast,
    ItemsView,
)


def _get_location(location: Location, sourceline: int) -> Location:
    if location.coordinates:
        c_upd = {"line": sourceline}
        l_upd = {"coordinates": location.coordinates.model_copy(update=c_upd)}
        return location.model_copy(update=l_upd)
    return location


def _get_packages(
    reader: LocationReadCloser,
    dependencies: IndexedDict | None,
) -> list[Package]:
    if dependencies is None:
        return []

    general_location = _get_location(
        reader.location, dependencies.position.start.line
    )
    items: ItemsView[str, IndexedDict | str] = dependencies.items()
    return [
        Package(
            name=name,
            version=version,
            locations=[general_location],
            language=Language.DART,
            licenses=[],
            type=PackageType.DartPubPkg,
            p_url=PackageURL(  # type: ignore
                type="pub",
                name=name,
                version=version,
            ).to_string(),
        )
        for name, version in items
        if isinstance(version, str)
    ]


def parse_pubspec_yaml(
    _: Resolver | None, __: Environment | None, reader: LocationReadCloser
) -> tuple[list[Package], list[Relationship]]:
    content = cast(
        IndexedDict, parse_yaml_with_tree_sitter(reader.read_closer.read())
    )
    deps: IndexedDict | None = content.get("dependencies")
    dev_deps: IndexedDict | None = content.get("dev_dependencies")
    packages = [
        *_get_packages(reader, deps),
        *_get_packages(reader, dev_deps),
    ]
    return packages, []
