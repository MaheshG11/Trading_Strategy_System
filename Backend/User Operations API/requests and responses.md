Note hostName and port will be there in the .env file so don't worry about it<br>

1. SignUp <br>
    request type : POST
    request url generalized
   ```sh
   http://<hostName>:<port>/signUp
   ```
   request url for development
   ```sh
   http://127.0.0.1:8081/signUp
   ```
    <br>
    request body:
     
    
        {
        "username": "String",
        "name": "string",
        "password": "string",
        "email": "string"
        }
    
    
    this data should be of <b>JSON</b> type<br>

    You can expect the following messages<br>
        a. {"message":"signup successfull"}<br>
        b. {"message": "User Already Exists"}<br>
        c. {"message":"Unexpected Error Occurred"} <br>


2. SignUp <br>
    request type : GET
    request url generalized
   ```sh
   http://<hostName>:<port>/login
   ```
   request url for development
   ```sh
   http://127.0.0.1:8081/login
   ```
    <br>
    request body:
     
    
        {
        "password": "string",
        "email": "string"
        }
    
    
    this data should be of <b>JSON</b> type<br>

    You can expect the following data from api<br>
        a. {"name":"name","email":"email","JWT": JWT_Token,"status": 200, "message":"login successful"}<br>
        b. {"status":401,"message":"Incorrect Password. Try Again."}<br>
        c. {"message":"Unexpected Error Occurred"} <br>
        
            
                