import urllib
import json
import requests

class repo_github(object):
    def __init__(self, rank, name, url, language, created_at):
        self.rank = rank
        self.name = name
        self.url = url
        self.language = language
        self.created_at = created_at

url = "https://api.github.com/users/SanteauX/repos"

response = urllib.urlopen(url)
data = json.loads(response.read())
liste = []
for k in data:
    github_repo = repo_github(k, k["name"], k["url"], k["language"], k["created_at"])
    liste.append(github_repo)

for i in range(0, len(liste)):
    print(liste[i].name)

f = open("data/github_projects.csv", "w")


for i in
lines = f.readlines()
