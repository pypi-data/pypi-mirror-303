from fluid_sbom.file.location import (
    Location,
)
from io import (
    TextIOWrapper,
)
from pydantic import (
    BaseModel,
    ConfigDict,
)
from typing import (
    TextIO,
)


class LocationReadCloser(BaseModel):
    location: Location
    read_closer: TextIO | TextIOWrapper
    model_config = ConfigDict(arbitrary_types_allowed=True)
