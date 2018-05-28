from tradePlace.MaxMaiCoin import MaxMaiCoin
from tradePlace.bitopro import bitopro

from tradePlace.binance import binance
from tradePlace.cex import cex
from tradePlace.HitBTC import HitBTC
from tradePlace.poloniex import poloniex
from tradePlace.bitfinex import bitfinex
from tradePlace.bittrex import bittrex

from decimal import Decimal

class moveBrick():
    def __init__(self, local, abroad, lookingDataType, lookingCoinType):
        self.localPlace = local
        self.abroadPlace = abroad
        self.lookingDataType = lookingDataType
        self.lookingCoinType = lookingCoinType
        return
    
    def advise(self):
        lookingDataType = self.lookingDataType
        lookingCoinType = self.lookingCoinType
        local = {
            # local tradePlace
            "MaxMaiCoin" : lambda: MaxMaiCoin(lookingDataType,lookingCoinType).router(),
            "bitopro" : lambda: bitopro(lookingDataType,lookingCoinType).router(),
        }.get(self.localPlace, lambda: print('we do not support this trade place'))()

        abroad = {
            # abroad tradePlace
            "binance" : lambda: binance(lookingDataType,lookingCoinType).router(),
            "bitfinex" : lambda: bitfinex(lookingDataType,lookingCoinType).router(),
            "cex" : lambda: cex(lookingDataType,lookingCoinType).router(),
            "HitBTC" : lambda: HitBTC(lookingDataType,lookingCoinType).router(),
            "poloniex" : lambda: poloniex(lookingDataType,lookingCoinType).router(),
            "bittrex" : lambda: bittrex(lookingDataType,lookingCoinType).router(),
        }.get(self.abroadPlace, lambda: print('we do not support this trade place'))()

        localArbitrage = (abroad[0]['bid']/local[0]['ask'])*Decimal(0.99)
        abroadArbitrage = (local[0]['bid']/abroad[0]['ask'])*Decimal(0.99)

        if localArbitrage>1.01:
            print('local')
        if abroadArbitrage>1.01:
            print('abroad')
        
        return localArbitrage