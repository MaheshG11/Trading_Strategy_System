import psycopg2
from connectDatabase import connectDatabase
import yfinance as yf
from datetime import date, timedelta


def startScheduleFor(exchange: str, port: int):
    today = date.today()
    y1 = today - timedelta(days=1)
    y2 = today
    conn: psycopg2.extensions.connection
    conn = connectDatabase.connect("masterdb", port)
    cur = conn.cursor()
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
        print(f"The Exchange had holiday on {str(y1)} so we are aborting the operation")
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

    conn.commit()
    conn.close()
