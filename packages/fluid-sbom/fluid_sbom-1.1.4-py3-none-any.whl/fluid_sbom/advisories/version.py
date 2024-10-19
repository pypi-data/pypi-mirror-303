from fluid_sbom.pkg.package import (
    Advisory,
    Package,
)
import logging
from packageurl import (
    PackageURL,
)
import re
from typing import (
    Self,
)
from univers.version_range import (
    InvalidVersionRange,
    RANGE_CLASS_BY_SCHEMES,
    VersionConstraint,
    VersionRange,
)
from univers.versions import (
    AlpineLinuxVersion,
    ComposerVersion,
    DebianVersion,
    GolangVersion,
    InvalidVersion,
    MavenVersion,
    NugetVersion,
    PypiVersion,
    RpmVersion,
    RubygemsVersion,
    SemverVersion,
    Version,
)

LOGGER = logging.getLogger(__name__)


def _get_version_scheme_by_namespace(
    package: Package, namespace: str
) -> Version | None:
    schemes = {
        "distro": {
            "alpine": AlpineLinuxVersion,
            "debian": DebianVersion,
            "redhat": RpmVersion,
            "ubuntu": DebianVersion,
        },
        "language": {
            "dart": SemverVersion,
            "dotnet": NugetVersion,
            "go": GolangVersion,
            "java": MavenVersion,
            "javascript": SemverVersion,
            "php": ComposerVersion,
            "python": PypiVersion,
            "ruby": RubygemsVersion,
            "rust": SemverVersion,
            "swift": SemverVersion,
        },
    }

    def _get_language_scheme() -> Version | None:
        return schemes["language"].get(package.language.value)

    def _get_distro_scheme() -> Version | None:
        if package.p_url:
            package_url = PackageURL.from_string(package.p_url)
            if isinstance(package_url.qualifiers, dict) and (
                distro := package_url.qualifiers.get("distro_id")
            ):
                return schemes["distro"].get(distro)
        return None

    parts = namespace.split(":")
    if len(parts) < 3:
        return _get_language_scheme() or _get_distro_scheme()

    namespace_type, subtype = parts[1], parts[2]
    result = schemes.get(namespace_type, {}).get(subtype)

    return result or _get_language_scheme() or _get_distro_scheme()


class ApkVersionRange(VersionRange):  # type: ignore[misc]
    scheme = "apk"
    version_class = AlpineLinuxVersion

    @classmethod
    def from_native(cls, string: str) -> Self:
        match = re.match(r"([<>=~!^]*)(.*)", string)
        if not match:
            raise ValueError(f"Invalid version range: {string}")
        comparator, version = match.groups()
        version = version.strip()
        return cls(
            constraints=[
                VersionConstraint(
                    comparator=comparator, version=cls.version_class(version)
                ),
            ]
        )


def _compare_single_constraint(
    version: Version,
    constraint: str,
    scheme: str,
) -> bool:
    version_range: VersionRange | None = {
        **RANGE_CLASS_BY_SCHEMES,
        "apk": ApkVersionRange,
    }.get(scheme)

    if not version_range:
        raise ValueError(f"Invalid version scheme: {scheme}")
    try:
        return version in version_range.from_native(constraint.strip())
    except (InvalidVersion, InvalidVersionRange, TypeError):
        return False


def _matches_constraint(
    version: Version, constraint: str, version_scheme: str
) -> bool:
    if not constraint:
        return True

    constraints = constraint.split("||")
    return any(
        _compare_single_constraint(version, constraint.strip(), version_scheme)
        for constraint in constraints
    )


def matches_version(package: Package, advisory: Advisory) -> bool:
    version_type = _get_version_scheme_by_namespace(
        package, advisory.namespace
    )
    if version_type is None:
        LOGGER.debug(
            "No version scheme found for namespace %s",
            advisory.namespace,
        )
        return False

    if advisory.version_constraint is None:
        return True
    if not package.p_url:
        return False

    try:
        match = re.match(r"([<>=~!^]*)(.*)", package.version)
        if not match:
            return False

        _, version = match.groups()
        version = version.strip()

        return all(
            _matches_constraint(
                version_type(version),
                constraint,
                PackageURL.from_string(package.p_url).type,
            )
            for constraint in advisory.version_constraint.split(",")
        )
    except (AttributeError, InvalidVersion):
        return False
