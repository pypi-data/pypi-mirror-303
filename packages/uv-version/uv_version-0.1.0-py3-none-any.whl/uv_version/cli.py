from pathlib import Path

import typer

import uv_version
from uv_version.increment.emums import IncrementEnum
from uv_version.manager import UvVersionManager

app = typer.Typer(help='uv-version CLI')


uv_version_manager = UvVersionManager()


def version_callback(value: bool):
    if value:
        print(f'Version of uv-version is {uv_version.__version__}')
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def callback(  # noqa: C901
    ctx: typer.Context,
    #
    version: bool = typer.Option(
        False,
        '--version',
        callback=version_callback,
        is_eager=True,
    ),
    # Setters
    to_pyproject: bool = typer.Option(
        False,
        '--to-pyproject',
        help='Установить новую версию в pyproject.toml.',
        metavar='Default',
        rich_help_panel='uv-version Setters Options',
    ),
    to_print: bool = typer.Option(
        False,
        '--to-print',
        help='Вывести новую версию в консоль.',
        rich_help_panel='uv-version Setters Options',
    ),
    # Collectors
    from_pyproject: bool = typer.Option(
        False,
        '--from-pyproject',
        help='Версия определяется на значения pyproject.toml project.version',
        metavar='Default',
        rich_help_panel='uv-version Collectors Options',
    ),
    from_git: bool = typer.Option(
        False,
        '--from-git',
        help='Версия определяется на основе состояния git',
        rich_help_panel='uv-version Collectors Options',
    ),
    from_stdin: bool = typer.Option(
        False,
        '--from-stdin',
        help='Версия ожидается последним аргументом вызова или из stdin',
        rich_help_panel='uv-version Collectors Options',
    ),
    from_env: bool = typer.Option(
        False,
        '--from-env',
        help='Версия ожидается в переменной окружения PACKAGE_VERSION',
        rich_help_panel='uv-version Collectors Options',
    ),
):
    # Setters

    if not any((to_pyproject, to_print)):
        to_pyproject = True

    if to_pyproject:
        from uv_version.setters.pyproject_setter import PyprojectSetter

        pyproject_file = Path('pyproject.toml').absolute()

        if not pyproject_file.exists():
            print(f'File {pyproject_file} not found')
            raise typer.Exit(1)

        uv_version_manager.add_setter(PyprojectSetter(pyproject_file))

    if to_print:
        from uv_version.setters.print_setter import PrintSetter

        uv_version_manager.add_setter(PrintSetter())

    if not any((
        from_pyproject,
        from_git,
        from_stdin,
        from_env,
    )):
        from_pyproject = True

    if from_pyproject:
        from uv_version.collectors.pyproject_collector import PyprojectCollector

        pyproject_file = Path('pyproject.toml').absolute()

        if not pyproject_file.exists():
            print(f'File {pyproject_file} not found')
            raise typer.Exit(1)

        uv_version_manager.add_collector(PyprojectCollector(pyproject_file))

    if from_git:
        from uv_version.collectors.git_collector import GitCollector

        uv_version_manager.add_collector(GitCollector())

    if from_stdin:
        from uv_version.collectors.stdin_collector import StdinCollector

        uv_version_manager.add_collector(StdinCollector())

    if from_env:
        from uv_version.collectors.env_collector import EnvCollector

        uv_version_manager.add_collector(EnvCollector())

    if ctx.invoked_subcommand is None:
        uv_version_manager.collect()
        uv_version_manager.set()


@app.command('increment')
def increment_command(
    # Increment
    increment: IncrementEnum = typer.Argument(
        IncrementEnum.patch,
        show_default=False,
        help='Увеличивает выбранную часть версии на 1',
        rich_help_panel='uv-version Increment Options',
    ),
):
    uv_version_manager.collect()
    uv_version_manager.increment(increment)
    uv_version_manager.set()


def cli():
    app()
