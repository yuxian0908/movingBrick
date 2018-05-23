import requests
import json
from decimal import Decimal
import time
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib

from .tradePlace import tradePlace
from helper.bitopro import bitoproHelper

class bitopro(tradePlace):
    def __init__(self, lookingDataType, lookingCoinType):
        self.helper = self.login()
        self.lookingDataType = lookingDataType
        self.lookingCoinType = lookingCoinType
 
    def router(self):
        Data = {
            "Tick" : lambda: self.Tick(),
            "Bid"  : lambda: self.Bid(),
            "Ask"  : lambda: self.Ask(),
            "Volumns"  : lambda: self.Volumns(),
        }.get(self.lookingDataType, lambda: print('we do not support this data type'))()
        return Data



    def Tick(self):

        if self.lookingCoinType=="btc":
            return self.helper.getTick(self.lookingCoinType)
        elif self.lookingCoinType=="ltc":
            return "btcData"
        elif self.lookingCoinType=="eth":
            return "btcData"


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
        helper = bitoproHelper()
        helper.login()
        return helper