from uv_version.collectors.base import BaseCollector


class GitCollector(BaseCollector):
    def __init__(self) -> None:
        super().__init__()
