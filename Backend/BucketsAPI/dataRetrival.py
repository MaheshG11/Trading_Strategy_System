from connectDatabase import connectDatabase
import psycopg2
from operations import databaseQueries


class stockRetrivals(databaseQueries):

    def __init__(self) -> None:
        super().__init__()

    async def getExchanges(self):
        data = self.exchanges("mastertable")

        return {"status": 200, "data": data}
