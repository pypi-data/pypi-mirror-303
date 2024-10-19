from copy import (
    deepcopy,
)
from fluid_sbom.artifact.relationship import (
    Relationship,
    RelationshipType,
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
from fluid_sbom.pkg.cataloger.ruby.package import (
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
import logging
import os
from pydantic import (
    ValidationError,
)
from tree_sitter import (
    Language as TLanguage,
    Node,
    Parser,
)

LOGGER = logging.getLogger(__name__)


def collect_gem_entries(_content: str) -> list[Node]:
    parser = Parser()
    parser.set_language(
        TLanguage(
            os.path.join(
                os.environ["TREE_SITTETR_PARSERS_DIR"],
                "gemfilelock.so",
            ),
            "gemfilelock",
        )
    )
    result = parser.parse(_content.encode("utf-8"))
    gem_section = next(
        (
            node
            for node in result.root_node.children
            if node.type == "gem_section"
        ),
        None,
    )
    if gem_section and (
        specs := next(
            (x for x in gem_section.children[1].children if x.type == "specs"),
            None,
        )
    ):
        return [x.children[0] for x in specs.children[1:]]

    return []


def parse_gemfile_lock(
    _: Resolver | None,
    __: Environment | None,
    reader: LocationReadCloser,
) -> tuple[list[Package], list[Relationship]]:
    packages: list[Package] = []
    relationships: list[Relationship] = []
    gem_entries = collect_gem_entries(reader.read_closer.read())

    packages = _process_packages(gem_entries, reader)
    relationships = _process_dependencies(gem_entries, packages)

    return packages, relationships


def _process_packages(
    gem_entries: list, reader: LocationReadCloser
) -> list[Package]:
    packages = []

    for gem_entry in gem_entries:
        gem_name = gem_entry.named_children[0].text.decode("utf-8")
        gem_version = gem_entry.named_children[1].text.decode("utf-8")

        if not gem_name or not gem_version:
            continue

        location = deepcopy(reader.location)
        if location.coordinates:
            location.coordinates.line = gem_entry.start_point[0] + 1

        try:
            packages.append(
                Package(
                    name=gem_name,
                    version=gem_version,
                    locations=[location],
                    language=Language.RUBY,
                    licenses=[],
                    p_url=package_url(gem_name, gem_version),
                    type=PackageType.GemPkg,
                    metadata=None,
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

    return packages


def _process_dependencies(
    gem_entries: list, packages: list[Package]
) -> list[Relationship]:
    relationships = []

    for gem_entry in gem_entries:
        gem_entry_name = gem_entry.named_children[0].text.decode("utf-8")
        _package = next(
            (pkg for pkg in packages if pkg.name == gem_entry_name), None
        )

        if not _package or not gem_entry.parent:
            continue

        for dependency_node in (
            x for x in gem_entry.parent.children if x.type == "dependency"
        ):
            dependency_name = dependency_node.named_children[0].text.decode(
                "utf-8"
            )
            dependency_package = next(
                (pkg for pkg in packages if pkg.name == dependency_name), None
            )

            if dependency_package:
                relationships.append(
                    Relationship(
                        from_=_package,
                        to_=dependency_package,
                        type=RelationshipType.DEPENDENCY_OF_RELATIONSHIP,
                        data=None,
                    )
                )

    return relationships
