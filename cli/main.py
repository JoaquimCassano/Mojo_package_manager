import typer
from tools.install import *
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()


@app.command("install")
def install_package(pkg_name:str) -> None:
    '''
    Downloads a package in your project
    '''
    if requests.get(f'http://localhost:8000/repos/search/{pkg_name}').status_code == 200:
        return install(pkg_name)
    rich_error(f"Package {pkg_name} not found")

@app.command("uninstall")
def uninstall_package(pkg_name:str) -> None:
    '''
    Uninstalls a package in your project
    '''
    uninstall(pkg_name)

if __name__ == "__main__":
    app()    