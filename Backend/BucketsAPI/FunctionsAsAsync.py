import os
import pickle


async def readFile(filePath):
    with open(filePath, "rb") as f:
        data = f.read()
        f.close()
    print(data)
    return data


async def generateReport_(contents):

    return "None"
