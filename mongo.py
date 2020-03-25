from pymongo import MongoClient

import ssl


uri = "mongodb+srv://HugoAdmin:<yvctrd6F7GUYBVYT>@personalsite-3gjka.mongodb.net/test?retryWrites=true&w=majority??ssl=true&ssl_cert_reqs=CERT_NONE"
cluster = MongoClient("uri")
db = cluster['Site']
collection = db['BlogPosts']

post = {"_id": 0, "author": "Hugo Joncour", "date": "25/03/2020", "Title": "test", "Subtitle": "subtitle test", "tags": ["CS", "ECON"], "body": ["part 1", "part 2"], "images": ["image 1", "image 2"]}
collection.insert_one(post)
