
import requests

url = "http://localhost:8000/repos/create"

data = {
    "name":"tubinho",
    "repo": {
        "name": "tubinho",
        "description": "aaaaaaaaaa",
        "github_url": "https://github.com/SoUmNerd/Mojo_package_manager"
    },
    "user": {
        "name": "dummy_name",
        "email": "dummy_email"
    }
}
requests.post(url, json=data)
print(requests.get('http://localhost:8000/repos/').content)