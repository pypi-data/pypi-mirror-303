from packaging.version import InvalidVersion, Version

from uv_version.collectors.base import BaseCollector
from uv_version.increment.emums import IncrementEnum
from uv_version.increment.processing import increment_version
from uv_version.setters.base import BaseSetter


class UvVersionManager(object):
    setters: list[BaseSetter]
    collectors: list[BaseCollector]
    versions: list[Version]

    def __init__(self) -> None:
        self.setters = []
        self.collectors = []
        self.versions = []

    def add_setter(self, setter: BaseSetter):
        assert isinstance(setter, BaseSetter)

        self.setters.append(setter)

    def add_collector(self, collector: BaseCollector):
        assert isinstance(collector, BaseCollector)

        self.collectors.append(collector)

    def collect(self):
        for collector in self.collectors:
            d = collector.collect()

            if d is None:
                continue

            try:
                version = Version(d)

            except InvalidVersion:
                continue

            self.versions.append(version)

    def get_current_version(self) -> Version | None:
        if self.versions:
            return max(self.versions)

        return None

    def increment(self, increment_part: IncrementEnum):
        current_version = self.get_current_version()

        if current_version is None:
            return None

        new_version = increment_version(current_version, increment_part)

        self.versions.append(new_version)

    def set(self):
        current_version = self.get_current_version()

        if current_version is None:
            return None

        for setter in self.setters:
            setter.set(current_version)
