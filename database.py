from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")  

db = client["phone_database"]

collection = db["phone_numbers"]
