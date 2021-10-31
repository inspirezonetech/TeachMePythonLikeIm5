# ------------------------------------------------------------------------------------
# Implementation of REST API using Python and FastAPI
# ------------------------------------------------------------------------------------

import uvicorn
# uvicorn is a lightning-fast ASGI server implementation,
# using uvloop and httptools.

# the main function to run the API on the localhost
if __name__ == "__main__":
    """
    Run the app with uvicorn server on localhost and port given as parameters.
    """
    uvicorn.run("src.main:app", host="localhost", port=8081, reload=True)

# ------------------------------------------------------------------------------------
# Challenge: Create your own Student API having attributes like name, rollno, class etc.
# and add all the http methods explained.
# ------------------------------------------------------------------------------------
