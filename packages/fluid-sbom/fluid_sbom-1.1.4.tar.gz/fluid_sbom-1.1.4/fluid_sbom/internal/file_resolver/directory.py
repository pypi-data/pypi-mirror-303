from fluid_sbom.file.coordinates import (
    Coordinates,
)
from fluid_sbom.file.location import (
    Location,
)
from fluid_sbom.file.metadata import (
    Metadata,
)
from fluid_sbom.file.resolver import (
    Resolver,
)
from fluid_sbom.file.type import (
    Type,
)
import glob
import magic
import os
from pydantic import (
    BaseModel,
)
from typing import (
    Callable,
    Generator,
    TextIO,
)


class Directory(Resolver, BaseModel):
    root: str

    def __post__init__(self, root: str) -> None:
        self.root = os.path.realpath(os.path.abspath(root))

    def has_path(self, path: str) -> bool:
        path = os.path.join(self.root, path.lstrip("/"))
        return os.path.exists(path)

    def files_by_path(self, *paths: str) -> list[Location]:
        locations: list[Location] = []
        for path in paths:
            relative_path = path.replace(self.root, "").lstrip("/")
            full_path = os.path.join(self.root, relative_path)
            if os.path.exists(full_path):
                locations.append(
                    Location(
                        coordinates=Coordinates(
                            real_path=full_path, file_system_id=""
                        ),
                        access_path=relative_path,
                        annotations={},
                    )
                )
        return locations

    def files_by_glob(self, *patters: str) -> list[Location]:
        result = []
        for pattern in patters:
            for item in glob.glob(pattern, root_dir=self.root):
                result.append(
                    Location(
                        coordinates=Coordinates(
                            real_path=os.path.join(self.root, item),
                            file_system_id="",
                        ),
                        access_path=item,
                        annotations={},
                    )
                )

        return result

    def files_by_mime_type(self, mime_type: str) -> list[Location]:
        matching_files = []
        mime_detector = magic.Magic(mime=True)

        for dirpath, _, filenames in os.walk(self.root):
            for filename in filenames:
                relative_path = (
                    os.path.join(dirpath, filename)
                    .replace(self.root, "")
                    .lstrip("/")
                )
                result_mime_type = mime_detector.from_file(relative_path)
                if mime_type == result_mime_type:
                    matching_files.append(
                        Location(
                            coordinates=Coordinates(
                                real_path=os.path.join(
                                    self.root, relative_path
                                ),
                                file_system_id="",
                            ),
                            access_path=relative_path,
                            annotations={},
                        )
                    )

        return matching_files

    def file_contents_by_location(
        self,
        location: Location,
        *,
        function_reader: Callable[..., TextIO] | None = None,
        mode: str | None = None,
    ) -> TextIO | None:
        if (
            location.coordinates
            and location.coordinates.real_path is not None
            and os.path.exists(location.coordinates.real_path)
        ):
            return (function_reader or open)(  # type: ignore
                location.coordinates.real_path,
                encoding="utf-8",
                mode=mode or "r",
            )

        return None

    def file_metadata_by_location(self, location: Location) -> Metadata | None:
        link_destination = None
        if not location.access_path:
            return None

        stats = os.stat(location.access_path, follow_symlinks=False)

        if os.path.islink(location.access_path):
            file_type = Type.TYPE_SYM_LINK
            link_destination = os.readlink(location.access_path)
        elif os.path.isdir(location.access_path):
            file_type = Type.TYPE_DIRECTORY
        elif os.path.isfile(location.access_path):
            file_type = Type.TYPE_REGULAR

        mime_type = magic.Magic(mime=True).from_file(location.access_path)

        return Metadata(
            path=location.access_path,
            link_destination=link_destination or "",
            user_id=stats.st_uid,
            group_id=stats.st_gid,
            type=file_type,
            mime_type=mime_type,
        )

    def relative_file_path(self, _: Location, _path: str) -> Location:
        return Location(
            coordinates=Coordinates(
                real_path=_path, file_system_id="", line=None
            ),
            access_path=_path.replace(self.root, "").lstrip("/"),
        )

    def walk_file(self) -> Generator[str, None, None]:
        exclusions = {
            "node_modules",
            "dist",
            "__pycache__",
        }
        for dirpath, dirnames, filenames in os.walk(self.root):
            dirnames[:] = [dir for dir in dirnames if dir not in exclusions]

            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                relative_path = full_path.replace(self.root, "").lstrip("/")
                yield relative_path
