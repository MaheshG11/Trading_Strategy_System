import csv
import mysql.connector
import os

# Database connection details (replace with your own)
password = '_Enter_your_password_here_1'
db_name = "StocksData"
user = "root"
host = "mysqlservice:3306"
if __name__=='__main__':
    connection = mysql.connector.connect(
        database=db_name, user=user, password=password, host=host,auth_plugin='mysql_native_password'
    )

    # Create a cursor object
    cursor = connection.cursor()
    stockName=input("Enter Company Name: ")
    cursor.execute(f"SELECT * FROM Stocks WHERE stock_name='{stockName.lower()}'")
    ticker=''
    id=0
    for i in cursor:
        ticker=i[1]
        id=i[0]
    print(f"The Ticker for the given stock is {ticker}\n")
    cursor.execute(f"SELECT * FROM StockPrice WHERE stocks_id={id}")
    filename=f'/home/mahesh/Current/Trading_Strategy_System/Database/data/{ticker}.csv'
    
    rows=[]
    cols=cursor.column_names
    print(cols)
    
    for i in cursor:
        if len(i)>0:
            rows.append(list(i))
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(cols)
        csvwriter.writerows(rows)
    
            
        
        
        
    