import scrypt 
import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta
import pytz

load_dotenv()
salt=os.getenv("Salt")
class userAuth:
    
    def passcrypt(password:str):
        password = scrypt.hash(password, salt, N=16384, r=8, p=1)
        return password
    def genJWT(username:str,_id:str):
        payload={
            "_id": _id,
            "username": username,
            "exp": datetime.now(pytz.utc) + timedelta(days=2)
        }
        token =jwt.encode(payload, salt, algorithm=os.getenv("JWT_Hashing_Algo"))
        print(token)
        return token
    def verifyJWT(token_JWT:str):
        
        try:
            decoded_payload = jwt.decode(token_JWT, salt,algorithm=[os.getenv("JWT_Hashing_Algo")])
            current_time = datetime.now(pytz.utc)
            if decoded_payload.get('exp') is not None and current_time > datetime.fromtimestamp(decoded_payload['exp']):
                return False
            else:
                return True
        except jwt.exceptions.JWTError as e:
            return False