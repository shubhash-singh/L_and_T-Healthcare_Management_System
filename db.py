from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare_system"]

# Functions for database operations
def insert_record(collection, data):
    db[collection].insert_one(data)
    print(f"Record added to {collection}.")

def find_record(collection, query):
    return db[collection].find_one(query)

def update_record(collection, query, new_values):
    db[collection].update_one(query, {"$set": new_values})
    print(f"Record updated in {collection}.")

def delete_record(collection, query):
    db[collection].delete_one(query)
    print(f"Record deleted from {collection}.")
