from pymongo import MongoClient
import json

# connect the db on the container using port mapping from the host
mongo_host = "localhost"
mongo_port = 27017
mongo_user_name = "root"
mongo_user_password = "example"
mongo_db_name = "cr-db"
mongo_collection = "users"
export_file_path = "/mongo/db_export/users.json"

users = []

# Connect and authenticate to the database
client = MongoClient(host=mongo_host, port= mongo_port)
client.admin.authenticate(mongo_user_name, mongo_user_password)
# Get the database and the collection
db = client[mongo_db_name]
collection = db[mongo_collection]

# Saving all the data in the collection
for item in collection.find():
    item["_id"] = str(item["_id"])
    users.append(item)
with open(export_file_path, 'w') as outfile:
    json.dump(users, outfile)