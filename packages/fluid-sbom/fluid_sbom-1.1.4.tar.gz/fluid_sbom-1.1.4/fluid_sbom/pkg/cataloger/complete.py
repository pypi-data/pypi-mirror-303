from fluid_sbom.pkg.cataloger.alpine import (
    package as package_alpine,
)
from fluid_sbom.pkg.cataloger.dart import (
    package as package_dart,
)
from fluid_sbom.pkg.cataloger.debian import (
    package as package_debian,
)
from fluid_sbom.pkg.cataloger.dotnet import (
    package as package_dotnet,
)
from fluid_sbom.pkg.cataloger.java import (
    package as package_java,
)
from fluid_sbom.pkg.cataloger.javascript import (
    package as package_js,
)
from fluid_sbom.pkg.cataloger.php import (
    package as package_php,
)
from fluid_sbom.pkg.cataloger.python import (
    package as package_python,
)
from fluid_sbom.pkg.cataloger.ruby import (
    package as package_ruby,
)
from fluid_sbom.pkg.cataloger.rust import (
    package as package_rust,
)
from fluid_sbom.pkg.package import (
    Package,
)
from fluid_sbom.pkg.type import (
    PackageType,
)
import logging
from pydantic import (
    ValidationError,
)

LOGGER = logging.getLogger(__name__)


def complete_package(package: Package) -> Package | None:
    completion_map = {
        PackageType.NpmPkg: package_js.complete_package,
        PackageType.DartPubPkg: package_dart.complete_package,
        PackageType.DotnetPkg: package_dotnet.complete_package,
        PackageType.JavaPkg: package_java.complete_package,
        PackageType.PhpComposerPkg: package_php.complete_package,
        PackageType.PythonPkg: package_python.complete_package,
        PackageType.GemPkg: package_ruby.complete_package,
        PackageType.RustPkg: package_rust.complete_package,
        PackageType.DebPkg: package_debian.complete_package,
        PackageType.ApkPkg: package_alpine.complete_package,
    }

    try:
        if package.type in completion_map:
            package = completion_map[package.type](package)  # type: ignore
            package.model_validate(package.__dict__)
    except ValidationError as ex:
        LOGGER.warning(
            "Malformed package completion. Required fields are missing "
            "or data types are incorrect.",
            extra={
                "extra": {
                    "exception": ex.errors(include_url=False),
                    "location": package.locations,
                    "package_type": package.type,
                }
            },
        )
        return None

    return package
