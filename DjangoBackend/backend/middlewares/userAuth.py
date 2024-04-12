import pymongo
import scrypt 
import os
from dotenv import load_dotenv

load_dotenv()
class userAuth:
    salt=os.getenv("Salt")
    def __init__(self,db):
        self.users=db
    def passcrypt(self,password:str):
        password = scrypt.hash(password, self.salt, N=16384, r=8, p=1)
        return password
