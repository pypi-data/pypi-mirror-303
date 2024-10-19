from fluid_sbom.pkg.cataloger.redhat.rpmdb.entry import (
    IndexEntry,
)
from fluid_sbom.pkg.cataloger.redhat.rpmdb.file_digest import (
    DigestAlgorithm,
)
from fluid_sbom.pkg.cataloger.redhat.rpmdb.rpmtags import (
    RPM_BIN_TYPE,
    RPM_I18NSTRING_TYPE,
    RPM_INT16_TYPE,
    RPM_INT32_TYPE,
    RPM_STRING_ARRAY_TYPE,
    RPM_STRING_TYPE,
    RPMTAG_ARCH,
    RPMTAG_BASENAMES,
    RPMTAG_DIRINDEXES,
    RPMTAG_DIRNAMES,
    RPMTAG_EPOCH,
    RPMTAG_FILEDIGESTALGO,
    RPMTAG_FILEDIGESTS,
    RPMTAG_FILEFLAGS,
    RPMTAG_FILEGROUPNAME,
    RPMTAG_FILEMODES,
    RPMTAG_FILESIZES,
    RPMTAG_FILEUSERNAME,
    RPMTAG_INSTALLTIME,
    RPMTAG_LICENSE,
    RPMTAG_MODULARITYLABEL,
    RPMTAG_NAME,
    RPMTAG_PGP,
    RPMTAG_PROVIDENAME,
    RPMTAG_RELEASE,
    RPMTAG_REQUIRENAME,
    RPMTAG_SIGMD5,
    RPMTAG_SIZE,
    RPMTAG_SOURCERPM,
    RPMTAG_SUMMARY,
    RPMTAG_VENDOR,
    RPMTAG_VERSION,
)
import io
from pydantic import (
    BaseModel,
    Field,
)
import struct
import time
from typing import (
    Callable,
)

SIZE_OF_UINT16 = 2
SIZE_OF_INT32 = 4


class PackageInfo(BaseModel):
    epoch: int | None = None
    name: str = ""
    version: str = ""
    release: str = ""
    arch: str = ""
    source_rpm: str = ""
    size: int = 0
    license: str = ""
    vendor: str = ""
    modularity_label: str = ""
    summary: str = ""
    pgp: str = ""
    sig_md5: str = ""
    digest_algorithm: DigestAlgorithm | None = None
    install_time: int = 0
    base_names: list[str] = Field(default_factory=list)
    dir_indexes: list[int] = Field(default_factory=list)
    dir_names: list[str] = Field(default_factory=list)
    file_sizes: list[int] = Field(default_factory=list)
    file_digests: list[str] = Field(default_factory=list)
    file_modes: list[int] = Field(default_factory=list)
    file_flags: list[int] = Field(default_factory=list)
    user_names: list[str] = Field(default_factory=list)
    group_names: list[str] = Field(default_factory=list)
    provides: list[str] = Field(default_factory=list)
    requires: list[str] = Field(default_factory=list)


class PgpSig:  # pylint: disable=too-few-public-methods
    pub_key_algo: int
    hash_algo: int
    key_id: bytes
    date: int

    def __init__(self, data: bytes) -> None:
        (
            self.date,
            self.key_id,
            self.pub_key_algo,
            self.hash_algo,
        ) = struct.unpack(">3x i 8s BB", data)


class TextSig:  # pylint: disable=too-few-public-methods
    pub_key_algo: int
    hash_algo: int
    key_id: bytes
    date: int

    def __init__(self, data: bytes) -> None:
        (
            self.pub_key_algo,
            self.hash_algo,
            self.date,
            self.key_id,
        ) = struct.unpack(">2x BB 4x i 4x 8s", data)


class Pgp4Sig:  # pylint: disable=too-few-public-methods
    pub_key_algo: int
    hash_algo: int
    key_id: bytes
    date: int

    def __init__(self, data: bytes) -> None:
        (
            self.pub_key_algo,
            self.hash_algo,
            self.key_id,
            self.date,
        ) = struct.unpack(">2x BB 17x 8s 2x i", data)


def parse_int32_array(data: bytes, array_size: int) -> list[int]:
    length = array_size // SIZE_OF_INT32

    try:
        # Unpack the byte data into a list of int32 values (big-endian)
        values = struct.unpack(f">{length}i", data[:array_size])
        return list(values)
    except struct.error as exc:
        raise ValueError("Failed to read binary data") from exc


def parse_int32(data: bytes) -> int:
    try:
        # Unpack a single big-endian int32 value from the data
        (value,) = struct.unpack(">i", data[:4])
        return value
    except struct.error as exc:
        raise ValueError("Failed to read binary data") from exc


def uint16_array(data: bytes, array_size: int) -> list[int]:
    length = array_size // SIZE_OF_UINT16

    try:
        # Unpack the byte data into a list of uint16 values (big-endian)
        values = struct.unpack(f">{length}H", data[:array_size])
        return list(values)
    except struct.error as exc:
        raise ValueError("Failed to read binary data") from exc


def parse_string_array(data: bytes) -> list[str]:
    # Decode the bytes to a string and strip trailing null characters
    decoded_str = data.rstrip(b"\x00").decode("utf-8")

    # Split the string by null terminators
    return decoded_str.split("\x00")


def get_nevra(index_entries: list[IndexEntry]) -> PackageInfo:
    package_info = PackageInfo()
    parsing_map: dict[
        int, Callable[[IndexEntry, PackageInfo], PackageInfo]
    ] = {
        RPMTAG_DIRINDEXES: _parse_rpmtag_dirindex,
        RPMTAG_DIRNAMES: _parse_rpmtag_dirnames,
        RPMTAG_BASENAMES: _parse_rpmtag_basenames,
        RPMTAG_MODULARITYLABEL: _parse_rpmtag_modularitylabel,
        RPMTAG_NAME: _parse_rpmtag_name,
        RPMTAG_EPOCH: _parse_rpmtag_epoch,
        RPMTAG_VERSION: _parse_rpmtag_version,
        RPMTAG_RELEASE: _parse_rpmtag_release,
        RPMTAG_ARCH: _parse_rpmtag_arch,
        RPMTAG_SOURCERPM: _parse_rpmtag_sourcerpm,
        RPMTAG_PROVIDENAME: _parse_rpmtag_providename,
        RPMTAG_REQUIRENAME: _parse_rpmtag_requirename,
        RPMTAG_LICENSE: _parse_rpmtag_license,
        RPMTAG_VENDOR: _parse_rpmtag_vendor,
        RPMTAG_SIZE: _parse_rpmtag_size,
        RPMTAG_FILEDIGESTALGO: _parse_rpmtag_filedigestalgo,
        RPMTAG_FILESIZES: _parse_rpmtag_filesizes,
        RPMTAG_FILEDIGESTS: _parse_rpmtag_filedigests,
        RPMTAG_FILEMODES: _parse_rpmtag_filemodes,
        RPMTAG_FILEFLAGS: _parse_rpmtag_fileflags,
        RPMTAG_FILEUSERNAME: _parse_rpmtag_fileusername,
        RPMTAG_FILEGROUPNAME: _parse_rpmtag_filegroupname,
        RPMTAG_SUMMARY: _parse_rpmtag_summary,
        RPMTAG_INSTALLTIME: _parse_rpmtag_installtime,
        RPMTAG_SIGMD5: _parse_rpmtag_sigmd5,
        RPMTAG_PGP: _parse_rpmtag_pgpsig,
    }
    for entry in index_entries:
        if entry.info.tag not in parsing_map:
            continue
        parse_function = parsing_map[entry.info.tag]
        package_info = parse_function(entry, package_info)
    return package_info


def _parse_rpmtag_dirindex(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_INT32_TYPE:
        raise ValueError("Invalid tag dir indexes")
    try:
        package_info.dir_indexes = parse_int32_array(entry.data, entry.length)
    except ValueError as exc:
        raise ValueError("unable to read dir indexes") from exc

    return package_info


def _parse_rpmtag_dirnames(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_ARRAY_TYPE:
        raise ValueError("Invalid tag dir names")
    try:
        package_info.dir_names = parse_string_array(entry.data)
    except ValueError as exc:
        raise ValueError("unable to read dir names") from exc

    return package_info


def _parse_rpmtag_basenames(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_ARRAY_TYPE:
        raise ValueError("Invalid tag base names")
    try:
        package_info.base_names = parse_string_array(entry.data)
    except ValueError as exc:
        raise ValueError("unable to read base names") from exc
    return package_info


def _parse_rpmtag_modularitylabel(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_TYPE:
        raise ValueError("Invalid tag modularity label")
    package_info.modularity_label = entry.data.rstrip(b"\x00").decode("utf-8")
    return package_info


def _parse_rpmtag_name(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_TYPE:
        raise ValueError("Invalid tag name")
    package_info.name = entry.data.rstrip(b"\x00").decode("utf-8")
    return package_info


def _parse_rpmtag_epoch(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_INT32_TYPE:
        raise ValueError("Invalid tag epoch")
    if not entry.data:
        return package_info

    try:
        package_info.epoch = parse_int32(entry.data)
    except ValueError as exc:
        raise ValueError("unable to read epoch") from exc
    return package_info


def _parse_rpmtag_version(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_TYPE:
        raise ValueError("Invalid tag version")
    package_info.version = entry.data.rstrip(b"\x00").decode("utf-8")
    return package_info


def _parse_rpmtag_release(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_TYPE:
        raise ValueError("Invalid tag release")
    package_info.release = entry.data.rstrip(b"\x00").decode("utf-8")
    return package_info


def _parse_rpmtag_arch(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_TYPE:
        raise ValueError("Invalid tag arch")
    package_info.arch = entry.data.rstrip(b"\x00").decode("utf-8")
    return package_info


def _parse_rpmtag_sourcerpm(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_TYPE:
        raise ValueError("Invalid tag source rpm")
    package_info.source_rpm = entry.data.rstrip(b"\x00").decode("utf-8")

    if package_info.source_rpm == "(none)":
        package_info.source_rpm = ""
    return package_info


def _parse_rpmtag_providename(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_ARRAY_TYPE:
        raise ValueError("Invalid tag provide name")
    try:
        package_info.provides = parse_string_array(entry.data)
    except ValueError as exc:
        raise ValueError("unable to read provide name") from exc

    return package_info


def _parse_rpmtag_requirename(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_ARRAY_TYPE:
        raise ValueError("Invalid tag require name")
    try:
        package_info.requires = parse_string_array(entry.data)
    except ValueError as exc:
        raise ValueError("unable to read require name") from exc
    return package_info


def _parse_rpmtag_license(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_TYPE:
        raise ValueError("Invalid tag license")

    package_info.license = entry.data.rstrip(b"\x00").decode("utf-8")
    if package_info.license == "(none)":
        package_info.license = ""

    return package_info


def _parse_rpmtag_vendor(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_TYPE:
        raise ValueError("Invalid tag vendor")
    package_info.vendor = entry.data.rstrip(b"\x00").decode("utf-8")
    if package_info.vendor == "(none)":
        package_info.vendor = ""
    return package_info


def _parse_rpmtag_size(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_INT32_TYPE:
        raise ValueError("Invalid tag size")
    try:
        size = parse_int32(entry.data)
    except ValueError as exc:
        raise ValueError("Invalid tag size") from exc
    package_info.size = size
    return package_info


def _parse_rpmtag_filedigestalgo(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_INT32_TYPE:
        raise ValueError("Invalid tag file digest algo")
    if not entry.data:
        return package_info
    try:
        digest_algorimth = parse_int32(entry.data)
    except ValueError as exc:
        raise ValueError("unable to read file digest algo") from exc
    package_info.digest_algorithm = DigestAlgorithm(algorithm=digest_algorimth)
    return package_info


def _parse_rpmtag_filesizes(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_INT32_TYPE:
        raise ValueError("Invalid tag file sizes")
    if not entry.data:
        return package_info
    try:
        package_info.file_sizes = parse_int32_array(entry.data, entry.length)
    except ValueError as exc:
        raise ValueError("unable to read file sizes") from exc
    return package_info


def _parse_rpmtag_filedigests(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_ARRAY_TYPE:
        raise ValueError("Invalid tag file digests")

    try:
        package_info.file_digests = parse_string_array(entry.data)
    except ValueError as exc:
        raise ValueError("unable to read file digests") from exc

    return package_info


def _parse_rpmtag_filemodes(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_INT16_TYPE:
        raise ValueError("Invalid tag file modes")
    try:
        package_info.file_modes = uint16_array(entry.data, entry.length)
    except ValueError as exc:
        raise ValueError("unable to read file modes") from exc
    return package_info


def _parse_rpmtag_fileflags(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_INT32_TYPE:
        raise ValueError("Invalid tag file flags")
    try:
        package_info.file_flags = parse_int32_array(entry.data, entry.length)
    except ValueError as exc:
        raise ValueError("unable to read file flags") from exc
    return package_info


def _parse_rpmtag_fileusername(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_ARRAY_TYPE:
        raise ValueError("Invalid tag file username")
    try:
        package_info.user_names = parse_string_array(entry.data)
    except ValueError as exc:
        raise ValueError("unable to read fileusername") from exc
    return package_info


def _parse_rpmtag_filegroupname(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_STRING_ARRAY_TYPE:
        raise ValueError("Invalid tag file groupname")
    try:
        package_info.group_names = parse_string_array(entry.data)
    except ValueError as exc:
        raise ValueError("unable to read file groupname") from exc
    return package_info


def _parse_rpmtag_summary(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type not in (RPM_I18NSTRING_TYPE, RPM_STRING_TYPE):
        raise ValueError("Invalid tag summary")
    package_info.summary = entry.data.split(b"\x00")[0].decode("utf-8")

    return package_info


def _parse_rpmtag_installtime(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    if entry.info.type != RPM_INT32_TYPE:
        raise ValueError("Invalid tag install time")

    try:
        package_info.install_time = parse_int32(entry.data)
    except ValueError as exc:
        raise ValueError("unable to read install time") from exc
    return package_info


def _parse_rpmtag_sigmd5(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    package_info.sig_md5 = entry.data.hex()
    return package_info


def _parse_rpmtag_pgpsig(
    entry: IndexEntry, package_info: PackageInfo
) -> PackageInfo:
    pub_key_look = {
        0x01: "RSA",
    }
    has_look_up = {
        0x02: "SHA1",
        0x08: "SHA256",
    }

    if entry.info.type != RPM_BIN_TYPE:
        raise ValueError("Invalid tag pgp sig")
    reader = io.BytesIO(entry.data)
    _, signature_type, version = struct.unpack(">BBB", reader.read(3))

    pub_key_algo = ""
    hash_algo = ""
    package_date = ""
    key_id = b""
    sig: TextSig | PgpSig | Pgp4Sig | None = None
    if signature_type == 0x01:
        if version == 0x1C:
            sig = TextSig(reader.read(struct.calcsize(">2x BB 4x i 4x 8s")))
            pub_key_algo = pub_key_look.get(sig.pub_key_algo, "Unknown")
            hash_algo = has_look_up.get(sig.hash_algo, "Unknown")
            package_date = time.strftime(
                "%a %b %d %H:%M:%S %Y", time.gmtime(sig.date)
            )
            key_id = sig.key_id
        else:
            sig = PgpSig(reader.read(struct.calcsize(">3x i 8s BB")))
            pub_key_algo = pub_key_look.get(sig.pub_key_algo, "Unknown")
            hash_algo = has_look_up.get(sig.hash_algo, "Unknown")
            package_date = time.strftime(
                "%a %b %d %H:%M:%S %Y", time.gmtime(sig.date)
            )
            key_id = sig.key_id
    elif signature_type == 0x02:
        if version == 0x33:
            sig = Pgp4Sig(reader.read(struct.calcsize(">2x BB 17x 8s 2x i")))
            pub_key_algo = pub_key_look.get(sig.pub_key_algo, "Unknown")
            hash_algo = has_look_up.get(sig.hash_algo, "Unknown")
            package_date = time.strftime(
                "%a %b %d %H:%M:%S %Y", time.gmtime(sig.date)
            )
            key_id = sig.key_id
        else:
            sig = PgpSig(reader.read(struct.calcsize(">3x i 8s BB")))
            pub_key_algo = pub_key_look.get(sig.pub_key_algo, "Unknown")
            hash_algo = has_look_up.get(sig.hash_algo, "Unknown")
            package_date = time.strftime(
                "%a %b %d %H:%M:%S %Y", time.gmtime(sig.date)
            )
            key_id = sig.key_id

    package_info.pgp = (
        f"{pub_key_algo}/{hash_algo}, {package_date}, Key ID {key_id.hex()}"
    )

    return package_info
