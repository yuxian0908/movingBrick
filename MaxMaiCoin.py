import requests
import json

def router(lookingDataType, lookingCoinType):
    Data = {
        "Tick" : lambda: Tick(lookingCoinType),
        "Bid"  : lambda: Bid(lookingCoinType),
        "Ask"  : lambda: Ask(lookingCoinType),
        "Volumns"  : lambda: Volumns(lookingCoinType),
    }.get(lookingDataType, lambda: print('we do not have this data type'))()
    return Data

def Tick(lookingCoinType):
    # it only support usd
    URL = "https://api.maicoin.com/v1/prices/"+lookingCoinType
    apiData = requests.get(URL)
    dataObj = json.loads(apiData.text)
    data = dataObj['price']

    return data

def Bid(lookingCoinType):
    return "not done yet"

def Ask(lookingCoinType):
    return "not done yet"

def Volumns(lookingCoinType):
    return "not done yet"