import requests
import argparse
from datetime import datetime
from packaging.version import parse


def get_package_versions(package_name: str) -> list:
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        versions = sorted(data['releases'].keys(), key=parse)
        return versions
    else:
        raise ValueError(f"Package '{package_name}' not found on PyPI.")


def generate_new_version(versions: list) -> str:
    now = datetime.now()
    first_day_of_month = now.replace(day=1)
    week_number_in_month = (now.day + first_day_of_month.weekday()) // 7 + 1

    version_patterns = [
        f"{now.year}.{now.month}",
        f"{now.year}.{now.month}.{week_number_in_month}",
        f"{now.year}.{now.month}.{now.day}",
        f"{now.year}.{now.month}.{now.day}.{now.hour}",
        f"{now.year}.{now.month}.{now.day}.{now.hour}.{now.minute}",
        f"{now.year}.{now.month}.{now.day}.{now.hour}.{now.minute}.{now.second}"
    ]

    for pattern in version_patterns:
        if pattern not in versions:
            return pattern

    return version_patterns[-1]


def main():
    parser = argparse.ArgumentParser(description="Version Hawk: Generate new version tags.")
    parser.add_argument("package", help="The name of the package on PyPI.")
    parser.add_argument("--versions", action="store_true", help="List all versions of the package.")

    args = parser.parse_args()
    package_name = args.package

    if args.versions:
        try:
            versions = get_package_versions(package_name)
            for version in versions:
                print(version)
        except ValueError as e:
            print(e)
    else:
        try:
            versions = get_package_versions(package_name)
            new_version = generate_new_version(versions)
            print(new_version)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()