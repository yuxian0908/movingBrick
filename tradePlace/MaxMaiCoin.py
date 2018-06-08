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
        URL = "https://max.maicoin.com/markets/btctwd"
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('--log-level=3')
        option.add_argument("--window-size=1296,696")
        browser = webdriver.Chrome(chrome_options=option)
        # browser = webdriver.Chrome()
        browser.get(URL)

        indexes = ["1","2","3"]
        index = ""
        if self.lookingCoinType=="btc":
            index = indexes[0]
        elif self.lookingCoinType=="ltc":
            index = indexes[2]
        elif self.lookingCoinType=="eth":
            index = indexes[1]
        apiData = browser.find_element_by_xpath(".//*[@id='market_list']//table[contains(@class, 'twd')]/tbody/tr["+index+"]/td[2]/span").text

        return apiData


    def All(self):        
        URL = "https://max.maicoin.com/markets/btctwd"
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('--log-level=3')
        option.add_argument("--window-size=1296,696")
        browser = webdriver.Chrome(chrome_options=option)
        # browser = webdriver.Chrome()
        browser.get(URL)

        indexes = ["1","2","3"]
        index = ""
        if self.lookingCoinType=="btc":
            index = indexes[0]
        elif self.lookingCoinType=="ltc":
            index = indexes[2]
        elif self.lookingCoinType=="eth":
            index = indexes[1]
        browser.find_element_by_xpath(".//*[@id='market_list']//table[contains(@class, 'twd')]/tbody/tr["+index+"]").click()

        trades = ["1","2","3","4","5"]
        results = list()
        
        for trade in trades:
            result = {
                'bid': Decimal(browser.find_element_by_xpath(".//*[@id='order_book_body']//table[contains(@class, 'bids')]/tbody/tr["+trade+"]/td[3]/div").text.replace(",","")),
                'ask': Decimal(browser.find_element_by_xpath(".//*[@id='order_book_body']//table[contains(@class, 'asks')]/tbody/tr["+trade+"]/td[1]/div").text.replace(",","")),
                'bidVolumns': Decimal(browser.find_element_by_xpath(".//*[@id='order_book_body']//table[contains(@class, 'bids')]/tbody/tr["+trade+"]/td[2]/div").text.replace(",","")),
                'askVolumns': Decimal(browser.find_element_by_xpath(".//*[@id='order_book_body']//table[contains(@class, 'asks')]/tbody/tr["+trade+"]/td[2]/div").text.replace(",","")),
            }
            results.append(result)

        returnData = results
        return returnData
        

