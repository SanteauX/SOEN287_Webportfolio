import urllib

url = 'https://api.github.com/users/SanteauX/repos'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.urlencode(values)
data = data.encode('ascii') # data should be bytes
print(data)
