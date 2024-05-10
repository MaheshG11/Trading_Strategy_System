<h4><b>Note:</b>We prefer using Virtual environment everywhere and we will be using FastAPI throughout our backend (decided after several performance and usecase specific considerations).</h4>
<h2>Instructions to setup virtual environment</h2><br>

<h2>Follow these steps</h2><br><br>

1. Go to the API directory that you would like to work on 
    ```sh
    cd Trading_Strategy_System<directory_Name>
    ```
    example <directory_name> = User\ Operations\ API/
    <br>
2. Setup python virtual environment<br>
    Make sure you have installed virtual environment before you setup
     ```sh
    pip install virtualenv
    ```
    Refer <a href="https://docs.python.org/3/tutorial/venv.html"> this</a> to know how to setup and activate virtual environment<br>

3. Install the required packages for development
    ```sh
    python3 -m pip install -r requirements.txt
    ```
4. To run FastAPI use
    ```sh
    python3 main.py
    ```

5. After you have made some changes make sure you have updated requirements.txt for your edits just in case.
    ```sh
     pip3 freeze > requirements.txt
    ```
    <br>

Every API that you will see here will consists of a "requests and responses.md" file this will help you know what kind of requests the api is expecting on what address and what response it will give. 



