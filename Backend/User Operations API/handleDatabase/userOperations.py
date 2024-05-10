
from middlewares.userAuth import userAuth
import pymongo
class userOperation:
    async def signUp(userscollection:pymongo.collection.Collection,name:str,password:str,email:str,username:str):
        
        f=(userscollection.find_one({"username":username}) or userscollection.find_one({"email":email}))!= None #flag
        if(f):
            return {"status":401,"message":("User with username or alredy exists")}
        else:
            try:
                password=userAuth.passcrypt(password)
                userscollection.insert_one({
                    "username":username,
                    "name":name,
                    "password":password,
                    "email":email,
                })
                return {"status":200,"message":"User Created"}
            except:
                return {"status":401,"message":"Please try again"}
    async def login(userscollection:pymongo.collection.Collection,email:str,password:str):
        try:
            user=userscollection.find_one({'email':email})
            password=userAuth.passcrypt(password=password)
            if(user['password']==password):
                token_JWT=userAuth.genJWT(username=user["username"],_id=str(user["_id"]))
                
                return {"name":user["name"],"email":user["email"],"JWT": token_JWT,"status": 200, "message":"login successful"}
            else :
                return {"status":401,"message":"Incorrect Password. Try Again."}
        except Exception as e: 
            print(e)
            return {"there was an unexpected error"}
        
        
        