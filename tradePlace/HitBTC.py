import requests
import json
from decimal import Decimal

from .tradePlace import tradePlace

class HitBTC(tradePlace):
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

        apiData = ''
        if self.lookingCoinType=="btc":
            apiData = requests.get('https://api.hitbtc.com/api/2/public/ticker/BTCUSD')
        elif self.lookingCoinType=="eth":
            apiData = requests.get('https://api.hitbtc.com/api/2/public/ticker/ETHUSD')
        elif self.lookingCoinType=="ltc":
            apiData = requests.get('https://api.hitbtc.com/api/2/public/ticker/LTCUSD')
        else:
            return "we do not support this coin"

        dataObj = json.loads(apiData.text)
        returnData = Decimal(dataObj['last'])*self.usdToTwd()

        return returnData


    def All(self):

        if self.lookingCoinType=="btc":
            apiData = requests.get('https://api.hitbtc.com/api/2/public/orderbook/BTCUSD?limit=5')

        elif self.lookingCoinType=="eth":
            apiData = requests.get('https://api.hitbtc.com/api/2/public/orderbook/ETHUSD?limit=5')

        elif self.lookingCoinType=="ltc":
            apiData = requests.get('https://api.hitbtc.com/api/2/public/orderbook/LTCUSD?limit=5')

        else:
            returnData = "we do not support this coin"


        dataObj = json.loads(apiData.text)
        results = list()
        for index in range(0,4):
            result = {
                'bid': Decimal(dataObj['bid'][index]['price'])*self.usdToTwd(),
                'ask': Decimal(dataObj['ask'][index]['price'])*self.usdToTwd(),
                'bidVolumns': dataObj['bid'][index]['size'],
                'askVolumns': dataObj['ask'][index]['size']
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