# ------------------------------------------------------------------------------------
# Implementation of REST API using Python and FastAPI
# ------------------------------------------------------------------------------------

from typing import Optional
from fastapi import FastAPI

# intialising the REST API
app = FastAPI(title="REST API", docs_url="/", redoc_url="/doc")

# get method with endpoint /
@app.get("/")
def read_root():
    # returns the message
    return {"Hello": "World"}

# get method with endpoint /items/{item_id}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    # returns the item_id along with query q.
    return {"item_id": item_id, "q": q}

# ------------------------------------------------------------------------------------
# Challenge: Create get methods for Student API to view attributes like name, rollno, class etc.
# ------------------------------------------------------------------------------------
