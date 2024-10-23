from packaging.version import Version

from uv_version.setters.base import BaseSetter


class PrintSetter(BaseSetter):
    def set(self, version: Version):
        print(version)
