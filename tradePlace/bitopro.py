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
        # use request to get data
        cookies = open('helper/bitoproCookies.txt', "r")
        cookiesAry = cookies.readlines()

        if self.lookingCoinType=="btc":
            cookies_dict = cookiesAry[0]
            cookies_dict = json.loads(cookies_dict)['1']
        elif self.lookingCoinType=="ltc":
            cookies_dict = cookiesAry[1]
            cookies_dict = json.loads(cookies_dict)['2']
        elif self.lookingCoinType=="eth":
            cookies_dict = cookiesAry[2]
            cookies_dict = json.loads(cookies_dict)['3']


        currentTime = int(time.time())
        beginTime = str(currentTime-1000)
        currentTime = str(currentTime)
        apiData = requests.get("https://www.bitopro.com/trading_datas/history?resolution=180&from="+beginTime+"&to="+currentTime, cookies=cookies_dict)
        apiData = json.loads(apiData.text)
        return apiData[0][4]


    def All(self):
        # use request to get data
        cookies = open('helper/bitoproCookies.txt', "r")
        cookiesAry = cookies.readlines()

        if self.lookingCoinType=="btc":
            cookies_dict = cookiesAry[0]
            cookies_dict = json.loads(cookies_dict)['1']
        elif self.lookingCoinType=="ltc":
            cookies_dict = cookiesAry[1]
            cookies_dict = json.loads(cookies_dict)['2']
        elif self.lookingCoinType=="eth":
            cookies_dict = cookiesAry[2]
            cookies_dict = json.loads(cookies_dict)['3']


        currentTime = int(time.time())
        beginTime = str(currentTime-48000)
        currentTime = str(currentTime)
        apiData = requests.get("https://www.bitopro.com/trading_datas/history?resolution=180&from="+beginTime+"&to="+currentTime, cookies=cookies_dict)
        apiData = json.loads(apiData.text)
        
        results = list()
        
        for data in apiData:
            result = {
                'bid': data[1],
                'ask': data[2],
                'deal': data[4],
                'volumns': data[5]
            }
            results.append(result)
        return results

    def login(self):
        helper = bitoproHelper()
        helper.login()
        return helper