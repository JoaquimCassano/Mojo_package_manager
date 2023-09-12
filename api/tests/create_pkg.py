
import requests

url = "http://localhost:8000/repos/create"

data = {
    "name":"tubinho",
    "repo": {
        "name": "tubinho",
        "description": "aaaaaaaaaa",
        "github_url": "dummy_github_url"
    },
    "user": {
        "username": "dummy_username",
        "real_name": "dummy_real_name",
        "last_name": "dummy_last_name",
        "email": "dummy_email"
    }
}
#requests.get(url, json=data)
print(requests.get('http://localhost:8000/repos/').json())