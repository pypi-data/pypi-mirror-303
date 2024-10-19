from fluid_sbom.internal.cache import (
    dual_cache,
)
import requests
from typing import (
    Any,
)


@dual_cache
def get_pypi_package(
    package_name: str, version: str | None = None
) -> dict[str, Any] | None:
    url = (
        f"https://pypi.org/pypi/{package_name}"
        f"{'/' +version if version else ''}/json"
    )
    response = requests.get(url, timeout=20)
    if response.status_code == 200:
        package_info = response.json()
        return package_info

    return None
