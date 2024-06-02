import psycopg2
from connectDatabase import connectDatabase
import yfinance as yf


class initializeDatabase:
    db: psycopg2.extensions.connection

    def __init__(self, port):
        self.db = connectDatabase.connect("masterdb", port)
        self.dbd = {}  # datatbase dict
        self.l = [
            "exchange",
            "currency",
            "symbol",
            "exchange",
            "industryKey",
            "sectorKey",
            "shortName",
            "timeZoneFullName",
            "timeZoneShortName",
            "auditRisk",
            "boardRisk",
            "compensationRisk",
            "shareHolderRightsRisk",
            "overallRisk",
            "governanceEpochDate",
            "compensationAsOfEpochDate",
            "dividendRate",
            "dividendYield",
            "exDividendDate",
            "payoutRatio",
            "fiveYearAvgDividendYield",
            "beta",
            "trailingPE",
            "forwardPE",
            "regularMarketVolume",
            "marketCap",
            "fiftyTwoWeekLow",
            "fiftyTwoWeekHigh",
            "priceToSalesTrailing12Months",
            "twoHundredDayAverage",
            "trailingAnnualDividendRate",
            "trailingAnnualDividendYield",
            "profitMargins",
            "sharesOutstanding",
            "heldPercentInsiders",
            "heldPercentInstitutions",
            "impliedSharesOutstanding",
            "bookValue",
            "priceToBook",
            "lastFiscalYearEnd",
            "nextFiscalYearEnd",
            "mostRecentQuarter",
            "earningsQuarterlyGrowth",
            "netIncomeToCommon",
            "trailingEps",
            "forwardEps",
            "lastSplitFactor",
            "lastSplitDate",
            "52WeekChange",
            "lastDividendValue",
            "lastDividendDate",
            "totalCash",
            "ebitda",
            "totalDebt",
            "quickRatio",
            "currentRatio",
            "totalRevenue",
            "debtToEquity",
            "returnOnAssets",
            "returnOnEquity",
            "freeCashflow",
            "operatingCashflow",
            "revenueGrowth",
            "grossMargins",
            "ebitdaMargins",
            "operatingMargins",
        ]

    def __del__(self):
        self.db.close()
        for i in self.dbd:
            self.dbd[i].close()

    def createMasterStockTable(
        self, exchangeName: str
    ):  # db = connectDatabase.connect("masterdb")
        query = f"""CREATE TABLE {exchangeName}(
            symbol VARCHAR(100) PRIMARY KEY,
            exchange VARCHAR(100),
            industryKey VARCHAR(100),
            sectorKey VARCHAR(100),
            shortName VARCHAR(100),
            timeZoneFullName VARCHAR(100),
            timeZoneShortName VARCHAR(100),
            auditRisk NUMERIC(23,9),
            boardRisk NUMERIC(23,9),
            compensationRisk NUMERIC(23,9),
            shareHolderRightsRisk NUMERIC(23,9),
            overallRisk NUMERIC(23,9),
            governanceEpochDate NUMERIC(23,9),
            compensationAsOfEpochDate NUMERIC(23,9),
            dividendRate NUMERIC(23),
            dividendYield NUMERIC(23),
            exDividendDate NUMERIC(23,9),
            payoutRatio NUMERIC(23),
            fiveYearAvgDividendYield NUMERIC(23),
            beta NUMERIC(23),
            trailingPE NUMERIC(23),
            forwardPE NUMERIC(23),
            regularMarketVolume NUMERIC(23,9),
            marketCap NUMERIC(23,9),
            fiftyTwoWeekLow NUMERIC(23),
            fiftyTwoWeekHigh NUMERIC(23),
            priceToSalesTrailing12Months NUMERIC(23),
            twoHundredDayAverage NUMERIC(23),
            trailingAnnualDividendRate NUMERIC(23),
            trailingAnnualDividendYield NUMERIC(23),
            profitMargins NUMERIC(23),
            sharesOutstanding NUMERIC(23,9),
            heldPercentInsiders NUMERIC(23),
            heldPercentInstitutions NUMERIC(23),
            impliedSharesOutstanding NUMERIC(23,9),
            bookValue NUMERIC(23),
            priceToBook NUMERIC(23),
            lastFiscalYearEnd NUMERIC(23,9),
            nextFiscalYearEnd NUMERIC(23,9),
            mostRecentQuarter NUMERIC(23,9),
            earningsQuarterlyGrowth NUMERIC(23),
            netIncomeToCommon NUMERIC(23,9),
            trailingEps NUMERIC(23),
            forwardEps NUMERIC(23),
            lastSplitFactor VARCHAR(100),
            lastSplitDate NUMERIC(23,9),
            f52WeekChange NUMERIC(23),
            lastDividendValue NUMERIC(23),
            lastDividendDate NUMERIC(23,9),
            totalCash NUMERIC(23,9),
            ebitda NUMERIC(23,9),
            totalDebt NUMERIC(23,9),
            quickRatio NUMERIC(23),
            currentRatio NUMERIC(23),
            totalRevenue NUMERIC(23,9),
            debtToEquity NUMERIC(23),
            returnOnAssets NUMERIC(23),
            returnOnEquity NUMERIC(23),
            freeCashflow NUMERIC(23,9),
            operatingCashflow NUMERIC(23,9),
            revenueGrowth NUMERIC(23),
            grossMargins NUMERIC(23),
            ebitdaMargins NUMERIC(23),
            operatingMargins NUMERIC(23));
            """

        try:
            cur = self.db.cursor()
            try:
                cur.execute(query)
            except:
                return True
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def createMasterTable(self):  # db = connectDatabase.connect("masterdb")
        query = """CREATE TABLE mastertable(
            exchange VARCHAR(100) PRIMARY KEY,
            currency VARCHAR(100)
            )"""
        try:
            cur = self.db.cursor()
            try:
                cur.execute(query)
                self.db.commit()
            except:

                return True

            return True
        except Exception as e:
            print(e)
            return False

    def createStockTable(self, symbol: str, db: psycopg2.extensions.connection):

        query = f"""CREATE TABLE {symbol}(
            id SERIAL PRIMARY KEY,
            date TIMESTAMPTZ NOT NULL UNIQUE,
            open NUMERIC(16,4),
            high NUMERIC(16,4),
            low NUMERIC(16,4),
            close NUMERIC(16,4),
            volume NUMERIC(22,0),
            Dividends NUMERIC(16,4),
            StockSplits NUMERIC(16,4));
            """
        try:
            cur = db.cursor()
            try:
                cur.execute(query)
                db.commit()
            except Exception as e:
                print(e)
                return db
            return db
        except Exception as e:
            print(e)
            return False

    def insertDataMasterTable(self, exchange: str, currency: str):
        query = f"""INSERT INTO mastertable
                    VALUES ('{exchange}','{currency}');
                """
        try:
            cur = self.db.cursor()
            try:
                cur.execute(query)
                self.db.commit()
            except Exception as e:
                print(e)
                return True

            return True
        except Exception as e:
            print(e)
            return False

    def insertDataMasterStockTable(self, symbol: str, port: int):  # masterdb
        """
        this function creates a entry of stock in masterdb's exchange table
        and then create a table in exchange's db by name of stock and inerts
        time series data of that stock in this table
        """
        stock = yf.Ticker(symbol)
        info = stock.info
        print(info)
        exchange = info[self.l[0]]

        if self.l[1] in info:
            temp = info[self.l[1]]
        else:
            temp = "NULL"
        if not self.insertDataMasterTable(exchange, temp):
            return False
        exchange = "_".join(exchange.split("."))
        exchange = exchange.lower()
        i = 3
        n = len(self.l)
        query = f"""INSERT INTO {exchange}
                    VALUES ('{symbol}',"""
        while i < n:
            try:
                s = info[self.l[i]]
            except:
                s = "NULL"
            if type(s) == str:
                if s == "NULL":
                    s += ","
                else:
                    s = "'" + str(s) + "',"
            else:
                s = str(s) + ","
            query += s
            i += 1
        query = query[:-1] + ");"

        if not self.createMasterStockTable(exchange):
            return False
        cur = self.db.cursor()
        try:
            cur.execute(
                f"""DELETE FROM {exchange}
                WHERE symbol='{symbol}';"""
            )
        except:
            pass
        try:
            cur.execute(query)

        except Exception as e:
            print(e)
            return False
        history = stock.history(interval="1d", period="max")
        n = len(history)

        i = 0
        m = 7
        if n == 0:
            try:
                cur.execute(
                    f"""DELETE FROM {exchange}
                    WHERE symbol='{symbol}';"""
                )
            except:
                return "Invalid Stock"

        symbol = "_".join(symbol.split("."))
        db: psycopg2.extensions.connection
        try:
            db = self.dbd[exchange]
        except Exception as e:
            try:
                db = connectDatabase.connect(exchange, port)
                self.dbd[exchange] = db

            except Exception as e:
                print(e)
        self.createStockTable(symbol, db)
        query = f"""INSERT INTO {symbol}
                    VALUES \n"""
        while i < n:
            k = history.iloc[i]

            _ = "(DEFAULT,'" + str(k.name) + "'"
            j = 0
            while j < m:
                _ += "," + str(k.iloc[j])
                j += 1
            _ += "),\n"
            query += _
            i += 1
        query = query[:-2] + " ON CONFLICT DO NOTHING;"
        cur = db.cursor()
        cur.execute(query)
        print("done")
        return True

    def insertMultipleStocks(self, symbols: list[str]):
        for i in symbols:
            self.insertDataMasterStockTable(i)


if __name__ == "__main__":
    a = initializeDatabase(5432)
    a.insertDataMasterStockTable("JPPOWER.BO", 5432)
    # def inizialize(port: int):
    #     l = []
    #     st = initializeDatabase(port)
    #     with open("listOfStocks", "r") as f:
    #         while True:
    #             a = f.readline()
    #             if len(a) == 0:
    #                 break
    #             l.append(a[0:-1])
    #     st.insertMultipleStocks(l)

    # inizialize(5432)
