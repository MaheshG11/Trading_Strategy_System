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

    def getStocksData(self, backgroundTasks: BackgroundTasks, exchange: str):
        filename = self.getStocksDataFrame(exchange=exchange, backTestDays=2520)
        print(filename)
        yesterday = str((datetime.now() - timedelta(1)).date()) + ".pickle"
        try:
            yesterdays_file = os.path.join("output", yesterday)
            os.remove(yesterdays_file)
        except Exception as e:
            return


if __name__ == "__main__":
    b = BackgroundTasks()
    a = stockRetrivals()
    a.getStocksData(b, exchange="bse")
