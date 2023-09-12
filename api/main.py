from tools.repos import *
from tools.auth import *
from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/repos/create")
def create_repo(data:dict) -> Response:
    add_repo(data)
    return Response(status_code=200)
 
@app.get("/repos")
def aaaa():
    data = str(get_repos())
    return Response(data, status_code=200)

@app.get("/repos/search/<pkg_name>")
def get_package(pkg_name):
    data = str(get_repos())
    return Response(data, status_code=200)