from fluid_sbom.sources.docker import (
    extract_docker_image,
    ImageMetadata,
)
import os
from pydantic import (
    BaseModel,
)
import re
import tempfile
from typing import (
    Any,
)


class LayerInfo(BaseModel):
    id_: str
    tar_full_path: str
    metadata: dict[str, Any]


class ImageContext(BaseModel):
    id: str
    name: str
    publisher: str | None
    arch: str
    size: str
    full_extraction_dir: str
    layers_dir: str
    manifest: dict[str, Any]
    image_ref: str

    def get_layer_info(self, layer_id: str) -> LayerInfo | None:
        if layer_metadata := next(
            x for x in self.manifest["Layers"] if x["id"] == layer_id
        ):
            return LayerInfo(
                id_=layer_id,
                tar_full_path=os.path.join(self.layers_dir, layer_metadata),
                metadata=layer_metadata,
            )
        return None


def get_context(
    image: ImageMetadata,
    *,
    username: str | None = None,
    password: str | None = None,
    token: str | None = None,
    daemon: bool = False,
) -> ImageContext | None:
    temp_dir = tempfile.mkdtemp()
    layers_dir, manifest = extract_docker_image(
        image,
        temp_dir,
        username=username,
        password=password,
        token=token,
        daemon=daemon,
    )

    return ImageContext(
        id=image.digest,
        name=image.name,
        publisher="",
        arch=image.architecture,
        size=str(sum(x.size for x in image.layersdata)),
        full_extraction_dir=temp_dir,
        layers_dir=layers_dir,
        manifest=manifest,
        image_ref=image.image_ref,
    )


def extract_image_ref_info(user_input: str) -> dict[str, str] | None:
    patter = (
        r"^((?P<publisher>[a-z0-9]+(?:[._-][a-z0-9]+)*)\/)?"
        r"(?P<name>[a-z0-9]+(?:[._-][a-z0-9]+)*)"
        r"(:(?P<tag>[a-zA-Z0-9_.-]+))?"
        r"(?P<digest>@sha256:[a-fA-F0-9]{64})?$"
    )
    if match := re.match(patter, user_input):
        return match.groupdict()
    return None
