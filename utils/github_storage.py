import base64
import json
import requests
import yaml


class GitHubYAMLStore:
def __init__(self, token, repo_owner, repo_name, data_path):
self.token = token
self.repo_owner = repo_owner
self.repo_name = repo_name
self.data_path = data_path
self.api = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{data_path}"
self.headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}


def read_yaml(self):
r = requests.get(self.api, headers=self.headers)
if r.status_code == 404:
return None
r.raise_for_status()
content_b64 = r.json()["content"]
content = base64.b64decode(content_b64).decode("utf-8")
return yaml.safe_load(content)


def write_yaml(self, payload, commit_message="Update documents"):
# get SHA if exists
sha = None
r = requests.get(self.api, headers=self.headers)
if r.status_code == 200:
sha = r.json().get("sha")
elif r.status_code != 404:
r.raise_for_status()


data = yaml.safe_dump(payload, allow_unicode=True).encode("utf-8")
body = {
