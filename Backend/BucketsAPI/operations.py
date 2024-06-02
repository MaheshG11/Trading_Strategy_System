from connectDatabase import connectDatabase
import psycopg2
import pandas as pd
from datetime import datetime, timedelta, timezone


class databaseQueries:

    def __init__(self) -> None:
        self.dbs = {}
        self.cur = {}
        self.dbs["masterdb"] = connectDatabase.connect("masterdb")
        self.cur["masterdb"] = self.dbs["masterdb"].cursor()

    def getCursor(self, dbName):
        cur = None
        if dbName not in self.dbs:
            try:

                self.dbs[dbName] = connectDatabase.connect(dbName)
                cur = self.dbs[dbName].cursor()
                self.cur[dbName] = cur

            except Exception as e:
                print(e)
                return e
        return self.cur[dbName]

    def exchanges(self):
        query = f"SELECT * FROM mastertable;"
        cur = self.dbs["masterdb"]
        cur.execute(query=query)
        data = []
        for i in cur:
            data.append(i[0])
        return data

    def getTableDaily(
        self, exchange: str, tableName, currentTime: datetime, delta=0, backTestDays=504
    ):
        try:
            exchange = ("_".join(exchange.split("."))).lower()
            tableName = ("_".join(tableName.split("."))).lower()

            cur = self.getCursor(exchange)
            print(cur)
            query = f"""SELECT column_name, data_type
                    FROM information_schema.columns
                    WHERE table_schema = 'public' AND table_name = '{tableName}';"""
            cur.execute(query=query)
            columns = []

            for i in cur:
                columns.append(i)
            i = 2
            data = {}
            n = len(columns)
            while i < n:
                data[columns[i][0]] = []
                i += 1

            query = f"SELECT * FROM {tableName} WHERE id=1;"
            try:
                cur.execute(query=query)
            except Exception as e:
                print(e)
                return None
            val = None
            for i in cur:
                val = i
                break
            firstDate = currentTime - timedelta(days=delta + backTestDays)
            if val[1] - (firstDate) > timedelta(0):
                print("here")
                return None
            query = f"SELECT * FROM {tableName} WHERE date> '{str(firstDate.date())}';"
            cur.execute(query=query)
            index = []

            for i in cur:

                index.append(i[1])
                ind = 2
                while ind < len(columns):
                    data[columns[ind][0]].append(float(i[ind]))
                    ind += 1

            data = pd.DataFrame(data, index=index)

            return data
        except Exception as e:
            print(e)
            return None

    def getExchangeTable(self, exchange):
        exchange = "_".join(exchange.split("."))
        cur = self.getCursor("masterdb")
        query = f"""SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_schema = 'public' AND table_name = '{exchange}';"""

        cur.execute(query=query)
        columns = []
        for i in cur:
            columns.append(i)
        query = f"SELECT * FROM {exchange};"
        cur.execute(query=query)
        i = 1
        data = {}
        n = len(columns)
        while i < n:
            data[columns[i][0]] = []
            i += 1
        index = []
        for i in cur:
            index.append(i[0])
            ind = 1
            while ind < n:
                if i[ind] == None:
                    data[columns[ind][0]].append(i[ind])
                elif columns[ind][1] == "numeric":
                    data[columns[ind][0]].append(float(i[ind]))
                else:
                    data[columns[ind][0]].append(str(i[ind]))
                ind += 1

        data = pd.DataFrame(data, index=index)
        data.index.name = columns[0][0]
        return data

    def getStocks(self, exchange):
        cur = self.getCursor("masterdb")
        query = f"SELECT symbol from {exchange};"
        symbols = []
        cur.execute(query)
        for i in cur:
            symbols.append(i[0])
        return symbols

    def getStocksDataFrame(self, exchange, delta, backTestDays=504):
        """
        Returns Dictonary of pandas dataframe
        """
        symbols = self.getStocks(exchange)
        stocksDict = {}
        currentTime = datetime.now(tz=timezone.utc)
        for symbol in symbols:
            stocksDict[symbol] = self.getTableDaily(
                exchange,
                symbol,
                currentTime=currentTime,
                delta=delta,
                backTestDays=backTestDays,
            )


if __name__ == "__main__":
    a = databaseQueries()
    a.getStocksDataFrame("bse", 10)
