from pathlib import Path

import tomlkit

from uv_version.collectors.base import BaseCollector


class PyprojectCollector(BaseCollector):
    pyproject_file: Path

    def __init__(self, pyproject_file: Path) -> None:
        super().__init__()
        self.pyproject_file = pyproject_file

    def collect(self) -> str | None:
        with self.pyproject_file.open('r') as toml_file:
            toml_data = tomlkit.parse(toml_file.read())

        # Возвращаем значение project.name, если оно существует
        return toml_data.get('project', {}).get('version', None)
