from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://tubilo:admin@mojopak.buok0w6.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['repos']
collection = db['repos']
print(list(collection.find()))
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
    return list(collection.find())

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
    collection.insert_one(data)

def search_repo(name:str) -> dict|None:
    '''
    Receives:
        name: str
    Returns:
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
            OR None, if not found
    '''
    return collection.find_one({"name": name})