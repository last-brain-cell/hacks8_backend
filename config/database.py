from pymongo import MongoClient

client = MongoClient("mongodb+srv://Naad:naad2002@cluster0.7redvzp.mongodb.net/")

db = client.hacks8

users_collections = db["users"]


