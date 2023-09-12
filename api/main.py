from api.tools.repos import *
from api.tools.auth import *
from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/repos/create")
def create_repo(data:dict) -> Response:
    add_repo(data)
    return Response(data, status_code=200)
 
@app.get("/repos")
def get_repos():
    return Response(get_repos(), status_code=200)