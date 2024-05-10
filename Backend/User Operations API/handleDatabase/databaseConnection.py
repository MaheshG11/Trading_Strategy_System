import mysql.connector
class mysqlOps:
    # Database connection details (replace with your own)
    # Enter your MysqlDB password here
    
      # Use the service name here
      # The NodePort you've exposed

    conn={}
    def connect(self,database_name:str):
        try:
            connection = mysql.connector.connect(
            database=database_name,
            user="root",
            password="Password123@",
            host="localhost",
            port=3306,
            auth_plugin='mysql_native_password',
            )
            print("Connected successfully!",connection)
            if(connection==None):
                return f'Error connecting to postgreSQL {database_name} database'
            else : 
                self.conn[database_name]=connection
                return f'successfully connected to {database_name} database access mysqlOps.conn[{database_name}] to get the connection'
    # Rest of your code here...
        except mysql.connector.Error as err:
            print(f"Error: {err}")
                
    
        
        
        

mysq=mysqlOps()
mysq.connect("users")
print(mysq.conn)


        
    
#print(type(conn)) = psycopg2.extensions.connection
