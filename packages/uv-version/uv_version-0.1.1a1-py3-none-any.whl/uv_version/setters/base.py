from packaging.version import Version


class BaseSetter(object):
    """Базовый класс для обьектов для сохранения версии."""

    def set(self, version: Version):
        pass
