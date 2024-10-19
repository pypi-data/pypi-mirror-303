from fluid_sbom.config.logger import (
    LOGGER,
)
from fluid_sbom.pkg.cataloger.redhat.rpmdb.errors import (
    InvalidDBFormat,
)
from fluid_sbom.pkg.cataloger.redhat.rpmdb.rpmdb_interface import (
    RpmDBInterface,
)
import sqlite3
from typing import (
    Generator,
)


class Sqlite(RpmDBInterface):  # pylint: disable=too-few-public-methods
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection
        super().__init__()

    def read(
        self,
    ) -> Generator[bytes, None, None]:
        cursor = self.connection.cursor()
        try:
            blobs = cursor.execute("SELECT blob FROM Packages;").fetchall()
        except sqlite3.DatabaseError:
            return

        for blob in blobs:
            yield blob[0]


def open_sqlite(file_path: str) -> RpmDBInterface:
    connection = sqlite3.connect(file_path)
    cursor = connection.cursor()
    try:
        cursor.execute("PRAGMA schema_version;")
    except sqlite3.DatabaseError as exc:
        LOGGER.warning(
            "Invalid SQLite database file",
            extra={
                "extra": {
                    "location": file_path,
                }
            },
        )
        raise InvalidDBFormat from exc
    return Sqlite(connection)
