import subprocess, os, getpass
from rich.console import Console
cmd = Console()

def get_home_dir() -> str:
    """
    Returns the home directory of the current user.

    :return: A string representing the path of the home directory.
    :rtype: str
    """
    return os.path.expanduser("~")

def rich_error(message:str) -> None:
    cmd.print(f'[reverse red]ERROR[/reverse red] {message}')

def rich_warning(message:str) -> None:
    cmd.print(f'[reverse yellow]WARNING[/reverse yellow] {message}')


def rich_info(message:str) -> None:
    cmd.print(f'[reverse blue]INFO[/reverse blue] {message}')

def rich_sucess(message:str) -> None:
    cmd.print(f'[reverse green]SUCESS[/reverse green] {message}')

def install(repo_url:str) -> int:
    """
    Installs a package from a given repository URL.

    Parameters:
    - repo_url (str): The URL of the repository.

    Returns:
    - int: 0 if the package is installed successfully, 1 otherwise.
    """
    pkg_name = repo_url.split("/")[-1]
    #Get the user's home directory, by getting the username 
    username = getpass.getuser()
    dirs = os.listdir(f'/home/{username}')

    if ".mojo_modules" not in dirs:
        rich_error("""MPAK Was not installed correctly. 
        Please run `mpak init` to initialize mpak.""")
        return 1
    try:
        rich_info(f"Found package {pkg_name}")
        rich_info("Trying to install...")
        subprocess.check_call(["cd", f"/home/{username}/.mojo_modules", "&&", "git", "clone", repo_url], shell=False)
        rich_sucess(f"Package {pkg_name} installed")
        return 0 
    except Exception as e:
        with open("error.log", "w") as f:
            f.write(str(e))
        rich_error(f"Failed to install package {pkg_name}")
        return 1

def uninstall(pkg_name:str) -> int:
    dirs = os.listdir()
    if ".mojo_modules" not in dirs:
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