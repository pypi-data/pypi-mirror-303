from fluid_sbom.file.type import (
    Type,
)
from pydantic import (
    BaseModel,
)


class Metadata(BaseModel):
    path: str
    link_destination: str
    user_id: int
    group_id: int
    type: Type
    mime_type: str
