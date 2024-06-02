import psycopg2
from connectDatabase import connectDatabase
import yfinance as yf
from datetime import date, timedelta, datetime


class schedules:

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
                return e
        return self.cur[dbName]

    def startQuaterlyScheduleFor(self, exchange: str, port: int):
        today = date.today()
        y1 = today - timedelta(days=1)
        y2 = today
        cur = self.getCursor("masterdb")
        exchange = ("_".join(exchange.split("."))).lower()
        query = f"SELECT symbol FROM {exchange};"
        cur.execute(query)
        symbols = cur.fetchall()
        conn.close()
        conn = connectDatabase.connect(exchange, port)
        cur = conn.cursor()
        i = 0
        n = len(symbols)
        data = (yf.Ticker(symbols[i][0])).history(start=y1, end=y2, interval="1d")
        data = data.iloc[0].name
        if str(data)[:10] != str(y1):
            print(
                f"The Exchange had holiday on {str(y1)} so we are aborting the operation"
            )
            return

        while i < n:
            symbol = symbols[i][0]
            data = yf.Ticker(symbol)
            data = (data.history(start=y1, end=y2, interval="1d")).iloc[0]
            symbol = ("_".join(symbol.split("."))).lower()
            j = 0
            query = f"""INSERT INTO {symbol} VALUES ('""" + str(data.name) + "'"
            while j < 7:
                query += "," + str(data.iloc[j])
                j += 1
            query += ");"
            i += 1
            cur.execute(query)

    def getStocks(self, exchange):
        cur = self.getCursor("masterdb")
        query = f"SELECT symbol from {exchange};"
        symbols = []
        cur.execute(query)
        for i in cur:
            symbols.append(i[0])
        return symbols

    def startDailyScheduleFor(self, ExchangeName):
        symbols = self.getStocks(exchange=ExchangeName)

        for symbol in symbols:
            stock = yf.Ticker(symbol)
            symbol = "_".join(symbol.split("."))
            query = f"""INSERT INTO {symbol}
                        VALUES  \n"""

            data = (stock.history(interval="1d", period="1d")).iloc[0]
            print(data)
            _ = "(DEFAULT,'" + str(data.name) + "'"
            j = 0
            m = len(data)
            while j < m:
                _ += "," + str(data.iloc[j])
                j += 1
            _ += "),\n"
            query += _
            query = query[:-2] + " ON CONFLICT DO NOTHING;"
            cur = self.getCursor(ExchangeName)
            cur.execute(query)
            return True


a = schedules()
a.startDailyScheduleFor("bse")
