from pymongo import MongoClient
import certifi

client = MongoClient("mongodb+srv://Naad:naad2002@cluster0.7redvzp.mongodb.net/", tlsCAfile=certifi.where(),)

db = client.hacks8

users_collections = db["users"]


