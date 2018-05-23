import requests
import json
from decimal import Decimal
import time
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib

from .tradePlace import tradePlace
import helper.bitopro as helper

class bitopro(tradePlace):
    def __init__(self, lookingDataType, lookingCoinType):
        self.lookingDataType = lookingDataType
        self.lookingCoinType = lookingCoinType
 
    def router(self):
        self.browser = self.login()
        Data = {
            "Tick" : lambda: self.Tick(),
            "Bid"  : lambda: self.Bid(),
            "Ask"  : lambda: self.Ask(),
            "Volumns"  : lambda: self.Volumns(),
        }.get(self.lookingDataType, lambda: print('we do not support this data type'))()
        return Data



    def Tick(self):
        currentTime = int(time.time())
        beginTime = str(currentTime-1000)
        currentTime = str(currentTime)
        cookie = {}

        session = requests.Session()

        if self.lookingCoinType=="btc":
            #BTC
            cookie = {'session': '51731c9f09d1517e485bfc55696126d4'}
        elif self.lookingCoinType=="ltc":
            #LTC
            cookie = {'session': '6012a6d6586b0ae11feb20cec83a662d'}
        elif self.lookingCoinType=="eth":
            #ETH
            cookie = {'session': '5ef3f4f26870e21e53ad5674d475b444'}

        btcToTwd = session.get("https://www.bitopro.com/trading_datas/history?symbol="+
                                    self.lookingCoinType+"&resolution=180&from="+
                                    beginTime+"&to="+currentTime,cookies=cookie)
        btcToTwd = json.loads(btcToTwd.text)

        return btcToTwd[0][4]


    def Bid(self):
        currentTime = int(time.time())
        beginTime = str(currentTime-48000)
        currentTime = str(currentTime)
        btcToTwd = requests.get("https://www.bitopro.com/trading_datas/history?symbol=BTC&resolution=180&from="+beginTime+"&to="+currentTime)
        btcToTwd = json.loads(btcToTwd.text)
        for data in btcToTwd:
            print(data[4])
        return "not done yet"

    def Ask(self):

        return "not done yet"

    def Volumns(self):
        return "not done yet"


    def login(self):
        return helper.login()