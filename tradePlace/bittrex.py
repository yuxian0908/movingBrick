import requests
import json
from decimal import Decimal

from .tradePlace import tradePlace

class bittrex(tradePlace):
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
            apiData = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=USDT-BTC')
        elif self.lookingCoinType=="eth":
            apiData = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=USDT-ETH')
        elif self.lookingCoinType=="ltc":
            apiData = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=USDT-LTC')
        else:
            return "we do not support this coin"

        dataObj = json.loads(apiData.text)['result']
        returnData = Decimal(dataObj['Last'])*self.usdToTwd()

        return returnData


    def All(self):

        if self.lookingCoinType=="btc":
            apiData = requests.get('https://bittrex.com/api/v1.1/public/getorderbook?market=USDT-BTC&type=both')

        elif self.lookingCoinType=="eth":
            apiData = requests.get('https://bittrex.com/api/v1.1/public/getorderbook?market=USDT-ETH&type=both')

        elif self.lookingCoinType=="ltc":
            apiData = requests.get('https://bittrex.com/api/v1.1/public/getorderbook?market=USDT-LTC&type=both')

        else:
            returnData = "we do not support this coin"


        dataObj = json.loads(apiData.text)['result']
        results = list()
        for index in range(0,4):
            result = {
                'bid': Decimal(dataObj['buy'][index]['Rate'])*self.usdToTwd(),
                'ask': Decimal(dataObj['sell'][index]['Rate'])*self.usdToTwd(),
                'bidVolumns': dataObj['buy'][index]['Quantity'],
                'askVolumns': dataObj['sell'][index]['Quantity']
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