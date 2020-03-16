import urllib
import json
import requests

class repo_github(object):
    def __init__(self, name, url, language, created_at):
        self.name = name
        self.url = url
        self.language = language
        self.created_at = created_at



url = "https://api.github.com/users/SanteauX/repos"

# data = requests.get(url)
# json_data = data.json()

# json_file = json.loads(json_data)
# u = repo_github(json_file)

response = urllib.urlopen(url)
data = json.loads(response.read())
liste = []
for k in data:
    github_repo = repo_github(k["name"], k["url"], k["language"], k["created_at"])
    liste.append(github_repo)


for i in liste:
    print(liste[i])

    # print(k["name"])
    # print(k["url"])
    # print(k["language"])
    # print(k["created_at"])
    # print("\n \n")
