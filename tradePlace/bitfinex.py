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
        
        if self.lookingCoinType=="btc":
            btcToTwd = requests.get("https://api.bitfinex.com/v2/ticker/tBTCUSD")
            dataObj = json.loads(btcToTwd.text)
            returnData = Decimal(dataObj[6])*usdToTwd

        elif self.lookingCoinType=="eth":
            btcToEth = requests.get("https://api.bitfinex.com/v2/ticker/tETHUSD")
            dataObj = json.loads(btcToEth.text)
            returnData = Decimal(dataObj[6])*usdToTwd

        elif self.lookingCoinType=="ltc":
            btcToLtc = requests.get("https://api.bitfinex.com/v2/ticker/tLTCUSD")
            dataObj = json.loads(btcToLtc.text)
            returnData = Decimal(dataObj[6])*usdToTwd
        else:
            returnData = "we do not support this coin"

        return returnData


    def All(self):
        open('helper/bitoproCookies.txt', 'w').close()
        for index in ['1','2','3']:
            cookies_dict = ["1","2","2"]
            cookies_dict = json.dumps(cookies_dict)
            cookiefile = open('helper/bitoproCookies.txt', "a+")
            cookiefile.writelines(cookies_dict) 
            cookiefile.write("\n")
        return "test/"