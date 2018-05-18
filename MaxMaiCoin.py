import requests
import json

def router(lookingDataType):
    Data = {
        "Tick" : lambda: Tick(),
        "Bid"  : lambda: Bid(),
        "Ask"  : lambda: Ask(),
        "Volumns"  : lambda: Volumns(),
    }.get(lookingDataType, lambda: print('E'))()
    return Data

def Tick():
    # it only support usd
    URL = "https://api.maicoin.com/v1/prices/usd"
    apiData = requests.get(URL)
    dataObj = json.loads(apiData.text)
    data = {
        'USD':dataObj['price'],
    }

    return data

def Bid():
    return "not done yet"

def Ask():
    return "not done yet"

def Volumns():
    return "not done yet"