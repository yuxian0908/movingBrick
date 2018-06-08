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
from helper.calculator import fees
from helper.calculator import formula


class moveBrick():
    def __init__(self,localPlaces,abroadPlaces,coinType,arbType,dataLen,volumn):
        self.localPlaces = localPlaces
        self.abroadPlaces = abroadPlaces
        self.coinType = coinType
        self.arbType = arbType
        self.dataLen = dataLen
        self.volumn = volumn
        return
    
    def advise(self):
        # init varibles
        localPlaces = self.localPlaces
        abroadPlaces = self.abroadPlaces
        coinType = self.coinType
        arbType = self.arbType
        dataLen = self.dataLen
        volumn = self.volumn
        dataTypes = "All"

        # iter seeds
        arbTypeIndex = 0
        localPlaceIndex = 0
        abroadPlacesIndex = 0
        coinTypeIndex = 0
        dataIndex = 0

        # resAry = []

        while(arbTypeIndex<len(arbType) and localPlaceIndex<len(localPlaces) and
            abroadPlacesIndex<len(abroadPlaces) and coinTypeIndex<len(coinType) and dataIndex<dataLen):
            res = {'Arb': "false"}
            try:
                res = self._cpuArb(arbType[arbTypeIndex], localPlaces[localPlaceIndex], abroadPlaces[abroadPlacesIndex], dataTypes, coinType[coinTypeIndex], dataIndex, volumn)
            except KeyboardInterrupt:
                sys.exit()
            except:
                print("Unexpected error:", sys.exc_info()[0])

            if(res['Arb']=="true"):
                print(res['coinType'],"可以套利")
                print("套利比例:",res['ArbRate'])
                print("從 ",res['from']," 搬運到 ",res['to'])
                print("此價格最多可以搬",res['volumnAval'])
            # resAry.append(res)

            # iterator seeds
            if dataIndex<dataLen-1:
                dataIndex = dataIndex+1
            elif arbTypeIndex<len(arbType)-1:
                arbTypeIndex = arbTypeIndex+1
                dataIndex = 0
            elif localPlaceIndex<len(localPlaces)-1:
                localPlaceIndex = localPlaceIndex+1
                dataIndex = 0
                arbTypeIndex = 0
            elif abroadPlacesIndex<len(abroadPlaces)-1:
                abroadPlacesIndex = abroadPlacesIndex+1
                dataIndex = 0
                arbTypeIndex = 0
                localPlaceIndex = 0
            elif coinTypeIndex<len(coinType):
                coinTypeIndex = coinTypeIndex+1
                dataIndex = 0
                arbTypeIndex = 0
                localPlaceIndex = 0
                abroadPlacesIndex = 0
        # return resAry
        return "end"

    def _cpuArb(self, ArbType, localPlace, abroadPlace, lookingDataType, lookingCoinType, dataIndex, wantVolumn):
        data = self._getData(localPlace,abroadPlace,lookingDataType,lookingCoinType)
        abroad = data['abroad']
        local = data['local']
        res = {'Arb': "false"}
        charges = fees(abroadPlace,lookingCoinType).routes(wantVolumn)

        def culArb(base,target):
            # find volumn for each trade
            volumnSum = float(0)
            count = 0
            while(count<=dataIndex):
                count+=1
                volumnSum = volumnSum + float(target[count]['bidVolumns'])
            # make sure volumn is enough
            Arbitrage = 0
            if volumnSum > wantVolumn:
                Arbitrage = formula(target,base,charges,wantVolumn,dataIndex)

            return {
                'rate': Arbitrage,
                'volumnSum': volumnSum
            }

        if(ArbType=="localArbitrage"):
            localData = culArb(local,abroad)
            localArbitrage = localData['rate']
            # determin whether the rate is enough
            if localArbitrage>1.01:
                res = {
                    'Arb': "true",
                    'ArbRate': localArbitrage,
                    'from': localPlace,
                    'to': abroadPlace,
                    'coinType': lookingCoinType,
                    'volumnAval': localData['volumnSum']
                }

        elif(ArbType=="abroadArbitrage"):
            abroadData = culArb(local,abroad)
            abroadArbitrage = abroadData['rate']
            # determin whether the rate is enough
            if abroadArbitrage>1.01:
                res = {
                    'Arb': "true",
                    'ArbRate': abroadArbitrage,
                    'from': abroadPlace,
                    'to': localPlace,
                    'coinType': lookingCoinType,
                    'volumnAval': abroadData['volumnSum']
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