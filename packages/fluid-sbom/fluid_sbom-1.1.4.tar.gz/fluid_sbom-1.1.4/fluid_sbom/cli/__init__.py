# pylint:disable=no-value-for-parameter
import click
from concurrent.futures import (
    ThreadPoolExecutor,
)
from fluid_sbom.advisories.database import (
    DATABASE,
)
from fluid_sbom.config.bugsnag import (
    initialize_bugsnag,
)
from fluid_sbom.config.config import (
    SbomConfig,
    SourceType,
)
from fluid_sbom.config.logger import (
    configure_logger,
)
from fluid_sbom.context.image import (
    get_context,
)
from fluid_sbom.format import (
    format_sbom,
)
from fluid_sbom.internal.file_resolver.container_image import (
    ContainerImage,
)
from fluid_sbom.internal.file_resolver.directory import (
    Directory,
)
from fluid_sbom.internal.operations.package_operation import (
    package_operations_factory,
)
from fluid_sbom.pkg.cataloger.complete import (
    complete_package,
)
from fluid_sbom.sources.docker import (
    get_docker_image,
)
import logging
import os
import textwrap

LOGGER = logging.getLogger(__name__)


def show_banner() -> None:
    logo = textwrap.dedent(
        """
         ───── ⌝
        |    ⌝|  Fluid Attacks
        |  ⌝  |  We hack your software.
         ─────
        """
    )
    click.secho(logo, fg="red")


@click.command()
@click.argument("source")
@click.option(
    "--from",
    "o_from",
    type=click.Choice(
        ["docker", "dir", "docker-daemon"], case_sensitive=False
    ),
    help=(
        "Source of the scan: 'docker' for scanning Docker images "
        "or 'dir' for scanning directories."
    ),
    required=True,
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(
        [
            "fluid-json",
            "cyclonedx-json",
            "spdx-json",
            "cyclonedx-xml",
            "spdx-xml",
        ],
        case_sensitive=False,
    ),
    default="fluid-json",
    help="Output format for the scanned data.",
)
@click.option(
    "--output",
    "-o",
    help="Output filename.",
    default="sbom",
)
@click.option(
    "--docker-user",
    help="Docker registry username.",
)
@click.option(
    "--docker-password",
    help="Docker registry password.",
)
def scan(  # pylint:disable=too-many-arguments
    source: str,
    o_from: str,
    output_format: str,
    output: str,
    docker_user: str | None = None,
    docker_password: str | None = None,
) -> None:
    configure_logger()
    initialize_bugsnag()
    show_banner()
    config = SbomConfig(
        source=source,
        source_type=SourceType.from_string(o_from),
        output_format=output_format,
        output=output,
        resolver=None,
    )

    match config.source_type:
        case SourceType.DIRECTORY:
            config.resolver = Directory(root=source)
        case SourceType.DOCKER | SourceType.DOCKER_DAEMON:
            daemon = config.source_type == SourceType.DOCKER_DAEMON
            docker_image = get_docker_image(
                source,
                username=docker_user,
                password=docker_password,
                daemon=daemon,
            )
            if not docker_image:
                raise ValueError(f"No image found for {source}")

            context = get_context(
                docker_image,
                username=docker_user,
                password=docker_password,
                daemon=daemon,
            )
            if context is None:
                raise ValueError(f"No context found for {docker_image}")
            config.resolver = ContainerImage(
                img=docker_image, context=context, lazy=False
            )
        case _:
            raise ValueError(f"Unknown source: {source}")

    DATABASE.initialize()
    LOGGER.info("📦 Generating SBOM from %s: %s", o_from, source)

    packages, relationships = package_operations_factory(config.resolver)
    with ThreadPoolExecutor(
        max_workers=min(
            32, (os.cpu_count() or 1) * 5 if os.cpu_count() is not None else 32
        )
    ) as executor:
        LOGGER.info("📦 Gathering additional package information")
        packages = list(filter(None, executor.map(complete_package, packages)))

    LOGGER.info("📦 Preparing %s report", config.output_format)
    format_sbom(packages, relationships, config)


if __name__ == "__main__":
    scan(prog_name="sbom")
