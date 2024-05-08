import pymongo  # type: ignore
from middlewares.userAuth import userAuth
class userOperation:
    def __init__(self,db:pymongo.collection.Collection):
        self.users=db
        self.authMiddlewares=userAuth(db)
        
        
    def signUp(self,name:str,password:str,email:str,username:str):
        users=self.users
        if(users.find_one({"username":username})!= None):
            return {"status":401,"message":("User with username alredy exists")}
        elif(users.find_one({"email":email})!= None):
            return {"status":401,"message":"User with this email already exists"}
        else:
            try:
                password=self.authMiddlewares.passcrypt(password)
                users.insert_one({
                    "username":username,
                    "name":name,
                    "password":password,
                    "email":email,
                    "netProfits":[{
                        "allotedFunds":0,
                        "currency":"Rs",
                    }],
                    "funds":[{
                        "allotedFunds":0,
                        "currency":"Rs",
                    }],
                })
                return {"status":200,"message":"User Created"}
            except:
                return {"status":401,"message":"Please try again"}
    def login(self,email:str,password:str):
        try:
            user=self.users.find_one({'email':email})
            password=self.authMiddlewares.passcrypt(password)
            if(user['password']==password):
                token_JWT=self.authMiddlewares.genJWT(username=user["username"],_id=str(user["_id"]))
                
                return {"name":user["name"],"email":user["email"],"JWT": token_JWT,"status": 200, "message":"login successful"}
            else :
                return {"status":401,"message":"Incorrect Password. Try Again."}
        except Exception as e: 
            return e
        
        
        