from middlewares.userAuth import userAuth
import pymongo
from bson.objectid import ObjectId


class userOperation:

    async def verifyJWT(token: str):
        return userAuth.verifyJWT(token)
