from uv_version.collectors.base import BaseCollector


class IncrementCollector(BaseCollector):
    increment_type: str

    def __init__(self, increment_type: str) -> None:
        self.increment_type = increment_type

    def get(self):
        pass
