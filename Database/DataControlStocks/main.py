import yfinance as yf

k = yf.Ticker("TATAMOTORS.BO").history()
print(k)
