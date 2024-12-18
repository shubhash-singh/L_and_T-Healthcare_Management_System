from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare_system"]

def insert_record(collection, data):
    db[collection].insert_one(data)

def find_record(collection, query):
    return db[collection].find_one(query)

def find_all_records(collection, query={}):
    return list(db[collection].find(query))

def update_record(collection, query, new_values):
    db[collection].update_one(query, {"$set": new_values})

def delete_record(collection, query):
    db[collection].delete_one(query)
