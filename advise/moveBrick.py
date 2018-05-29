from decimal import Decimal
import sys

from tradePlace.MaxMaiCoin import MaxMaiCoin
from tradePlace.bitopro import bitopro

from tradePlace.binance import binance
from tradePlace.cex import cex
from tradePlace.HitBTC import HitBTC
from tradePlace.poloniex import poloniex
from tradePlace.bitfinex import bitfinex
from tradePlace.bittrex import bittrex


class moveBrick():
    def __init__(self):
        return
    
    def advise(self):
        localPlaces = ["MaxMaiCoin","bitopro"]
        abroadPlaces = ["binance","bitfinex","cex","HitBTC","poloniex","bittrex"]
        coinType = ["btc","ltc","eth"]
        arbType = ["localArbitrage", "abroadArbitrage"]
        dataTypes = "All"
        dataLen = 3

        arbTypeIndex = 0
        localPlaceIndex = 0
        abroadPlacesIndex = 0
        coinTypeIndex = 0
        dataIndex = 0

        resAry = []
        count = 0

        while(arbTypeIndex<len(arbType) and localPlaceIndex<len(localPlaces) and
            abroadPlacesIndex<len(abroadPlaces) and coinTypeIndex<len(coinType) and dataIndex<dataLen):
            res = {}
            count = count+1
            print(count)
            try:
                res = self._cpuArb(arbType[arbTypeIndex], localPlaces[localPlaceIndex], abroadPlaces[abroadPlacesIndex], dataTypes, coinType[coinTypeIndex], dataIndex)
            except KeyboardInterrupt:
                sys.exit()
            except:
                res = {}

            resAry.append(res)
            if arbTypeIndex<len(arbType)-1:
                arbTypeIndex = arbTypeIndex+1
            elif localPlaceIndex<len(localPlaces)-1:
                localPlaceIndex = localPlaceIndex+1
                arbTypeIndex = 0
            elif abroadPlacesIndex<len(abroadPlaces)-1:
                abroadPlacesIndex = abroadPlacesIndex+1
                arbTypeIndex = 0
                localPlaceIndex = 0
            elif coinTypeIndex<len(coinType):
                coinTypeIndex = coinTypeIndex+1
                arbTypeIndex = 0
                localPlaceIndex = 0
                abroadPlacesIndex = 0
            elif dataIndex<dataLen:
                dataIndex = dataIndex+1
                arbTypeIndex = 0
                localPlaceIndex = 0
                abroadPlacesIndex = 0
                coinTypeIndex = 0
            print(resAry)
        return resAry


    def _cpuArb(self, ArbType, localPlace, abroadPlace, lookingDataType, lookingCoinType, dataIndex):
        data = self._getData(localPlace,abroadPlace,lookingDataType,lookingCoinType)
        abroad = data['abroad']
        local = data['local']
        res = {'Arb': "false"}
        if(ArbType=="localArbitrage"):
            localArbitrage = (abroad[dataIndex]['bid']/local[dataIndex]['ask'])*Decimal(1.99)
            if localArbitrage>1.01:
                res = {
                    'Arb': "true",
                    'ArbRate': localArbitrage,
                    'from': localPlace,
                    'to': abroadPlace,
                    'coinType': lookingCoinType
                }
        elif(ArbType=="abroadArbitrage"):
            abroadArbitrage = (local[dataIndex]['bid']/abroad[dataIndex]['ask'])*Decimal(1.99)
            if abroadArbitrage>1.01:
                res = {
                    'Arb': "true",
                    'ArbRate': abroadArbitrage,
                    'from': abroadPlace,
                    'to': localPlace,
                    'coinType': lookingCoinType
                }
        return res

    def _getData(self,localPlace,abroadPlace,lookingDataType,lookingCoinType):
        lookingDataType = lookingDataType
        lookingCoinType = lookingCoinType
        local = {
            # local tradePlace
            "MaxMaiCoin" : lambda: MaxMaiCoin(lookingDataType,lookingCoinType).router(),
            "bitopro" : lambda: bitopro(lookingDataType,lookingCoinType).router(),
        }.get(localPlace, lambda: print('we do not support this trade place'))()

        abroad = {
            # abroad tradePlace
            "binance" : lambda: binance(lookingDataType,lookingCoinType).router(),
            "bitfinex" : lambda: bitfinex(lookingDataType,lookingCoinType).router(),
            "cex" : lambda: cex(lookingDataType,lookingCoinType).router(),
            "HitBTC" : lambda: HitBTC(lookingDataType,lookingCoinType).router(),
            "poloniex" : lambda: poloniex(lookingDataType,lookingCoinType).router(),
            "bittrex" : lambda: bittrex(lookingDataType,lookingCoinType).router(),
        }.get(abroadPlace, lambda: print('we do not support this trade place'))()

        res = {
            'local': local,
            'abroad': abroad
        }
        return res