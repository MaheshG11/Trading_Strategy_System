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
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from dataRetrival import stockRetrivals
from datetime import datetime
from FunctionsAsAsync import *

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
        return {"Error": e}
    return data


@app.get("/stocksData")
async def getStocksData(exchnage: str, backgroundTasks: BackgroundTasks):
    file = os.path.join("output/", str((datetime.now()).date()) + ".pickle")
    if os.path.isfile(file):
        data = await readFile(filePath=file)
        return data
    else:
        backgroundTasks.add_task(stockretrivals.getStocksData, exchange=exchnage)
        return "We are working on it please request data after a few minutes"


@app.post("/generateReport")
async def generateReport(file: UploadFile = File(...)):
    backgroundTasks: BackgroundTasks
    backgroundTasks.add_task(
        generateReport,
    )
    file = os.path.join("output/", str((datetime.now()).date()) + ".pickle")
    os.path.isfile(file)
    contents = await file.read()
    print(contents.decode("utf-8"))

    return "We are yet to work on it. When we do go to reports section and you will find your report there"


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.getenv("UserOperationsApiHost"),
        port=int(os.getenv("UserOperationsApiPort")),
    )
