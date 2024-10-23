from pathlib import Path

import tomlkit
from packaging.version import Version

from uv_version.setters.base import BaseSetter


class PyprojectSetter(BaseSetter):
    pyproject_file: Path

    def __init__(self, pyproject_file: Path) -> None:
        super().__init__()
        self.pyproject_file = pyproject_file

    def set(self, version: Version):
        # Открываем файл и читаем его содержимое
        with self.pyproject_file.open('r', encoding='utf-8') as toml_file:
            toml_data = tomlkit.parse(toml_file.read())

        if 'project' not in toml_data:
            toml_data['project'] = tomlkit.table()

        toml_data['project']['version'] = str(version)  # type: ignore

        # Перезаписываем файл с обновленными данными
        with self.pyproject_file.open('w', encoding='utf-8') as toml_file:
            toml_file.write(tomlkit.dumps(toml_data))
