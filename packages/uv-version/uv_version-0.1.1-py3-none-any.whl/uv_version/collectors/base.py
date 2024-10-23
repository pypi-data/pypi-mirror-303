class BaseCollector(object):
    """Базовый коллектор для определения версии."""

    def collect(self) -> str | None: ...
