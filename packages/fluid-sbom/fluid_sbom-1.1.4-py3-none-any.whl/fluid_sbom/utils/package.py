from fluid_sbom.internal.package_information.javascript import (
    NPMPackageLicense,
)


def strip_version_specifier(item: str) -> str:
    # Define the characters that indicate the start of a version specifier
    specifiers = "[(<>="

    # Find the index of the first occurrence of any specifier character
    index = next(
        (i for i, char in enumerate(item) if char in specifiers), None
    )

    # If no specifier character is found, return the original string
    if index is None:
        return item.strip()

    # Return the substring up to the first specifier character, stripped of
    # leading/trailing whitespace
    return item[:index].strip()


def handle_licenses(
    licenses: str | list[str | dict[str, str]] | NPMPackageLicense,
) -> list[str]:
    if isinstance(licenses, dict):
        return [licenses["type"]] if "type" in licenses else []
    if isinstance(licenses, list):
        licenses_list = []
        for license_item in licenses:
            if isinstance(license_item, str):
                licenses_list.append(license_item)
            if isinstance(license_item, dict) and license_item["type"]:
                licenses_list.append(license_item["type"])
        return licenses_list
    return [licenses]
