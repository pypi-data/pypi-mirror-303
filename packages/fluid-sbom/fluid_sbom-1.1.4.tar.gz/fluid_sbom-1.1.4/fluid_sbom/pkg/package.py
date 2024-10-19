from datetime import (
    datetime,
)
from fluid_sbom.file.location import (
    Location,
)
from fluid_sbom.pkg.language import (
    Language,
)
from fluid_sbom.pkg.type import (
    PackageType,
)
from fluid_sbom.utils.file import (
    Digest,
)
import hashlib
import json
from pydantic import (
    BaseModel,
    Field,
    field_validator,
)


class Advisory(BaseModel):
    cpes: list[str]
    description: str | None = Field(min_length=1)
    epss: float
    id: str = Field(min_length=1)
    namespace: str = Field(min_length=1)
    percentile: float
    severity: str = Field(min_length=1)
    urls: list[str]
    version_constraint: str | None = Field()

    @field_validator("cpes")
    @classmethod
    def check_cpes_min_length(cls, value: list[str]) -> list[str]:
        for cpe in value:
            if len(cpe) < 1:
                raise ValueError(
                    "Each cpe string must be at least 1 character long."
                )
        return value

    @field_validator("urls")
    @classmethod
    def check_urls_min_length(cls, value: list[str]) -> list[str]:
        for url in value:
            if len(url) < 1:
                raise ValueError(
                    "Each url string must be at least 1 character long."
                )
        return value

    def get_info_count(self) -> int:
        info_count = 0
        for attr in [
            self.cpes,
            self.description,
            self.urls,
            self.version_constraint,
        ]:
            if attr:
                info_count += 1
        return info_count

    def __repr__(self) -> str:
        return (
            f"Advisory(id={self.id}, "
            f"namespace={self.namespace}, severity={self.severity})"
        )


class Artifact(BaseModel):
    url: str = Field(min_length=1)
    integrity: Digest | None = None


class HealthMetadata(BaseModel):
    latest_version: str | None = Field(default=None, min_length=1)
    latest_version_created_at: str | datetime | None = None
    artifact: Artifact | None = None
    authors: str | None = Field(default=None, min_length=1)

    @field_validator("latest_version_created_at", mode="before")
    @classmethod
    def validate_latest_version_created_at(
        cls, value: str | datetime | None
    ) -> str | datetime | None:
        if isinstance(value, str) and len(value) < 1:
            raise ValueError(
                "latest_version_created_at must be at least 1 character long "
                "when it is a string."
            )
        return value


class Package(BaseModel):
    name: str = Field(min_length=1)
    version: str = Field(min_length=1)
    language: Language
    licenses: list[str]
    locations: list[Location]
    type: PackageType
    advisories: list[Advisory] | None = None
    dependencies: list["Package"] | None = None
    found_by: str | None = Field(default=None, min_length=1)
    health_metadata: HealthMetadata | None = None
    is_dev: bool = False
    metadata: object | None = None
    p_url: str = Field(min_length=1)

    @property
    def id_(self) -> str:
        return self.id_by_hash()

    def id_by_hash(self) -> str:
        try:
            obj_data = {
                "name": self.name,
                "version": self.version,
                "language": self.language.value,
                "type": self.type.value,
                "p_url": self.p_url,
            }
            obj_str = json.dumps(obj_data, sort_keys=True)
            hash_value = hashlib.sha256(obj_str.encode()).hexdigest()
            return hash_value
        except Exception as exc:  # pylint:disable=broad-exception-caught
            return f"Could not build ID for object={self}: {exc}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Package):
            return self.id_ == other.id_
        return False

    def __hash__(self) -> int:
        return hash(self.id_)

    @field_validator("licenses")
    @classmethod
    def check_licenses_min_length(cls, value: list[str]) -> list[str]:
        for license_str in value:
            if len(license_str) < 1:
                raise ValueError(
                    "Each license string must be at least 1 character long."
                )
        return value
