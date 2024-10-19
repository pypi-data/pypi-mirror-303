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
from fluid_sbom.internal.collection.json import (
    parse_json_with_tree_sitter,
)
from fluid_sbom.internal.collection.types import (
    IndexedDict,
)
from fluid_sbom.pkg.cataloger.generic.parser import (
    Environment,
)
from fluid_sbom.pkg.cataloger.python.package import (
    package_url,
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


def _get_version(value: IndexedDict) -> str:
    version: str = value["version"]
    return version.strip("=<>~^ ")


def _get_packages(
    reader: LocationReadCloser,
    dependencies: IndexedDict | None,
) -> list[Package]:
    if dependencies is None:
        return []

    items: ItemsView[str, IndexedDict] = dependencies.items()
    return [
        Package(
            name=name,
            version=_get_version(value),
            locations=[
                _get_location(reader.location, value.position.start.line)
            ],
            language=Language.PYTHON,
            type=PackageType.PythonPkg,
            p_url=package_url(
                name=name,
                version=_get_version(value),
                package=None,
            ),
            licenses=[],
        )
        for name, value in items
    ]


def parse_pipfile_lock_deps(
    _resolver: Resolver | None,
    _env: Environment | None,
    reader: LocationReadCloser,
) -> tuple[list[Package], list[Relationship]]:
    content = cast(
        IndexedDict, parse_json_with_tree_sitter(reader.read_closer.read())
    )
    deps: IndexedDict | None = content.get("default")
    dev_deps: IndexedDict | None = content.get("develop")
    packages = [
        *_get_packages(reader, deps),
        *_get_packages(reader, dev_deps),
    ]
    return packages, []
