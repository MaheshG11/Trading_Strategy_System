Note hostName and port will be there in the .env file so don't worry about it<br>

1. SignUp <br>
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
        a. signup successfull<br>
        b. User Already Exists<br>
        c. Unexpected Error Occurred <br>