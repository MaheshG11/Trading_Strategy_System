#IMPORTS
from fastapi import FastAPI
from dataTypes import *
import uvicorn
from handleDatabase.userOperations import userOperation
import pymongo
import os
from fastapi.middleware.cors import CORSMiddleware

#SETUP CONFIGURATION
app = FastAPI()
origins = ["http://localhost:3000"] 
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=False, allow_methods=["*"], allow_headers=["*"]
)
#connect_string = 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority'
connect_string=f'mongodb://{os.getenv("DatabaseHost")}:{os.getenv("DatabasePort")}/?directConnection=true'
my_client = pymongo.MongoClient(connect_string)
userdb=my_client["users"]
userscollection=userdb["users"]
print(type(userscollection))


@app.post("/signUp")
async def signup(data:signUpDetails):
    
    try:
        data= await userOperation.signUp(userscollection=userscollection,username=data.username,name=data.name,email=data.email,password=data.password)
        
    except Exception as e:
        print(e)
 
    return {"message":data}
    
    
@app.get("/login")
async def login(data:loginDetails):
    try:
      data= await userOperation.login(userscollection=userscollection,email=data.email,password=data.password)
    except:
      print('the except condition')
    return data
if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("UserOperationsApiHost"), port=int(os.getenv("UserOperationsApiPort")))