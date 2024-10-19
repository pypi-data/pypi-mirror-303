from contextlib import (
    suppress,
)
from datetime import (
    datetime,
    timezone,
)
from fluid_sbom.artifact.relationship import (
    Relationship,
)
from fluid_sbom.file.location_read_closer import (
    LocationReadCloser,
)
from fluid_sbom.file.resolver import (
    Resolver,
)
from fluid_sbom.pkg.alpm import (
    AlpmDBEntry,
    AlpmFileRecord,
)
from fluid_sbom.pkg.cataloger.arch.package import (
    new_package,
)
from fluid_sbom.pkg.cataloger.generic.parser import (
    Environment,
)
from fluid_sbom.pkg.package import (
    Package,
)
from fluid_sbom.utils.file import (
    Digest,
)
import gzip
import os
from pathlib import (
    Path,
)
from typing import (
    Any,
    TextIO,
)

IGNORED_FILES = {
    "/set": True,
    ".BUILDINFO": True,
    ".PKGINFO": True,
    "": True,
}


def parse_pkg_files(pkg_fields: dict[str, Any]) -> AlpmDBEntry | None:
    entry = AlpmDBEntry()

    entry.licenses = pkg_fields.get("license", "")
    entry.base_package = pkg_fields.get("base", "")
    entry.package = pkg_fields.get("name", "")
    entry.version = pkg_fields.get("version", "")
    entry.description = pkg_fields.get("desc", "")
    entry.architecture = pkg_fields.get("arch", "")
    entry.size = pkg_fields.get("size", 0)
    entry.packager = pkg_fields.get("packager", "")
    entry.url = pkg_fields.get("url", "")
    entry.validation = pkg_fields.get("validation", "")
    entry.reason = pkg_fields.get("reason", 0)
    entry.files = list(
        AlpmFileRecord(path=item["path"], digests=item.get("digests"))
        for item in pkg_fields.get("files", [])
    )
    entry.backup = list(
        AlpmFileRecord(path=item["path"], digests=item["digests"])
        for item in pkg_fields.get("backup", [])
    )

    if not entry.package and not entry.files and not entry.backup:
        return None
    return entry


def parse_key_value_pair(line: str) -> dict[str, Any]:
    try:
        key, value = line.split("\n", 1)
    except ValueError:
        return {}
    key = key.replace("%", "").lower()
    value = value.strip()

    if key == "files":
        return {key: _parse_files(value)}
    if key == "backup":
        return {key: parse_backup(value)}
    if key in ["reason", "size"]:
        return {key: parse_numeric_field(key, value)}
    return {key: value}


def _parse_files(value: str) -> list[dict[str, Any]]:
    files = []
    for item in value.split("\n"):
        path = f"/{item}"
        if path not in IGNORED_FILES:
            files.append({"path": path})
    return files


def parse_backup(value: str) -> list[dict[str, Any]]:
    backup = []
    for item in value.split("\n"):
        backup_fields = item.split("\t", 1)
        path = f"/{backup_fields[0]}"
        if path not in IGNORED_FILES:
            backup.append(
                {
                    "path": path,
                    "digests": [
                        Digest(algorithm="md5", value=backup_fields[1])
                    ],
                }
            )
    return backup


def parse_numeric_field(key: str, value: str) -> int:
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"Failed to parse {key} to integer: {value}") from exc


def parse_alpm_db_entry(reader: TextIO) -> AlpmDBEntry | None:
    pkg_fields: dict[str, Any] = {}
    lines = reader.read().split("\n\n")
    for line in lines:
        if not line.strip():
            break  # End of block or file
        pkg_fields.update(parse_key_value_pair(line))

    return parse_pkg_files(pkg_fields)


def parse_mtree(reader: TextIO) -> list[AlpmFileRecord]:
    file_info: dict[str, dict[str, str]] = {}
    result_records: list[AlpmFileRecord] = []
    data = reader.read()

    for line in data.splitlines():
        if line.startswith(".") and "time=" in line:
            parts = line.strip().split()
            file_path = parts[0][
                1:
            ]  # Remove the leading '.' from the file path
            file_attributes = {}
            for part in parts[
                1:
            ]:  # Skip the first part, which is the file path
                if "=" in part:
                    key, value = part.split("=", 1)
                    file_attributes[key] = value
            file_info[file_path] = file_attributes
    for file_path, file_attributes in file_info.items():
        if file_path.startswith("/."):
            continue
        result = AlpmFileRecord(
            path=file_path,
            size=file_attributes.get("size"),
            time=datetime.fromtimestamp(
                float(file_attributes["time"]), tz=timezone.utc
            ),
            type=file_attributes.get("type"),
            digests=[
                Digest(
                    algorithm=key.replace("digest", ""),
                    value=value,
                )
                for key, value in file_attributes.items()
                if key.endswith("digest")
            ],
            uid=file_attributes.get("uid"),
            gid=file_attributes.get("gid"),
            link=file_attributes.get("link"),
        )
        result_records.append(result)
    return result_records


def parse_alpm_db(
    _resolver: Resolver, _env: Environment, reader: LocationReadCloser
) -> tuple[list[Package], list[Relationship]]:
    data = parse_alpm_db_entry(reader.read_closer)
    if not data or not reader.location.coordinates:
        return ([], [])
    with suppress(IndexError):
        mtree_location = _resolver.files_by_path(
            os.path.join(
                Path(reader.location.coordinates.real_path).parent, "mtree"
            )
        )[0]
        if mtree_reader := _resolver.file_contents_by_location(
            mtree_location, function_reader=gzip.open, mode="rt"
        ):
            data.files = parse_mtree(mtree_reader)
    with suppress(IndexError):
        files_location = _resolver.files_by_path(
            os.path.join(
                Path(reader.location.coordinates.real_path).parent, "files"
            )
        )[0]
        if (
            files_reader := _resolver.file_contents_by_location(files_location)
        ) and (files_metadata := parse_alpm_db_entry(files_reader)):
            data.backup = files_metadata.backup

    package = new_package(data, _env.linux_release, reader.location)

    return [package] if package else [], []
