from fluid_sbom.file.coordinates import (
    Coordinates,
)
from pydantic import (
    BaseModel,
)


class LocationMetadata(BaseModel):
    annotations: dict[str, str]

    def merge(self, other: "LocationMetadata") -> "LocationMetadata":
        return LocationMetadata(
            annotations={**self.annotations, **other.annotations}
        )


class LocationData(BaseModel):
    coordinates: Coordinates
    access_path: str

    def __hash__(self) -> int:
        return hash(self.access_path) + hash(self.coordinates.file_system_id)


class Location(BaseModel):
    coordinates: Coordinates | None = None
    access_path: str | None = None
    annotations: dict[str, str] | None = None

    def with_annotation(self, key: str, value: str) -> "Location":
        if not self.annotations:
            self.annotations = {}
        self.annotations[key] = value
        return self

    def path(self) -> str:
        return (
            self.access_path
            or (self.coordinates.real_path if self.coordinates else "")
            or ""
        )


def new_location_from_image(
    access_path: str | None, layer_id: str, real_path: str | None = None
) -> Location:
    if access_path and not access_path.startswith("/"):
        access_path = f"/{access_path}"
    return Location(
        coordinates=Coordinates(
            real_path=real_path or "", file_system_id=layer_id
        ),
        access_path=access_path,
        annotations={},
    )


def new_location(real_path: str) -> Location:
    return Location(
        coordinates=Coordinates(
            real_path=real_path,
        ),
        access_path=real_path,
        annotations={},
    )
