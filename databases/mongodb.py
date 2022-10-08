
# ------------------------------------------------------------------------------------
# Tutorial: brief description of tutorial content
# ------------------------------------------------------------------------------------
'''

MongoDB
MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable.

To be able to experiment with the code examples in this tutorial, you will need access to a MongoDB database.

You can download a free MongoDB database at https://www.mongodb.com.

Or get started right away with a MongoDB cloud service at https://www.mongodb.com/cloud/atlas.

PyMongo
Python needs a MongoDB driver to access the MongoDB database.

In this tutorial we will use the MongoDB driver "PyMongo".

We recommend that you use PIP to install "PyMongo".

PIP is most likely already installed in your Python environment.

Navigate your command line to the location of PIP, and type the following:

Download and install "PyMongo":

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install pymongo


For more information visit : https://www.w3schools.com/python/python_mongodb_getstarted.asp

# ------------------------------------------------------------------------------------

# Code here explaining concept with comments to guide'''

# ------------------------------------------------------------------------------------

from pymongo import MongoClient

# connect to mongodb
client = MongoClient('localhost', 27017)

# create database
db = client['test-database']

# create collection
collection = db['test-collection']

# insert data
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": "2018-01-01"}
posts = db.posts
post_id = posts.insert_one(post).inserted_id

# find data
db.collection_names(include_system_collections=False)
db.collection_names(include_system_collections=True)
db.collection_names()

# update data
db.collection.update_one(
    {"author": "Mike"},
    {
        "$set": {
            "text": "My first blog post!",
            "date": "2018-01-01"
        }
    }
)

# delete data
db.collection.delete_one({"author": "Mike"})
db.collection.delete_many({"author": "Mike"})
db.collection.delete_many({})
db.collection.drop()

# drop database
client.drop_database('test-database')

# close connection
client.close()

# end of file


# ------------------------------------------------------------------------------------
# Challenge: list challenges to be completed here. minimum of one challenge per tutorial
# ------------------------------------------------------------------------------------

''' 
MongoDB cannot handle many connections and many concurrent users per node, companies often need to add a dedicated 
third-party cache to help MongoDB meet their performance requirements. The need for a third-party cache can add both
cost and complexity to a MongoDB deployment.
'''

# ------------------------------------------------------------------------------------


