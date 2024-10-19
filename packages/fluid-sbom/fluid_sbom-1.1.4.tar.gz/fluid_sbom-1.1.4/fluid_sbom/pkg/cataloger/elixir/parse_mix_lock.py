from copy import (
    deepcopy,
)
from fluid_sbom.artifact.relationship import (
    Relationship,
    RelationshipType,
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
from fluid_sbom.pkg.cataloger.elixir.package import (
    new_package,
)
from fluid_sbom.pkg.cataloger.generic.parser import (
    Environment,
)
from fluid_sbom.pkg.elixir import (
    ElixirMixLockEntry,
)
from fluid_sbom.pkg.package import (
    Package,
)
import os
from tree_sitter import (
    Language as TLanguage,
    Node,
    Parser,
)


def process_entry(entry: Node, location: Location) -> Package | None:
    name = next(
        x for x in entry.named_children if x.type == "package_name"
    ).text.decode("utf-8")[1:-1]
    version = next(
        x for x in entry.named_children if x.type == "version"
    ).text.decode("utf-8")[1:-1]
    pkg_hash = next(
        x for x in entry.named_children if x.type == "checksum"
    ).text.decode("utf-8")[1:-1]
    pkg_hash_ext = next(
        x for x in entry.named_children if x.type == "optional_checksum"
    ).text.decode("utf-8")[1:-1]
    new_location = deepcopy(location)
    if new_location.coordinates:
        new_location.coordinates.line = entry.start_point[0] + 1

    package = new_package(
        ElixirMixLockEntry(
            name=name,
            version=version,
            pkg_hash=pkg_hash,
            pkg_hash_ext=pkg_hash_ext,
        ),
        new_location,
    )

    return package if package else None


def collect_dependencies(
    packages: list[Package], package_entries: list[Node]
) -> list[Relationship]:
    relationships: list[Relationship] = []
    for entry in package_entries:
        current_package_name = next(
            x for x in entry.named_children if x.type == "package_name"
        ).text.decode("utf-8")[1:-1]
        for dependency_list in next(
            node
            for node in entry.named_children
            if node.type == "dependencies"
        ).named_children:
            dependencies = [
                next(
                    y for y in x.named_children if y.type == "atom"
                ).text.decode("utf-8")[1:]
                for x in dependency_list.named_children
                if x.type == "dependency"
            ]
            relationships.extend(
                Relationship(
                    from_=next(x for x in packages if x.name == dep_name),
                    to_=next(
                        x for x in packages if x.name == current_package_name
                    ),
                    type=RelationshipType.DEPENDENCY_OF_RELATIONSHIP,
                    data=None,
                )
                for dep_name in dependencies
                if next((x for x in packages if x.name == dep_name), None)
            )
    return relationships


def collect_entries(
    _content: str, location: Location
) -> tuple[list[Package], list[Relationship]]:
    parser = Parser()
    parser.set_language(
        TLanguage(
            os.path.join(
                os.environ["TREE_SITTETR_PARSERS_DIR"],
                "mix_lock.so",
            ),
            "mix_lock",
        )
    )
    result = parser.parse(_content.encode("utf-8"))
    package_entries = list(
        node
        for node in result.root_node.children
        if node.type == "package_entry"
    )

    packages = [
        package
        for x in package_entries
        if (package := process_entry(x, location)) is not None
    ]
    relations = collect_dependencies(packages, package_entries)

    return packages, relations


def parse_mix_lock(
    _: Resolver | None,
    __: Environment | None,
    reader: LocationReadCloser,
) -> tuple[list[Package], list[Relationship]]:
    packages: list[Package] = []
    relationships: list[Relationship] = []

    parser = Parser()
    parser.set_language(
        TLanguage(
            os.path.join(
                os.environ["TREE_SITTETR_PARSERS_DIR"],
                "mix_lock.so",
            ),
            "mix_lock",
        )
    )
    result = parser.parse(reader.read_closer.read().encode("utf-8"))
    package_entries = list(
        node
        for node in result.root_node.children
        if node.type == "package_entry"
    )

    packages = [
        package
        for x in package_entries
        if (package := process_entry(x, reader.location))
    ]
    relationships = collect_dependencies(packages, package_entries)

    return packages, relationships
