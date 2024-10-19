from collections import (
    defaultdict,
)
from cyclonedx.factory.license import (
    LicenseFactory,
)
from cyclonedx.model import (
    Tool,
)
from cyclonedx.model.bom import (
    Bom,
)
from cyclonedx.model.component import (
    Component,
    ComponentType,
)
from cyclonedx.model.license import (
    LicenseExpression,
)
from cyclonedx.output import (
    make_outputter,
)
from cyclonedx.output.json import (
    JsonV1Dot5,
)
from cyclonedx.schema import (
    OutputFormat,
    SchemaVersion,
)
from cyclonedx.validation import (
    make_schemabased_validator,
)
from cyclonedx.validation.json import (
    JsonStrictValidator,
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
    CycloneDXValidationError,
)
import logging
from packageurl import (
    PackageURL,
)
from typing import (
    cast,
    TYPE_CHECKING,
)

LOGGER = logging.getLogger(__name__)


if TYPE_CHECKING:
    from cyclonedx.output.json import (
        Json as JsonOutputter,
    )
    from cyclonedx.output.xml import (
        Xml as XmlOutputter,
    )
    from cyclonedx.validation.xml import (
        XmlValidator,
    )


def format_cyclone_json(bom: Bom, output: str) -> None:
    file_path = f"{output}.json"
    json_output: "JsonOutputter" = JsonV1Dot5(bom)
    serialized_json = json_output.output_as_string()

    json_validator = JsonStrictValidator(SchemaVersion.V1_5)
    validation_error = json_validator.validate_str(serialized_json)

    if validation_error:
        raise CycloneDXValidationError(validation_error)

    LOGGER.info("🆗 CycloneDx JSON valid, output file at %s", file_path)
    json_output.output_to_file(file_path, True, indent=2)
    LOGGER.info("✅ Output file successfully generated")


def format_cyclone_xml(bom: Bom, output: str) -> None:
    file_path = f"{output}.xml"
    xml_outputter: "XmlOutputter" = make_outputter(
        bom, OutputFormat.XML, SchemaVersion.V1_5
    )
    serialized_xml = xml_outputter.output_as_string()

    xml_validator: "XmlValidator" = make_schemabased_validator(
        xml_outputter.output_format, xml_outputter.schema_version
    )
    validation_error = xml_validator.validate_str(serialized_xml)

    if validation_error:
        raise CycloneDXValidationError(validation_error)

    LOGGER.info("🆗 CycloneDx XML valid, output file at %s", file_path)
    xml_outputter.output_to_file(file_path, True, indent=2)
    LOGGER.info("✅ Output file successfully generated")


def pkg_to_component(package: Package) -> Component:
    lc_factory = LicenseFactory()
    licenses = []
    for lic in package.licenses:
        item = lc_factory.make_from_string(lic)
        if not isinstance(item, LicenseExpression):
            licenses.append(item)
    return Component(
        type=ComponentType.LIBRARY,
        name=package.name,
        version=package.version,
        licenses=licenses,
        bom_ref=f"{package.name}@{package.version}",
        purl=PackageURL.from_string(package.p_url),
    )


def format_cyclonedx_sbom(  # pylint:disable=too-many-locals
    packages: list[Package],
    relationships: list[Relationship],
    file_format: str,
    output: str,
    config: SbomConfig,
) -> None:
    namespace, version = set_namespace_version(config=config)
    bom = Bom()
    bom.metadata.component = root_component = Component(
        name=namespace,
        type=ComponentType.APPLICATION,
        licenses=[],
        bom_ref="",
        version=version,
    )
    bom.metadata.tools.add(Tool(vendor="Fluid Attacks", name="Fluid-Sbom"))

    component_cache = {pkg: pkg_to_component(pkg) for pkg in packages}

    components = component_cache.values()
    for component in components:
        bom.components.add(component)
        bom.register_dependency(root_component, [component])

    dependency_map: dict[Component, list[Component]] = defaultdict(list)

    for relationship in relationships:
        to_pkg = component_cache.get(
            cast(Package, relationship.to_),
            pkg_to_component(cast(Package, relationship.to_)),
        )
        from_pkg = component_cache.get(
            cast(Package, relationship.from_),
            pkg_to_component(cast(Package, relationship.from_)),
        )

        dependency_map[to_pkg].append(from_pkg)

    for ref, depends_on_list in dependency_map.items():
        bom.register_dependency(ref, depends_on_list)

    match file_format:
        case "cyclonedx-json":
            format_cyclone_json(bom, output)
        case "cyclonedx-xml":
            format_cyclone_xml(bom, output)
