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
from fluid_sbom.linux.release import (
    Release,
)
from fluid_sbom.pkg.apk import (
    ApkDBEntry,
    ApkFileRecord,
)
from fluid_sbom.pkg.cataloger.alpine.package import (
    new_package,
    ParsedData,
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
import os
from pydantic import (
    BaseModel,
    ConfigDict,
)
import re
from typing import (
    cast,
    TypedDict,
)

APK_DB_GLOB = "**/lib/apk/db/installed"
FileInfo = TypedDict("FileInfo", {"uid": str, "gid": str, "perms": str})


class ApkField(BaseModel):
    name: str
    value: str
    model_config = ConfigDict(frozen=True)


class ApkFileParsingContext(BaseModel):
    files: list[ApkFileRecord]
    index_of_latest_directory: int
    index_of_latest_regular_file: int


def _parse_list_values(
    value: str | None, delimiter: str | None = None
) -> list[str]:
    delimiter = delimiter or " "
    if not value:
        return []
    return value.split(delimiter)


def _process_file_info(
    info: str,
) -> FileInfo | None:
    file_info = info.split(":")
    if len(file_info) < 3:
        return None
    return {"uid": file_info[0], "gid": file_info[1], "perms": file_info[2]}


def process_checksum(value: str) -> Digest:
    algorithm = "md5"
    if value.startswith("Q1"):
        algorithm = "'Q1'+base64(sha1)"
    return Digest(algorithm=algorithm, value=value)


def find_release(db_path: str) -> list[Release] | None:
    location = os.path.normpath(
        os.path.join(db_path, "../../../etc/apk/repositories")
    )
    if not os.path.exists(location):
        return None
    return None


def parse_apk_db(
    _resolver: Resolver,
    _env: Environment | None,
    reader: LocationReadCloser,
) -> tuple[list[Package], list[Relationship]] | None:
    content = reader.read_closer.read()
    apks = [
        parsed_package
        for package in content.strip().split("\n\n")
        if package and (parsed_package := parse_package(package)) is not None
    ]

    entries = [
        entry
        for apk in apks
        if (
            entry := new_package(
                apk, _env.linux_release if _env else None, reader.location
            )
        )
        is not None
    ]

    return entries, discover_package_dependencies(entries)


def parse_package(package: str) -> ParsedData | None:
    data: dict[str, str] = {}
    ctx = ApkFileParsingContext(
        files=[], index_of_latest_directory=-1, index_of_latest_regular_file=-1
    )
    lines = package.split("\n")
    key = ""
    for line in lines:
        key = process_line(line, key, data, ctx)
    return construct_apk(data, ctx)


def process_line(
    line: str, key: str, data: dict[str, str], ctx: ApkFileParsingContext
) -> str:
    if ":" in line:
        key, value = line.split(":", 1)
        data[key] = value
        update_context_with_line(key, value, ctx)
    elif key and key in data:
        data[key] += "\n" + line.strip()
    return key


def update_context_with_line(
    key: str, value: str, ctx: ApkFileParsingContext
) -> None:
    match key:
        case "F":
            ctx.files.append(ApkFileRecord(path=os.path.join("/", value)))
            ctx.index_of_latest_directory = len(ctx.files) - 1
        case "M":
            index = ctx.index_of_latest_directory
            latest = ctx.files[index]
            if file_info := _process_file_info(value):
                latest.owner_uid = file_info["uid"]
                latest.owner_gid = file_info["gid"]
                latest.permissions = file_info["perms"]
            ctx.files[index] = latest
        case "R":
            index = ctx.index_of_latest_directory
            if index < 0:
                regular_file = os.path.join("/", value)
            else:
                latest_dir_path = ctx.files[index].path
                regular_file = os.path.join(latest_dir_path, value)
            ctx.files.append(ApkFileRecord(path=regular_file))
            ctx.index_of_latest_regular_file = len(ctx.files) - 1
        case "a":
            index = ctx.index_of_latest_regular_file
            latest = ctx.files[index]
            if file_info := _process_file_info(value):
                latest.owner_uid = file_info["uid"]
                latest.owner_gid = file_info["gid"]
                latest.permissions = file_info["perms"]
            ctx.files[index] = latest
        case "Z":
            index = ctx.index_of_latest_regular_file
            latest = ctx.files[index]
            latest.digest = process_checksum(value)


def construct_apk(
    data: dict[str, str], ctx: ApkFileParsingContext
) -> ParsedData | None:
    if not (package := data.get("P")) or not (version := data.get("V")):
        return None

    return ParsedData(
        apk_db_entry=ApkDBEntry(
            package=package,
            origin_package=data.get("o"),
            maintainer=data.get("m"),
            version=version,
            architecture=data.get("A"),
            url=data.get("U", ""),
            description=data.get("T", ""),
            size=data.get("S", ""),
            installed_size=data.get("I"),
            dependencies=_parse_list_values(data.get("D")),
            provides=_parse_list_values(data.get("p")),
            checksum=data.get("C"),
            git_commit=data.get("c"),
            files=ctx.files,
        ),
        license=data.get("L"),
    )


def _build_lookup_table(pkgs: list[Package]) -> dict[str, list[Package]]:
    lookup: dict[str, list[Package]] = {}

    for pkg in pkgs:
        apkg: ApkDBEntry = cast(ApkDBEntry, pkg.metadata)
        if pkg.name not in lookup:
            lookup[pkg.name] = [pkg]
        else:
            lookup[pkg.name].append(pkg)

        for provides in apkg.provides:
            provides_k = strip_version_specifier(provides)
            if provides_k not in lookup:
                lookup[provides_k] = [pkg]
            else:
                lookup[provides_k].append(pkg)

    return lookup


def discover_package_dependencies(  # NOSONAR
    pkgs: list[Package],
) -> list[Relationship]:
    lookup: dict[str, list[Package]] = _build_lookup_table(pkgs)
    relationships: list[Relationship] = []

    for pkg in pkgs:
        apkg = cast(ApkDBEntry, pkg.metadata)
        for dep_specifier in apkg.dependencies:
            dep = strip_version_specifier(dep_specifier)
            for dep_pk in lookup.get(dep, []):
                relationships.append(
                    Relationship(
                        from_=dep_pk,
                        to_=pkg,
                        type=RelationshipType.DEPENDENCY_OF_RELATIONSHIP,
                        data={},
                    )
                )
    return relationships


def strip_version_specifier(version: str) -> str:
    return re.split("[<>=]", version)[0]
