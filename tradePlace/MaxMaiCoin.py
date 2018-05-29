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
        URL = "https://www.maicoin.com/zh-TW/charts"
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=option)
        # browser = webdriver.Chrome()
        browser.get(URL)
        cookies_list = browser.get_cookies()
        browser.close()
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']
        
        returnData = ""
        session = requests.Session() 
        if self.lookingCoinType=="btc":
            apiData = session.get("https://www.maicoin.com/api/prices/btc-twd",cookies=cookies_dict)
        elif self.lookingCoinType=="eth":
            apiData = session.get("https://www.maicoin.com/api/prices/eth-twd",cookies=cookies_dict)
        elif self.lookingCoinType=="ltc":
            apiData = session.get("https://www.maicoin.com/api/prices/ltc-twd",cookies=cookies_dict)
        else:
            returnData = "we do not support this coin"
        
        data = json.loads(apiData.content)
        returnData = data['formatted_price_in_twd']

        return returnData


    def All(self):        
        URL = "https://www.maicoin.com/zh-TW/charts"
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=option)
        # browser = webdriver.Chrome()
        browser.get(URL)
        cookies_list = browser.get_cookies()
        browser.close()
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']

        returnData = ""
        res = []
        session = requests.Session() 
        if self.lookingCoinType=="btc":
            apiData = session.get("https://www.maicoin.com/api/prices/btc-twd",cookies=cookies_dict)
        elif self.lookingCoinType=="eth":
            apiData = session.get("https://www.maicoin.com/api/prices/eth-twd",cookies=cookies_dict)
        elif self.lookingCoinType=="ltc":
            apiData = session.get("https://www.maicoin.com/api/prices/ltc-twd",cookies=cookies_dict)
        else:
            returnData = "we do not support this coin"
        
        data = json.loads(apiData.content)
        returnData = {
            'ask':Decimal(data['raw_buy_price_in_twd'])/Decimal(100000),
            'bid':Decimal(data['raw_sell_price_in_twd'])/Decimal(100000),
            'deal':Decimal(data['raw_price_in_twd'])/Decimal(100000)
        }
        res.append(returnData)
        return res
