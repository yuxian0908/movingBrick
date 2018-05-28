import requests
import json
from decimal import Decimal

from .tradePlace import tradePlace

class poloniex(tradePlace):
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
        
        apiData = requests.get("https://poloniex.com/public?command=returnTicker")
        dataObj = json.loads(apiData.text)
        if self.lookingCoinType=="btc":
            dataObj = dataObj['USDT_BTC']

        elif self.lookingCoinType=="eth":
            dataObj = dataObj['USDT_ETH']

        elif self.lookingCoinType=="ltc":
            dataObj = dataObj['USDT_LTC']
        else:
            return "we do not support this coin"

        returnData = Decimal(dataObj['last'])*self.usdToTwd()

        return returnData


    def All(self):
        if self.lookingCoinType=="btc":
            apiData = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_BTC&depth=5")

        elif self.lookingCoinType=="eth":
            apiData = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_ETH&depth=5")

        elif self.lookingCoinType=="ltc":
            apiData = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_LTC&depth=5")

        else:
            returnData = "we do not support this coin"


        dataObj = json.loads(apiData.text)
        results = list()
        for index in range(0,4):
            result = {
                'bid': Decimal(dataObj['bids'][index][0])*self.usdToTwd(),
                'ask': Decimal(dataObj['asks'][index][0])*self.usdToTwd(),
                'bidVolumns': dataObj['bids'][index][1],
                'askVolumns': dataObj['asks'][index][1]
            }
            results.append(result)
        returnData = results
        
        return returnData



    def usdToTwd(self):
        def converseCoin(btcToCoin1,btcToCoin2):
            btcToCoin1Price = json.loads(btcToCoin1.text)['price']
            btcToCoin2Price = json.loads(btcToCoin2.text)['price']
            return Decimal(btcToCoin1Price)/Decimal(btcToCoin2Price)
        twd = requests.get("https://api.maicoin.com/v1/prices/twd")
        usd = requests.get("https://api.maicoin.com/v1/prices/usd")
        usdToTwd = converseCoin(twd,usd)
        return usdToTwd