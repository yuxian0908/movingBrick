import requests
import json
from decimal import Decimal
from .tradePlace import tradePlace


class MaxMaiCoin(tradePlace):
    def __init__(self, lookingDataType, lookingCoinType):
        self.lookingDataType = lookingDataType
        self.lookingCoinType = lookingCoinType

    def router(self):
        Data = {
            "Tick" : lambda: self.Tick(),
            "Bid"  : lambda: self.Bid(),
            "Ask"  : lambda: self.Ask(),
            "Volumns"  : lambda: self.Volumns(),
        }.get(self.lookingDataType, lambda: print('we do not support this data type'))()
        return Data


    def Tick(self):
        btcToTwd = requests.get("https://api.maicoin.com/v1/prices/twd")
        returnData = ""

        def converseCoin(btcToCoin1,btcToCoin2):
            btcToCoin1Price = json.loads(btcToCoin1.text)['price']
            btcToCoin2Price = json.loads(btcToCoin2.text)['price']
            return Decimal(btcToCoin1Price)/Decimal(btcToCoin2Price)

        if self.lookingCoinType=="btc":
            dataObj = json.loads(btcToTwd.text)
            returnData = dataObj['price']
        elif self.lookingCoinType=="usdt":
            btcToUsd = requests.get("https://api.maicoin.com/v1/prices/usd")
            returnData = converseCoin(btcToTwd,btcToUsd)
        elif self.lookingCoinType=="eth":
            btcToEth = requests.get("https://api.maicoin.com/v1/prices/eth")
            returnData = converseCoin(btcToTwd,btcToEth)
        elif self.lookingCoinType=="ltc":
            btcToLtc = requests.get("https://api.maicoin.com/v1/prices/ltc")
            returnData = converseCoin(btcToTwd,btcToLtc)
        else:
            returnData = "we do not support this coin"

        return returnData


    def Bid(self):
        return "not done yet"

    def Ask(self):
        return "not done yet"

    def Volumns(self): 
        return "not done yet"