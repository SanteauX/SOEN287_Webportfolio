import urllib
import json
import requests

class repo_github(object):
    def __init__(self, rank, name, url, language, created_at, full_name):
        self.rank = rank
        self.name = name
        self.url = url
        self.language = language
        self.created_at = created_at
        self.full_name = full_name

    def get_name(self):
        return self.name

    def get_rank(self):
        return self.rank
    
    def get_url(self):
        return self.url
    
    def get_language(self):
        return language
    
    def get_created_at(self):
        return created_at

    def get_full_name(self):
        return full_name

    def get_line(self):
        stringy = str(self.rank) + ","
        return stringy  
        #stringy = self.rank + "," + self.name + "," + self.url + "," + self.language + "," + self.created_at + "," + self.full_name
        #return stringy
        
    def test(self):
        stringy = "name: " + self.name + ","
        return stringy   

url = "https://api.github.com/users/SanteauX/repos"

response = urllib.urlopen(url)
data = json.loads(response.read())
liste = []
for k in data:
    rank = k
    name = k["name"]
    url = k["url"]
    language = k["language"]
    created_at = k["created_at"]
    full_name = k["full_name"]
    github_repo = repo_github(rank, name, url, language, created_at, full_name)
    liste.append(github_repo)
    #print(github_repo.test())
    print(github_repo.get_line())


f = open("data/github_projects.csv", "w")
f.write("rank, name, url, language, created_at, full_name \n" )
for i in range(0, len(liste)):
    comma = ","
    #stringy = liste[i].get_rank() + comma + liste[i].get_name() + comma + liste[i].get_url() + comma, liste[i].get_language() + comma + liste[i].get_created_at() + comma + liste[i].get_full_name()
    #print(stringy)
