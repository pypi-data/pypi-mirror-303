from enum import (
    IntEnum,
)

# ref. https://github.com/rpm-software-management/rpm/blob
# /rpm-4.14.3-release/lib/rpmtag.h#L34
RPMTAG_HEADERIMAGE = 61
RPMTAG_HEADERSIGNATURES = 62
RPMTAG_HEADERIMMUTABLE = 63
HEADER_I18NTABLE = 100
RPMTAG_HEADERI18NTABLE = HEADER_I18NTABLE

# rpmTag_e
# ref. https://github.com/rpm-software-management/rpm
# /blob/rpm-4.14.3-release/lib/rpmtag.h#L34
RPMTAG_SIGMD5 = 261  # x
RPMTAG_NAME = 1000  # s
RPMTAG_VERSION = 1001  # s
RPMTAG_RELEASE = 1002  # s
RPMTAG_EPOCH = 1003  # i
RPMTAG_INSTALLTIME = 1008  # i
RPMTAG_SIZE = 1009  # i
RPMTAG_VENDOR = 1011  # s
RPMTAG_LICENSE = 1014  # s
RPMTAG_ARCH = 1022  # s
RPMTAG_FILESIZES = 1028  # i[] */
RPMTAG_FILEMODES = 1030  # h[] , specifically []uint16
# (ref https://github.com/rpm-software-management/rpm/blob
# /2153fa4ae51a84547129b8ebb3bb396e1737020e/lib/rpmtypes.h#L53 )*/
RPMTAG_FILEDIGESTS = 1035  # s[] */
RPMTAG_FILEFLAGS = 1037  # i[] */
RPMTAG_FILEUSERNAME = 1039  # s[] */
RPMTAG_FILEGROUPNAME = 1040  # s[] */
RPMTAG_SOURCERPM = 1044  # s */
RPMTAG_PROVIDENAME = 1047  # s[] */
RPMTAG_REQUIRENAME = 1049  # s[] */
RPMTAG_DIRINDEXES = 1116  # i[] */
RPMTAG_BASENAMES = 1117  # s[] */
RPMTAG_DIRNAMES = 1118  # s[] */
RPMTAG_FILEDIGESTALGO = 5011  # i  */
RPMTAG_SUMMARY = 1004  # s */
RPMTAG_PGP = 259  # b */

# rpmTag_enhances
# https://github.com/rpm-software-management/rpm/blob
# /rpm-4.16.0-release/lib/rpmtag.h#L375
RPMTAG_MODULARITYLABEL = 5096

# rpmTagType_e
# ref. https://github.com/rpm-software-management/rpm/blob
# /rpm-4.14.3-release/lib/rpmtag.h#L431
RPM_MIN_TYPE = 0
RPM_NULL_TYPE = 0
RPM_CHAR_TYPE = 1
RPM_INT8_TYPE = 2
RPM_INT16_TYPE = 3
RPM_INT32_TYPE = 4
RPM_INT64_TYPE = 5
RPM_STRING_TYPE = 6
RPM_BIN_TYPE = 7
RPM_STRING_ARRAY_TYPE = 8
RPM_I18NSTRING_TYPE = 9
RPM_MAX_TYPE = 9


class RpmTag(IntEnum):
    HEADERIMAGE = 61
    HEADERSIGNATURES = 62
    HEADERIMMUTABLE = 63
    HEADERI18NTABLE = 100
    SIGMD5 = 261
    NAME = 1000
    VERSION = 1001
    RELEASE = 1002
    EPOCH = 1003
    INSTALLTIME = 1008
    SIZE = 1009
    VENDOR = 1011
    LICENSE = 1014
    ARCH = 1022
    FILESIZES = 1028
    FILEMODES = 1030
    FILEDIGESTS = 1035
    FILEFLAGS = 1037
    FILEUSERNAME = 1039
    FILEGROUPNAME = 1040
    SOURCERPM = 1044
    PROVIDENAME = 1047
    REQUIRENAME = 1049
    DIRINDEXES = 1116
    BASENAMES = 1117
    DIRNAMES = 1118
    FILEDIGESTALGO = 5011
    SUMMARY = 1004
    PGP = 259
    MODULARITYLABEL = 5096


class RpmTagType(IntEnum):
    MIN_TYPE = 0
    NULL_TYPE = 0
    CHAR_TYPE = 1
    INT8_TYPE = 2
    INT16_TYPE = 3
    INT32_TYPE = 4
    INT64_TYPE = 5
    STRING_TYPE = 6
    BIN_TYPE = 7
    STRING_ARRAY_TYPE = 8
    I18NSTRING_TYPE = 9
    MAX_TYPE = 9
