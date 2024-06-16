from pydantic import BaseModel


class getStocksDataRequest(BaseModel):
    exchange: str
    stock: str


class getStocksRequest(BaseModel):
    exchange: str
    ch: str
