# IMPORTS
from fastapi import FastAPI
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from dataRetrival import stockRetrivals

load_dotenv()
# SETUP CONFIGURATION
app = FastAPI()
origins = [f'http://{os.getenv("frontendHost")}:{os.getenv("frontendPort")}']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/temp/{key}")
async def temp(key: str = 0):
    key = int(key)
    data = []
    with open(f"temp{key}.txt", "r") as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            line = line[:-2]
            line = line.split(":")
            line[0] = line[0][1:-2]
            line[1] = float(line[1])
            data.append({line[0]: line[1]})  # Use this to get dict
            # data.append(line) # Use this to get list
            # remember to restart once you change the configuration
    return {"status": 200, "plotThis": data}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=3000,
    )
