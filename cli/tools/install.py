import requests
import json
import subprocess, os
from rich.console import Console
cmd = Console()

def rich_error(message:str) -> None:
    cmd.print(f'[reverse red]ERROR[/reverse red] {message}')

def rich_warning(message:str) -> None:
    cmd.print(f'[reverse yellow]WARNING[/reverse yellow] {message}')


def rich_info(message:str) -> None:
    cmd.print(f'[reverse blue]INFO[/reverse blue] {message}')

def rich_sucess(message:str) -> None:
    cmd.print(f'[reverse green]SUCESS[/reverse green] {message}')

def install(repo_url:str) -> int:
    pkg_name = repo_url.split("/")[-1]
    dirs = os.listdir()
    if "mojo_modules" not in dirs:
        rich_error("""Your project is not initialized
        Please run `mpak init` to initialize the project""")
        return 1
    try:
        rich_info(f"Found package {pkg_name}")
        rich_info("Trying to install...")
        subprocess.check_call(["cd mojo_modules", "&&", "git", "clone", repo_url] )
        rich_sucess(f"Package {pkg_name} installed")
        return 0 
    except:
        rich_error(f"Failed to install package {pkg_name}")
        return 1

def uninstall(pkg_name:str) -> int:
    dirs = os.listdir()
    if "mojo_modules" not in dirs:
        rich_error("""Your project is not initialized
        Please run `mpak init` to initialize the project""")
        return 1
    try:
        rich_info(f"Found package {pkg_name}")
        rich_info("Trying to uninstall...")
        subprocess.check_call(["cd mojo_modules", "&&", "rm", "-rf", pkg_name] )
        rich_sucess(f"Package {pkg_name} uninstalled")
        return 0 
    except:
        rich_error(f"Failed to uninstall package {pkg_name}")
        return 1

def init():
    # Create the "mojo_modules" directory
    os.mkdir("mojo_modules")
    return