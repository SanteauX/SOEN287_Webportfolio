from pymongo import MongoClient

import ssl


client = MongoClient("mongodb+srv://admin:<admin>@personalsite-3gjka.mongodb.net/test?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
db = client.test

db = client['Site']

collection = db['BlogPosts']
#print(collection)
post = {"_id": 0, "author": "Hugo Joncour", "date": "25/03/2020"}
#, "Title": "test", "Subtitle": "subtitle test", "tags": ["CS", "ECON"], "body": ["part 1", "part 2"], "images": ["image 1", "image 2"]}
collection.insert_one(post)
