import csv
import mysql.connector
import os



# Database connection details (replace with your own)
password = password = '_Enter_your_password_here_1'
db_name = "StocksData"
user = "root"
host = "localhost"
port=30066

def add_columns(cursor : mysql.connector.cursor_cext.CMySQLCursor,attributes:list,datatypes:list,tablename:str):
    
    for i in range(len(attributes)):
        d= 'VARCHAR(40)' if datatypes[i]==str else 'DOUBLE'
        query=(f"ALTER TABLE {tablename} "
        f"ADD {attributes[i].lower()} {d}  DEFAULT {'' if datatypes[i]==str else 0};")
        cursor.execute(query)
        
def insert_data_from_csv(db_name, user, password, host, csv_file_path, ticker,companyName,port : int):
  t1="StockPrice"
  t2="Stocks"
  try:
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        port=port,
        auth_plugin='mysql_native_password',
    )

    # Create a cursor object
    cursor = connection.cursor()
    
    # Inserting New Stock Data
    try:
        addStock = (f"INSERT INTO {t2} "
               f"(name, stock_name) "
               "VALUES (%s, %s)")
        cursor.execute(addStock,(ticker,companyName.lower()))
    except: ''
    
    
    # Read the CSV file
    cursor.execute(f"Select ID from Stocks WHERE name= '{ticker}'")
    IDD=-1
    for i in cursor : 
        if IDD==-1 : IDD=i[0]
        else : continue
    with open(csv_file_path, "r") as csvfile:
      csv_reader = csv.reader(csvfile)

      # Get the header row (optional)
      header = next(csv_reader)
      datatypes=[]
      dateIND=-1
      for i in range(len(header)): 
          if header[i].lower()=='date':
              dateIND=i
              break
      for r in csv_reader:
          datatypes=r
          break
      for i in range(len(datatypes)): 
            
            try :
                datatypes[i]= type(float(datatypes[i]))
            except:
                datatypes[i]= type((datatypes[i]))
      
      # Adding columns if they do not exists in the database table
      cursor.execute("SELECT * FROM StockPrice WHERE id=1;")
      cols =set(cursor.column_names)
      for _ in cursor: pass
      attributes=[]
      dt=[]
      
      for i in range(len(header)):
          header[i]=header[i].lower()
          if header[i] not in cols: 
              attributes.append(header[i])
              dt.append(datatypes[i])
      if(len(attributes))>0:add_columns(cursor,attributes,dt,t1)
        
      header=','.join(header)+',stocks_id'
      # Prepare the INSERT SQL statement with placeholders for data
      insert_query = (f"INSERT INTO {t1} "
      f"({header}) "
      "VALUES (%s, %s,%s,%s,%s,%s,%s)")
      
      # Extracting column names
      
      
      

    #   Iterate over the CSV data and insert each row
      for row in csv_reader:
        r=row.copy()
        r.append(IDD)
        try:
            cursor.execute(insert_query, r)
            
        except:
            update=(f"UPDATE {t1} "
            f"({header}) "
            "VALUES (%s, %s,%s,%s,%s,%s,%s)"
            f"WHERE date={r[dateIND]} AND id={IDD}")

    # Commit the changes to the database
    connection.commit()

    print(f"Data inserted successfully into table {t1}")
    if connection:
      cursor.close()
      connection.close()


  except mysql.connector.Error as err:
    print(f"Error connecting to database: {err}")

  
    

# Call the function to insert data
if __name__=="__main__":
    
    csv_file_path = input("Enter CSV file path\n" )
    ticker=input("Enter Ticker Name\n")
    companyName= input("Enter Company Name\n")
    insert_data_from_csv(db_name, user, password, host, csv_file_path,ticker,companyName,port)
    
