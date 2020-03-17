import urllib
import json
import unicodedata
import requests

# Class for the data scraped on my github repo
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
        stringy = self.rank + "," + self.name + "," + self.url + "," + self.language + "," + self.created_at + "," + self.full_name + "\n"
        return stringy  

# Scraping of my github repo

url = "https://api.github.com/users/SanteauX/repos"
response = urllib.urlopen(url)
data = json.loads(response.read())
liste = []

i = 0
for k in data:
#str(thing) for encoding reasons (u'String')
    i = i+1
    rank = str(i)
    name = str(k["name"])
    url = str(k["url"])
    language = str(k["language"])
    created_at = str(k["created_at"])
    full_name = str(k["full_name"])
    github_repo = repo_github(rank, name, url, language, created_at, full_name)
    liste.append(github_repo)
    print(github_repo.get_line())
    print("\n")


f = open("data/github_projects.csv", "w")
f.write("rank, name, url, language, created_at, full_name \n" )

for i in range(0, len(liste)):
    f.write(liste[i].get_line())
    
