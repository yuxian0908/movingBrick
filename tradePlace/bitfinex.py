import requests
import json
from decimal import Decimal

from .tradePlace import tradePlace

class bitfinex(tradePlace):
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
        
        apiData = ''
        if self.lookingCoinType=="btc":
            apiData = requests.get("https://api.bitfinex.com/v2/ticker/tBTCUSD")

        elif self.lookingCoinType=="eth":
            apiData = requests.get("https://api.bitfinex.com/v2/ticker/tETHUSD")

        elif self.lookingCoinType=="ltc":
            apiData = requests.get("https://api.bitfinex.com/v2/ticker/tLTCUSD")
        else:
            returnData = "we do not support this coin"

        dataObj = json.loads(apiData.text)
        returnData = Decimal(dataObj[6])*usdToTwd

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
            apiData = requests.get("https://api.bitfinex.com/v1/book/BTCUSD?limit_bids=5&limit_asks=5")

        elif self.lookingCoinType=="eth":
            apiData = requests.get("https://api.bitfinex.com/v1/book/ETHUSD?limit_bids=5&limit_asks=5")

        elif self.lookingCoinType=="ltc":
            apiData = requests.get("https://api.bitfinex.com/v1/book/LTCUSD?limit_bids=5&limit_asks=5")

        else:
            returnData = "we do not support this coin"


        dataObj = json.loads(apiData.text)
        results = list()
        for index in range(0,4):
            result = {
                'bid': Decimal(dataObj['bids'][index]['price'])*usdToTwd,
                'ask': Decimal(dataObj['asks'][index]['price'])*usdToTwd,
                'bidVolumns': dataObj['bids'][index]['amount'],
                'askVolumns': dataObj['asks'][index]['amount']
            }
            results.append(result)
        returnData = results
        
        return returnData