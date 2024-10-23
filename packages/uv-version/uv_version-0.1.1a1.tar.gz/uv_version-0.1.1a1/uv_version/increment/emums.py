from enum import StrEnum


class IncrementEnum(StrEnum):
    major = 'major'
    minor = 'minor'
    patch = 'patch'
    prerelease = 'prerelease'
