import requests
from typer import Typer
from tools import *
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

@app.command("upload")
def upload_package() -> None:
    data = prompt(
        [
            {
                'type': 'input',
                'name': 'name',
                'message': 'Your first and last name  ',
                'validate': lambda value: len(value) > 0,
            },
            {
                'type': 'input',
                'name': 'email',
                'message': 'Your email  ',
                'validate': lambda value: (len(value) > 0) and ('@' in value),
            },
            {
                'type': 'input',
                'name': 'repo_name',
                'message': "Package's' name  ",
                'validate': lambda value: len(value) > 0,
            },
            {
                'type': 'input',
                'name': 'description',
                'message': "Package's' description  ",
                'default':'None',
            },
            {
                'type': 'input',
                'name': 'github',
                'message': "Package's' Github repository url  ",
                'validate': lambda value: (len(value) > 0) and ('http' in value),
            },
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Are you sure you want to upload this package?  ',
                'default': False
            }
        ]
    )

    if data['confirm']:
        formatted_data = {
            "repo":{
                "name": data['repo_name'],
                "description": data['description'],
                "github_url": data['github']
            },
            "user":{
                "name": data['name'],
                "email": data['email']
            }
        }
        resp = requests.post(f'http://localhost:8000/repos/create', json=formatted_data)
        if resp.status_code == 200:
            return install(str(resp.content.decode('utf-8')))
        rich_error(f"Package {data['name']} not found")

@app.command('update')
def update_package(package_name:str) -> None:
    username = getpass.getuser()
    dirs = os.listdir(f'/home/{username}')
    if ".modular" not in dirs:
        rich_error(""".modular folder not found, so Mojo was not installed correctly. Please contact Modular's support""")
        return 1
    path = f'/home/{username}/.modular/pkg/packages.modular.com_mojo/lib/mojo/'
    if package_name not in os.listdir(path=path):
        rich_error(f"Package {package_name} not found")
        return 1
    resp = requests.get(f'http://localhost:8000/repos/search/{package_name}')
    if resp.status_code == 200:
        rich_info(f"Reinstalling {package_name} for updates...")
        uninstall(package_name)
        return install(str(resp.content.decode('utf-8')))
    rich_error(f"Package {package_name} not found")



if __name__ == "__main__":
    import os
    import sys

    # Obtém o diretório atual do arquivo mpak.py
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Adiciona o diretório ao caminho do sistema
    sys.path.append(current_dir)
    app()    