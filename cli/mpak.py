import requests
from typer import Typer
from tools.install import *
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = Typer()


@app.command("install")
def install_package(pkg_name:str) -> None:
    '''
    Downloads a package in your project
    '''
    resp = requests.get(f'http://localhost:8000/repos/search/{pkg_name}')
    if resp.status_code == 200:
        return install(str(resp.content.decode('utf-8')))
    rich_error(f"Package {pkg_name} not found")

@app.command("uninstall")
def uninstall_package(pkg_name:str) -> None:
    '''
    Uninstalls a package in your project
    '''
    uninstall(pkg_name)

@app.command("init")
def init_project() -> None:
    '''
    Initializes your project
    '''
    init()

if __name__ == "__main__":
    import os
    import sys

    # Obtém o diretório atual do arquivo mpak.py
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Adiciona o diretório ao caminho do sistema
    sys.path.append(current_dir)
    app()    