from connectDatabase import connectDatabase
import psycopg2
from operations import databaseQueries
from fastapi import BackgroundTasks
from datetime import datetime, timedelta
import os


class stockRetrivals(databaseQueries):

    def __init__(self) -> None:
        super().__init__()

    async def getExchanges(self):
        data = self.exchanges("mastertable")

        return {"status": 200, "data": data}

    async def getStockData(self, exchange, stock):
        data = self.stockData(exchange=exchange, stock=stock)

        return {"status": 200, "data": data}


if __name__ == "__main__":
    b = BackgroundTasks()
    a = stockRetrivals()
    a.getStocksData(b, exchange="bse")
