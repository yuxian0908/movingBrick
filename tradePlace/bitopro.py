import requests
import json
from decimal import Decimal
import time
import pyotp

def router(lookingDataType, lookingCoinType):
    Data = {
        "Tick" : lambda: Tick(lookingCoinType),
        "Bid"  : lambda: Bid(lookingCoinType),
        "Ask"  : lambda: Ask(lookingCoinType),
        "Volumns"  : lambda: Volumns(lookingCoinType),
    }.get(lookingDataType, lambda: print('we do not support this data type'))()
    return Data



def Tick(lookingCoinType):
    currentTime = int(time.time())
    beginTime = str(currentTime-1000)
    currentTime = str(currentTime)
    print(lookingCoinType)
    cookie = {}

    if lookingCoinType=="btc":
        #BTC
        cookie = {'session': '51731c9f09d1517e485bfc55696126d4'}
    elif lookingCoinType=="ltc":
        #LTC
        cookie = {'session': '6012a6d6586b0ae11feb20cec83a662d'}
    elif lookingCoinType=="eth":
        #ETH
        cookie = {'session': '5ef3f4f26870e21e53ad5674d475b444'}
    btcToTwd = requests.get("https://www.bitopro.com/trading_datas/history?symbol="+lookingCoinType+"&resolution=180&from="+beginTime+"&to="+currentTime,cookies=cookie)
    btcToTwd = json.loads(btcToTwd.text)

    return btcToTwd[0][4]


def Bid(lookingCoinType):
    currentTime = int(time.time())
    beginTime = str(currentTime-48000)
    currentTime = str(currentTime)
    btcToTwd = requests.get("https://www.bitopro.com/trading_datas/history?symbol=BTC&resolution=180&from="+beginTime+"&to="+currentTime)
    btcToTwd = json.loads(btcToTwd.text)
    for data in btcToTwd:
        print(data[4])
    return "not done yet"

def Ask(lookingCoinType):

    return "not done yet"

def Volumns(lookingCoinType):
    return "not done yet"