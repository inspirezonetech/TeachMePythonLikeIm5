# ------------------------------------------------------------------------------------
"""
This Tutorial is about performing CRUD operations using Python in MongoDB.
CRUD stands for CREATE,READ,UPDATE,DELETE.
"""
# ------------------------------------------------------------------------------------
# Importing Modules
from pymongo import MongoClient
import pymongo
# Establish connection
from pymongo import MongoClient
# We can pass our host details in Mongoclient() function in 2 ways, also by default it is on "Localhost" and 27017 Port.
# client=MongoClient("Localhost",27017)
# client=MongoClient("mongodb://localhost:27107")
client = MongoClient()
print(client)
# Checking for available databases
print("Available Databases", client.list_database_names())
# Creating Database
db = client.test_database  # also we can write client['test_database']
# Checking for available connections in database
print("Available Collections", db.list_collection_names())
# Creating a Collection in DB
collection = db.test_collection  # also we can write db['test_course']
# ---CREATE--- (Create a record)
record = {
    "name": "Max Schwarzmueller",
    "age": 29
}
# Inserting this document in collection
insertion = collection.insert_one(record)
# Whenever we insert document is collection it by default takes ID as one of its field. We can also give ID manually to a document.
if insertion.acknowledged:
    print("Document is added and ID is: ", insertion.inserted_id)
# ---READ--- (Read documents from collection)
# Note: It will not return value instead it will return a cursor.
reading = collection.find()
print("This is cursor returned by MongoDB: ", collection)
# For seeing that value
for _ in reading:
    print(_)
# ---UPDATE--- (Updating an existing record)
update_query = {'name': 'Max Schwarzmueller'}
# $set will set new value of name based on update_query.
new_value = {"$set": {'name': 'James Bond'}}
# passing this values in update function
collection.update_one(update_query, new_value)
# print values after the update
for x in collection.find():
    print(x)
# ---DELETE--- (Deleting existing record)
# now deleting value based on query
delete_query = {'name': 'Max Schwarzmueller'}
# passing this value in delete function
collection.delete_one(delete_query)
# print values after the delete
for x in collection.find():
    print(x)
# ------------------------------------------------------------------------------------
# Challenge: Use this constraints and perform CRUD operations.
"""
1. Create a document with following fields: name,date(current),age,favourite_programming_language.
2. Read values from collection for those whose "favourite language is Python".
3. Update values for those whose age is greater than 30 and change it to 21
4. Delete the records of those whose favourite programming language is "C/C++".
"""
# ------------------------------------------------------------------------------------
