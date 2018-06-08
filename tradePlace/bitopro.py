import requests
from decimal import Decimal
import time
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import json

from .tradePlace import tradePlace
from helper.bitopro import bitoproHelper

class bitopro(tradePlace):
    def __init__(self, lookingDataType, lookingCoinType):
        self.lookingDataType = lookingDataType
        self.lookingCoinType = lookingCoinType
 
    def router(self):
        Data = {
            "Tick" : lambda: self.Tick(),
            "All"  : lambda: self.All(),
            "login" : lambda: self.login(),
        }.get(self.lookingDataType, lambda: print('we do not support this data type'))()
        return Data



    def Tick(self):
        URL = "https://www.bitopro.com/"
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('--log-level=3')
        option.add_argument("--window-size=1296,696")
        browser = webdriver.Chrome(chrome_options=option)
        # browser = webdriver.Chrome()
        browser.get(URL)
        browser.find_element_by_xpath(".//*[@id='section0']//div[contains(@class, 'welcome-btns')]/a[contains(@role, 'button')]").click()

        apiData = ""
        if self.lookingCoinType=="btc":
            apiData = browser.find_element_by_xpath(".//*[@id='crypto']//tbody/tr[2]/td[2]").text
        elif self.lookingCoinType=="ltc":
            apiData = browser.find_element_by_xpath(".//*[@id='crypto']//tbody/tr[3]/td[2]").text
        elif self.lookingCoinType=="eth":
            apiData = browser.find_element_by_xpath(".//*[@id='crypto']//tbody/tr[4]/td[2]").text
        return apiData

    def All(self):
        URL = "https://www.bitopro.com/"
        indexes = ["1","2","3"]
        if self.lookingCoinType=="btc":
            index = indexes[0]
        elif self.lookingCoinType=="ltc":
            index = indexes[1]
        elif self.lookingCoinType=="eth":
            index = indexes[2]
        

        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('--log-level=3')
        option.add_argument("--window-size=1296,696")
        browser = webdriver.Chrome(chrome_options=option)
        # browser = webdriver.Chrome()

        browser.implicitly_wait(30)
        browser.get(URL)

        # enter index page
        browser.find_element_by_xpath(".//*[@id='section0']//div[contains(@class, 'welcome-btns')]/a[contains(@role, 'button')]").click()

        # find the coin you are looking for
        browser.maximize_window()
        browser.find_element_by_xpath(".//*[@id='navbar']/ul/li[contains(@class, 'currency')]/a").click()
        time.sleep(0.5)
        browser.find_element_by_xpath(".//*[@id='navbar']/ul/li[contains(@class, 'currency')]/ul[contains(@role,'menu')]/*["+index+"]/a").click()
        
        # find the trade panel
        browser.find_element_by_xpath(".//*[@id='depth_tab']/a").click()
      
        trades = ["2","3","4","5","6"]
        results = list()
        
        for trade in trades:
            result = {
                'bid': Decimal(browser.find_element_by_xpath(".//*[@id='order_book']//ol[contains(@class, 'left')]/li["+trade+"]/span[4]").text.replace(",","")),
                'ask': Decimal(browser.find_element_by_xpath(".//*[@id='order_book']//ol[contains(@class, 'right')]/li["+trade+"]/span[1]").text.replace(",","")),
                'bidVolumns':Decimal(browser.find_element_by_xpath(".//*[@id='order_book']//ol[contains(@class, 'left')]/li["+trade+"]/span[2]").text.replace(",","")),
                'askVolumns': Decimal(browser.find_element_by_xpath(".//*[@id='order_book']//ol[contains(@class, 'right')]/li["+trade+"]/span[3]").text.replace(",","")),
            }
            results.append(result)

        returnData = results
        return returnData

    def login(self):
        helper = bitoproHelper()
        helper.login()
        return helper