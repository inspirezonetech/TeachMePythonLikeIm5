# ------------------------------------------------------------------------------------
"""
This tutorail is about to getting started with MongoDB using Python. There is a module for Pymongo for the same.
This one is the basic tutorial for Pymongo,some beginners things are discussed.
"""
# ------------------------------------------------------------------------------------
#Importing Modules
from pymongo import MongoClient
import pymongo
#Establish connection
from pymongo import MongoClient
#We can pass our host details in Mongoclient() function in 2 ways, also by default it is on "Localhost" and 27017 Port.
#client=MongoClient("Localhost",27017)
#client=MongoClient("mongodb://localhost:27107")
client=MongoClient()
print(client)
#Checking for available databases
print("Available Databases",client.list_database_names())
#Creating Database
db=client.test_database #also we can write client['test_database']
print(db)
#Checking for available connections in database
print("Available Collections",db.list_collection_names())
#Creating a Collection in DB
collection=db.test_collection #also we can write db['test_course']
print(collection)
# ------------------------------------------------------------------------------------
# Challenge: Try Creating a Database and Collection with "yourname_database/collection" using some remote host.
# ------------------------------------------------------------------------------------


