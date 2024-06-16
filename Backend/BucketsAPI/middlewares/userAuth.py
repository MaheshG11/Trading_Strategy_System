import scrypt
import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta
import pytz

load_dotenv()
salt = os.getenv("Salt")


class userAuth:
    def verifyJWT(token_JWT: str):

        try:
            decoded_payload = jwt.decode(
                token_JWT, salt, algorithms=os.getenv("JWT_Hashing_Algo")
            )

            current_time = datetime.now(pytz.utc)
            if (
                decoded_payload.get("exp") is not None
                and current_time.date()
                > datetime.fromtimestamp(decoded_payload["exp"]).date()
            ):
                return None, False
            else:
                return decoded_payload["_id"], True
        except Exception as e:
            return e, False
