
import mysql.connector


# Database connection details (replace with your own)
password = '_Enter_your_password_here_1'
db_name = "StocksData"
user = "root"
host = "localhost"  # Use the service name here
port = 3307  # The NodePort you've exposed

try:
    connection = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        port=port,
        auth_plugin='mysql_native_password',
    )
    print("Connected successfully!")
    # Rest of your code here...
except mysql.connector.Error as err:
    print(f"Error: {err}")
