from fastapi import FastAPI
from dataTypes import *
import uvicorn
from handleDatabase.userOperations import userOperation
import pymongo
import os


app = FastAPI()

#connect_string = 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority'
connect_string=f'mongodb://{os.getenv("DatabaseHost")}:{os.getenv("DatabasePort")}/?directConnection=true'
my_client = pymongo.MongoClient(connect_string)
userdb=my_client["users"]
userscollection=userdb["users"]
print(type(userscollection))
ops=userOperation(db=userscollection)


@app.post("/signUp")
async def signup(data:signUpDetails):
    
    try:
        data=ops.signUp(username=data.username,name=data.name,email=data.email,password=data.password)
    except:
        print('the except condition')
 
    return {"message":data}
    
    
@app.get("/signUp")
async def login(data:loginDetails):
    try:
      data=ops.login(email=data.email,password=data.password)
    except:
      print('the except condition')
    return "some message"
if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("UserOperationsApiHost"), port=int(os.getenv("UserOperationsApiPort")))