from packaging.version import Version

from uv_version.increment.emums import IncrementEnum


def increment_version(version: Version, part: IncrementEnum):
    """[![Iam cringe](https://markdown-videos-api.jorgenkh.no/youtube/Rmp6LCQ67JY)](https://youtu.be/Rmp6LCQ67JY)."""
    major, minor, micro = version.major, version.minor, version.micro

    prerelease = None

    if version.pre is not None:
        _, prerelease = version.pre

    if part == IncrementEnum.major:
        major += 1
        minor = 0
        micro = 0
        prerelease = None

    elif part == IncrementEnum.minor:
        minor += 1
        micro = 0
        prerelease = None

    elif part == IncrementEnum.patch:
        micro += 1
        prerelease = None

    elif part == IncrementEnum.prerelease:
        if prerelease is None:
            prerelease = 0
            micro += 1

        prerelease += 1

    new_version_str = f'{major}.{minor}.{micro}'
    if prerelease is not None:
        new_version_str += f'a{prerelease}'

    return Version(new_version_str)
