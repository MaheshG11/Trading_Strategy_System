from pydantic import BaseModel


class getStocksDataRequest(BaseModel):
    exchange: str
    token: str
