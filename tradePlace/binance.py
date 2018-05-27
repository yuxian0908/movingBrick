import requests
import json
from decimal import Decimal

from .tradePlace import tradePlace

class binance(tradePlace):
    def __init__(self, lookingDataType, lookingCoinType):
        self.lookingDataType = lookingDataType
        self.lookingCoinType = lookingCoinType
 
    def router(self):
        Data = {
            "Tick" : lambda: self.Tick(),
            "All"  : lambda: self.All(),
        }.get(self.lookingDataType, lambda: print('we do not support this data type'))()
        return Data



    def Tick(self):
        def converseCoin(btcToCoin1,btcToCoin2):
            btcToCoin1Price = json.loads(btcToCoin1.text)['price']
            btcToCoin2Price = json.loads(btcToCoin2.text)['price']
            return Decimal(btcToCoin1Price)/Decimal(btcToCoin2Price)
        twd = requests.get("https://api.maicoin.com/v1/prices/twd")
        usd = requests.get("https://api.maicoin.com/v1/prices/usd")
        usdToTwd = converseCoin(twd,usd)

        if self.lookingCoinType=="btc":
            apiData = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
            dataObj = json.loads(apiData.text)
            returnData = Decimal(dataObj['price'])*usdToTwd

        elif self.lookingCoinType=="eth":
            apiData = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT")
            dataObj = json.loads(apiData.text)
            returnData = Decimal(dataObj['price'])*usdToTwd

        elif self.lookingCoinType=="ltc":
            apiData = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=LTCUSDT")
            dataObj = json.loads(apiData.text)
            returnData = Decimal(dataObj['price'])*usdToTwd

        else:
            returnData = "we do not support this coin"

        return returnData


    def All(self):
        def converseCoin(btcToCoin1,btcToCoin2):
            btcToCoin1Price = json.loads(btcToCoin1.text)['price']
            btcToCoin2Price = json.loads(btcToCoin2.text)['price']
            return Decimal(btcToCoin1Price)/Decimal(btcToCoin2Price)
        twd = requests.get("https://api.maicoin.com/v1/prices/twd")
        usd = requests.get("https://api.maicoin.com/v1/prices/usd")
        usdToTwd = converseCoin(twd,usd)
        apiData = ''

        if self.lookingCoinType=="btc":
            apiData = requests.get("https://api.binance.com/api/v1/depth?symbol=BTCUSDT&limit=5")

        elif self.lookingCoinType=="eth":
            apiData = requests.get("https://api.binance.com/api/v1/depth?symbol=ETHUSDT&limit=5")

        elif self.lookingCoinType=="ltc":
            apiData = requests.get("https://api.binance.com/api/v1/depth?symbol=LTCUSDT&limit=5")

        else:
            returnData = "we do not support this coin"


        dataObj = json.loads(apiData.text)
        results = list()
        for index in range(0,4):
            result = {
                'bid': Decimal(dataObj['bids'][index][0])*usdToTwd,
                'ask': Decimal(dataObj['asks'][index][0])*usdToTwd,
                'bidVolumns': dataObj['bids'][index][1],
                'askVolumns': dataObj['asks'][index][2]
            }
            results.append(result)
        returnData = results

        return returnData