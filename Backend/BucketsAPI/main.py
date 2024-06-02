# IMPORTS
from fastapi import FastAPI
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from dataRetrival import stockRetrivals

load_dotenv()
# SETUP CONFIGURATION
app = FastAPI()
origins = [f'http://{os.getenv("frontendHost")}:{os.getenv("frontendPort")}']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
# connect_string = 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority'
# connect_string = f'mongodb://{os.getenv("DatabaseHost")}:{os.getenv("DatabasePort")}/?directConnection=true'
# my_client = pymongo.MongoClient(connect_string)
# userdb = my_client["users"]
# userscollection = userdb["users"]
# print(type(userscollection))
stockretrivals = stockRetrivals()


# @app.post("/signUp")
# async def signup(data: signUpDetails):

#     try:
#         data = await userOperation.signUp(
#             userscollection=userscollection,
#             username=data.username,
#             name=data.name,
#             email=data.email,
#             password=data.password,
#         )
#     except Exception as e:
#         print(e)
#     return {"message": data}


@app.get("/getExchanges")
async def getExchanges():
    try:
        data = await stockretrivals.getExchanges()
    except Exception as e:
        print(e)
        return {"Error": e}
    return data


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.getenv("UserOperationsApiHost"),
        port=int(os.getenv("UserOperationsApiPort")),
    )
