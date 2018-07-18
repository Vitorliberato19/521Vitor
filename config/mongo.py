#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient()
db = client['flask-app']

# for x in db.usuarios.find():
#     print(x)


