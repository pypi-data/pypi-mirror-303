import importlib
import importlib.util as import_utils
import os
from pathlib import Path
from typing import Optional

import typer

from fastapi_toolkit.generate import CodeGenerator
from fastapi_toolkit.apis_generate import ApiGenerator
from fastapi_toolkit.configer import Configer

app = typer.Typer()

tk_root = Path('.fastapi-toolkit')

configer = Configer()


def add_path_to_gitignore(path: Path):
    gitignore_path = Path('.gitignore')
    if not gitignore_path.exists():
        with open(gitignore_path, 'w') as f:
            f.write(f'{path}\n')
    else:
        with open(gitignore_path, 'r') as f:
            lines = f.readlines()
        if path.name not in lines:
            with open(gitignore_path, 'a') as f:
                f.write(f'{path}\n')


def import_module(module_name, module_path):
    spec = import_utils.spec_from_file_location(module_name, module_path)
    module = import_utils.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@app.command('a')
def aaa():
    print(123)


@app.command('i')
@app.command('init')
def init():
    os.mkdir(tk_root)
    add_path_to_gitignore(tk_root)


@app.command('g')
@app.command('generate')
def generate(metadata_path: Optional[Path] = None, root_path: Optional[Path] = None,
             force: bool = False,
             table: bool = True, router: bool = True, mock: bool = True, auth: str = ""):
    if metadata_path is None:
        metadata_path = Path(configer['metadata_path'] or 'metadata')
    if root_path is None:
        root_path = Path(configer['root_path'] or 'inner_code')
    if not root_path.is_dir():
        typer.confirm(f'root_path: {root_path} is not a dir, do you want to create it?', abort=True)
        root_path.mkdir(parents=True)
    module_name = "models"
    _ = import_module(module_name, metadata_path.joinpath(f'{module_name}.py'))
    generator = CodeGenerator(root_path)
    generator.force_rewrite = force
    generator.generate(table, router, mock, auth)


@app.command('mock')
@app.command('m')
def mock(root_path: Optional[Path] = None):
    if root_path is None:
        root_path = Path(configer['root_path'] or 'inner_code')
    main = importlib.import_module(str(root_path).replace('\\', '.') + '.mock').main
    main()


db_app = typer.Typer()


def get_dev_db(root_path: Optional[Path] = None):
    if root_path is None:
        root_path = Path(configer['root_path'] or 'inner_code')
    module_path = root_path.joinpath('dev').joinpath(f'db.py')
    return import_module('db', module_path)


@db_app.command('init')
@db_app.command('i')
def db_init(root_path: Optional[Path] = None):
    if root_path is None:
        root_path = Path(configer['root_path'] or 'inner_code')
    init = get_dev_db(root_path).init
    init()


@db_app.command('migrate')
@db_app.command('m')
def db_migrate(root_path: Optional[Path] = None, msg: str = None):
    if root_path is None:
        root_path = Path(configer['root_path'] or 'inner_code')
    migrate = get_dev_db(root_path).migrate
    migrate(msg)


@db_app.command('upgrade')
@db_app.command('u')
def db_upgrade(root_path: Optional[Path] = None):
    if root_path is None:
        root_path = Path(configer['root_path'] or 'inner_code')
    upgrade = get_dev_db(root_path).upgrade
    upgrade()


app.add_typer(db_app, name="db")
