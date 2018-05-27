import requests
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
        return self.helper.getTick(self.lookingCoinType)


    def All(self):
        return self.helper.getBid(self.lookingCoinType)

    def login(self):
        helper = bitoproHelper()
        helper.login()
        return helper