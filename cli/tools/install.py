import requests
import json
import subprocess, os
from rich.console import Console
cmd = Console()

def rich_error(message:str) -> None:
    cmd.print(f'[reverse red]ERROR[/reverse red] {message}')

def rich_warning(message:str) -> None:
    cmd.print(f'[reverse yellow]WARNING[/reverse yellow] {message}')

def install(repo_url:str) -> None:
    dirs = os.listdir()
    if "mojo_modules" not in dirs:
        rich_error("""Your project is not initialized
        Please run `mopm init . ` to initialize the project""")
        return
    subprocess.check_output( ["git", "clone", repo_url] )
    
