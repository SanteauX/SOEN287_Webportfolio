import urllib
import json
import unicodedata
import requests

url = "https://api.github.com/users/SanteauX/repos"

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

def scraping_github(url):
    # Scraping of my github repo
    # url = "https://api.github.com/users/SanteauX/repos"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

def obj_github(data):
    # Create objects from data gathered
    liste = []
    i = 0
    for k in data:
        i = i+1
        #str(thing) for encoding reasons (u'String')
        rank = str(i)
        name = str(k["name"])
        url = str(k["url"])
        language = str(k["language"])
        created_at = str(k["created_at"])
        full_name = str(k["full_name"])
        github_repo = repo_github(rank, name, url, language, created_at, full_name)
        liste.append(github_repo)
        # test function: print(github_repo.get_line())
        # test function: print("\n")
    return liste

def write_csv(liste):
    # write data from github in data/github_projects.csv
    f = open("data/github_projects.csv", "w")
    f.write("rank, name, url, language, created_at, full_name \n" )
    for i in range(0, len(liste)):
        f.write(liste[i].get_line())
        
def test_lines(lines):
    for i in range(0, len(liste)):
        print(liste[i].get_line())

data = scraping_github(url)
liste = obj_github(data)
write_csv(liste)
test_lines(liste)
