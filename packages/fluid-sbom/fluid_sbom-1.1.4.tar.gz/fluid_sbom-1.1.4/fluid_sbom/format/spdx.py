from datetime import (
    datetime,
    UTC,
)
from fluid_sbom.artifact.relationship import (
    Relationship,
)
from fluid_sbom.config.config import (
    SbomConfig,
)
from fluid_sbom.format.common import (
    set_namespace_version,
)
from fluid_sbom.pkg.package import (
    Package,
)
from fluid_sbom.utils.exceptions import (
    SPDXValidationError,
)
import logging
import os
import re
from spdx_tools.spdx.model.actor import (
    Actor,
    ActorType,
)
from spdx_tools.spdx.model.document import (
    CreationInfo,
    Document,
)
from spdx_tools.spdx.model.package import (
    ExternalPackageRef,
    ExternalPackageRefCategory,
    Package as SPDX_Package,
    PackagePurpose,
)
from spdx_tools.spdx.model.relationship import (
    Relationship as SPDXRelationship,
    RelationshipType as SPDXRelationshipType,
)
from spdx_tools.spdx.model.spdx_no_assertion import (
    SpdxNoAssertion,
)
from spdx_tools.spdx.validation.document_validator import (
    validate_full_spdx_document,
)
from spdx_tools.spdx.validation.validation_message import (
    ValidationMessage,
)
from spdx_tools.spdx.writer.write_anything import (
    write_file,
)
from typing import (
    cast,
)
from urllib.parse import (
    urlunparse,
)
import uuid

LOGGER = logging.getLogger(__name__)

NOASSERTION = SpdxNoAssertion()


def clear_name(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9.-]", "-", text)


def get_spdx_id(package: Package) -> str:
    name = clear_name(package.name)
    pkg_platform = clear_name(package.type.value.lower())
    pkg_id = package.id_
    return f"SPDXRef-Package-{pkg_platform}-{name}-{pkg_id}"


def document_namespace(working_dir: str) -> str:
    input_type = "unknown-source-type"

    if os.path.isfile(working_dir):
        input_type = "file"
    elif os.path.isdir(working_dir):
        input_type = "dir"

    unique_id = uuid.uuid4()
    identifier = os.path.join(input_type, str(unique_id))
    if working_dir != ".":
        identifier = os.path.join(input_type, f"{working_dir}-{unique_id}")

    doc_namespace = urlunparse(
        ("https", "fluidattacks.com", identifier, "", "", ""),
    )

    return doc_namespace


def package_to_spdx_pkg(package: Package) -> SPDX_Package:
    return SPDX_Package(
        name=package.name,
        download_location=NOASSERTION,
        spdx_id=get_spdx_id(package),
        version=package.version,
        license_concluded=NOASSERTION,
        primary_package_purpose=PackagePurpose.LIBRARY,
        external_references=[
            ExternalPackageRef(
                category=ExternalPackageRefCategory.PACKAGE_MANAGER,
                reference_type="purl",
                locator=package.p_url,
            )
        ],
    )


def add_empty_package(document: Document) -> None:
    document.creation_info.document_comment = (
        "No packages or relationships were found in the root."
    )

    empty_package = SPDX_Package(
        name="NONE",
        spdx_id="SPDXRef-Package-NONE",
        download_location=NOASSERTION,
        license_concluded=NOASSERTION,
        primary_package_purpose=PackagePurpose.LIBRARY,
    )

    document.packages = [empty_package]
    document.relationships = []


def add_packages_and_relationships(
    document: Document,
    packages: list[Package],
    _relationships: list[Relationship],
) -> None:
    package_cache = {pkg: package_to_spdx_pkg(pkg) for pkg in packages}

    spdx_packages: list[SPDX_Package] = list(package_cache.values())
    document.packages = spdx_packages

    doc_spdx_id = document.creation_info.spdx_id
    document_relationships = [
        SPDXRelationship(
            doc_spdx_id, SPDXRelationshipType.DESCRIBES, pkg.spdx_id
        )
        for pkg in spdx_packages
    ]

    for relationship in _relationships:
        to_pkg = package_cache.get(
            cast(Package, relationship.to_),
            package_to_spdx_pkg(cast(Package, relationship.to_)),
        )
        from_pkg = package_cache.get(
            cast(Package, relationship.from_),
            package_to_spdx_pkg(cast(Package, relationship.from_)),
        )

        document_relationships.append(
            SPDXRelationship(
                to_pkg.spdx_id,
                SPDXRelationshipType.DEPENDENCY_OF,
                from_pkg.spdx_id,
            )
        )

    document.relationships = document_relationships


def format_spdx_sbom(
    packages: list[Package],
    _relationships: list[Relationship],
    file_format: str,
    output: str,
    config: SbomConfig,
) -> None:
    now_utc = datetime.now(UTC)
    namespace, _ = set_namespace_version(config=config)
    creation_info = CreationInfo(
        spdx_version="SPDX-2.3",
        spdx_id="SPDXRef-DOCUMENT",
        name=namespace,
        data_license="CC0-1.0",
        document_namespace=document_namespace(namespace),
        creators=[Actor(ActorType.TOOL, "Fluid-Sbom", None)],
        created=now_utc,
    )

    document = Document(creation_info)

    if not packages and not _relationships:
        add_empty_package(document)
    else:
        add_packages_and_relationships(document, packages, _relationships)

    validation_errors: list[ValidationMessage] = validate_full_spdx_document(
        document
    )

    if validation_errors:
        raise SPDXValidationError(validation_errors)

    LOGGER.info(
        "🆗 SPDX %s valid, generating output file at %s.%s",
        file_format.upper(),
        output,
        file_format,
    )

    write_file(document, f"{output}.{file_format}")
    LOGGER.info("✅ Output file successfully generated")
