from tinydb import TinyDB, Query
from tinydb_sqlite import SQLiteStorage

# Initialize TinyDB
repos = TinyDB(storage=SQLiteStorage, connection='db.sqlite')

def get_repos():
    '''
    Just, return all repos, lol.
    Receives:
        Nothing, what did you expect?
    Returns:
        repos: list of dicts, following this schema: 
        {
            repo: dict {
                name: str,
                description: str,
                github_url: str,
            }
            user: dict {
                username: str,
                real_name: str,
                last_name:str,
                email: str
            }
        }
    '''
    return repos.all()

def add_repo(data:dict) -> None:
    '''
    Receives:
        data: dict -> {
            repo: dict {
                name: str,
                description: str,
                github_url: str,
            }
            user: dict {
                username: str,
                real_name: str,
                last_name:str,
                email: str
            }
        }
    Returns:
        None
    '''
    repos.insert(data)