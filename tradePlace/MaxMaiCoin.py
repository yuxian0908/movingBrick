import requests
import json
from decimal import Decimal
from .tradePlace import tradePlace
from pyquery import PyQuery
from selenium import webdriver


class MaxMaiCoin(tradePlace):
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


    def All(self):
        URL = "https://www.maicoin.com/zh-TW/charts"
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=option)
        browser.get(URL)
        cookies_list = browser.get_cookies()
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']
            

        def converseCoin(btcToCoin1,btcToCoin2):
            btcToCoin1Price = json.loads(btcToCoin1.text)['price']
            btcToCoin2Price = json.loads(btcToCoin2.text)['price']
            return Decimal(btcToCoin1Price)/Decimal(btcToCoin2Price)

        returnData = ""
        if self.lookingCoinType=="btc":
            session = requests.Session() 
            btcToTwd = session.get("https://www.maicoin.com/api/prices/btc-twd",cookies=cookies_dict)
            data = json.loads(btcToTwd.content)
            returnData = {
                'ask':data['raw_buy_price'],
                'bid':data['raw_sell_price'],
                'deal':data['raw_price']
            }


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
