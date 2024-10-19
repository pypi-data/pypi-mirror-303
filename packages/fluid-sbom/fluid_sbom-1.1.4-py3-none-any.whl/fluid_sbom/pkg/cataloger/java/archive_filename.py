from fluid_sbom.pkg.type import (
    PackageType,
)
import os
from pydantic import (
    BaseModel,
)
import re

# Compile regular expressions
name_and_version_pattern = re.compile(
    (
        r"(?i)^(?P<name>[a-zA-Z][\w.]*?(?:-[a-zA-Z][\w.]*?)*?)"
        r"(?:-(?P<version>\d.*|build\d.*|rc?\d+(?:[^\w].*)?))?$"
    )
)
secondary_version_pattern = re.compile(
    r"(?:[._-](?P<version>(\d.*|build\d+.*|"  # NOSONAR
    r"rc?\d+(?:[a-zA-Z].*)?)))?$"  # NOSONAR
)


class ArchiveFilename(BaseModel):
    raw: str
    name: str
    version: str

    def extension(self) -> str:
        return os.path.splitext(self.raw)[1][
            1:
        ].lower()  # Strip the dot and convert to lower case

    def pkg_type(self) -> PackageType:
        extension = self.extension()
        if extension in ["jar", "war", "ear", "lpkg", "par", "sar", "nar"]:
            return PackageType.JavaPkg
        if extension in ["jpi", "hpi"]:
            return PackageType.JenkinsPluginPkg

        return PackageType.UnknownPkg


def parse_filename(raw: str) -> ArchiveFilename:
    # Trim the file extension and remove any path prefixes
    cleaned_filename = os.path.splitext(os.path.basename(raw))[0]

    matches = name_and_version_pattern.search(cleaned_filename)

    name = get_subexp(matches, "name")
    version = get_subexp(matches, "version")

    # Some jars are named with different conventions,
    # like `_<version>` or `.<version>`
    if not version:
        matches = secondary_version_pattern.search(name)
        secondary_version = get_subexp(matches, "version")
        if secondary_version:
            name = name[: len(name) - len(secondary_version) - 1]
            version = secondary_version
    return ArchiveFilename(raw=raw, name=name, version=version)


def get_subexp(matches: re.Match[str] | None, subexp_name: str) -> str:
    if matches:
        return matches.group(subexp_name) or ""

    return ""
