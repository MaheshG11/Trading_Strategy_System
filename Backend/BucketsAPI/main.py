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
from userAuth.userOperations import userOperation

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


@app.get("/stocksData")
async def getStocksData(data: getStocksDataRequest, backgroundTasks: BackgroundTasks):
    ver = await userOperation.verifyJWT(token=data.token)  # verifying token
    if ver[1]:
        file = os.path.join("output/", str((datetime.now()).date()) + ".pickle")
        if os.path.isfile(file):

            def iter_file():
                with open(file, "rb") as f:
                    for chunk in iter(lambda: f.read(1024), b""):
                        yield chunk

            response = StreamingResponse(
                iter_file(), media_type="application/octet-stream"
            )
            response.headers["Content-Disposition"] = (
                f"attachment; filename=model.pickle"
            )
            return response
        else:
            backgroundTasks.add_task(
                stockretrivals.getStocksData, exchange=data.exchange
            )
            return {
                "message": "We are working on it please request data after a few minutes",
                "status": 200,
            }
    else:
        return {"message": "Login again to process the request", "status": 200}


@app.post("/generateReport")
async def generateReport(token: str, file: UploadFile = File(...)):
    ver = await userOperation.verifyJWT(token=token)
    if ver[1]:
        backgroundTasks: BackgroundTasks
        contents = await file.read()
        backgroundTasks.add_task(generateReport_, contents)
    else:
        return {
            "message": "Unauthorized, login again",
            "status": status.HTTP_401_UNAUTHORIZED,
        }
    return "We are yet to work on it. When we do go to reports section and you will find your report there"


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.getenv("UserOperationsApiHost"),
        port=int(os.getenv("UserOperationsApiPort")),
    )
