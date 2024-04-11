import pymongo  # type: ignore
class userOperation:
    def __init__(self,db:pymongo.collection.Collection):
        self.users=db
    def signUp(self,name:str,password:str,email:str,username:str):
        users=self.users
        print("at")
        if(users.find_one({"username":username})!= None):
            return {"success":0,"message":("User with username alredy exists")}
        elif(users.find_one({"email":email})!= None):
            return {"success":0,"message":"User with this email already exists"}
        else:
            try:
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
                return {"success":1,"message":"User Created"}
            except:
                return {"success":0,"message":"Please try again"}
            