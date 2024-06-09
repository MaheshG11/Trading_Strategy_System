import os
import pickle


async def readFile(filePath):
    with open(os.path.join("output/", filePath), "rb") as f:
        data = pickle.load(f)
        f.close()
    print(data)
    return data
