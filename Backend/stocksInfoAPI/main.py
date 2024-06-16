# IMPORTS
from fastapi import (
    FastAPI,
    Path,
    File,
    UploadFile,
    BackgroundTasks,
    HTTPException,
    status,
)
from bson.objectid import ObjectId
from fastapi.responses import StreamingResponse
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from dataRetrival import stockRetrivals
from datetime import datetime
from FunctionsAsAsync import *
from datatypes.datatypes import *

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


@app.get("/getExchanges")
async def getExchanges():
    try:
        data = await stockretrivals.getExchanges()
    except Exception as e:
        print(e)
        return {"Error": e, "status": 400}
    return {"data": data, "status": 200}


@app.get("/stockData")
async def getStockData(data: getStocksDataRequest, backgroundTasks: BackgroundTasks):
    try:
        data = await stockretrivals.getStockData(
            exchange=data.exchange, stock=data.stock
        )
        return data
    except Exception as e:
        print(e)
        return {"Error": e, "status": 400}


@app.get("/stocks")
async def getStockData(data: getStocksRequest, backgroundTasks: BackgroundTasks):
    try:
        data = await stockretrivals.stocks(exchange=data.exchange, stock=data.ch)
    except Exception as e:
        print(e)
        return {"Error": e, "status": 400}
    return {"data": data, "status": 200}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.getenv("UserOperationsApiHost"),
        port=int(os.getenv("UserOperationsApiPort")),
    )
