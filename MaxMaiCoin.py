import requests
import json
from decimal import Decimal

def router(lookingDataType, lookingCoinType):
    Data = {
        "Tick" : lambda: Tick(lookingCoinType),
        "Bid"  : lambda: Bid(lookingCoinType),
        "Ask"  : lambda: Ask(lookingCoinType),
        "Volumns"  : lambda: Volumns(lookingCoinType),
    }.get(lookingDataType, lambda: print('we do not support this data type'))()
    return Data


def Tick(lookingCoinType):
    btcToTwd = requests.get("https://api.maicoin.com/v1/prices/twd")
    returnData = ""

    def converseCoin(btcToCoin1,btcToCoin2):
        btcToCoin1Price = json.loads(btcToCoin1.text)['price']
        btcToCoin2Price = json.loads(btcToCoin2.text)['price']
        return Decimal(btcToCoin1Price)/Decimal(btcToCoin2Price)

    if lookingCoinType=="btc":
        dataObj = json.loads(btcToTwd.text)
        returnData = dataObj['price']
    elif lookingCoinType=="usdt":
        btcToUsd = requests.get("https://api.maicoin.com/v1/prices/usd")
        returnData = converseCoin(btcToTwd,btcToUsd)
    elif lookingCoinType=="eth":
        btcToEth = requests.get("https://api.maicoin.com/v1/prices/eth")
        returnData = converseCoin(btcToTwd,btcToEth)
    elif lookingCoinType=="ltc":
        btcToLtc = requests.get("https://api.maicoin.com/v1/prices/ltc")
        returnData = converseCoin(btcToTwd,btcToLtc)
    else:
        returnData = "we do not support this coin"

    return returnData


def Bid(lookingCoinType):
    return "not done yet"

def Ask(lookingCoinType):
    return "not done yet"

def Volumns(lookingCoinType):
    return "not done yet"