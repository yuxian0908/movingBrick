if __name__ == "__main__":
    import sys
    from tradePlace.MaxMaiCoin import MaxMaiCoin
    from tradePlace.bitopro import bitopro
    from tradePlace.binance import binance
    from tradePlace.cex import cex
    from tradePlace.HitBTC import HitBTC
    from tradePlace.poloniex import poloniex
    from tradePlace.bitfinex import bitfinex
    from tradePlace.bittrex import bittrex

    from advise.moveBrick import moveBrick

    # for test
    lookup = "advise"
    localPlaces = ["MaxMaiCoin"]
    abroadPlaces = ["binance"]
    coinType = ["btc"]
    arbType = ["localArbitrage", "abroadArbitrage"]
    dataLen = 1

    # # for prod
    # lookup = "advise"
    # localPlaces = ["MaxMaiCoin","bitopro"]
    # abroadPlaces = ["binance","bitfinex","cex","HitBTC","poloniex","bittrex"]
    # coinType = ["btc","ltc","eth"]
    # arbType = ["localArbitrage", "abroadArbitrage"]
    # dataLen = 3 # 0~5


    # test for tradePlace
    # lookup = "MaxMaiCoin"
    # lookingDataType = "All"
    # lookingCoinType = "ltc"
    
    Data = {
        # # local tradePlace
        # "MaxMaiCoin" : lambda: MaxMaiCoin(lookingDataType,lookingCoinType).router(),
        # "bitopro" : lambda: bitopro(lookingDataType,lookingCoinType).router(),

        # # abroad tradePlace
        # "binance" : lambda: binance(lookingDataType,lookingCoinType).router(),
        # "bitfinex" : lambda: bitfinex(lookingDataType,lookingCoinType).router(),
        # "cex" : lambda: cex(lookingDataType,lookingCoinType).router(),
        # "HitBTC" : lambda: HitBTC(lookingDataType,lookingCoinType).router(),
        # "poloniex" : lambda: poloniex(lookingDataType,lookingCoinType).router(),
        # "bittrex" : lambda: bittrex(lookingDataType,lookingCoinType).router(),

        # advise 
        "advise" : lambda: moveBrick(localPlaces,abroadPlaces,coinType,arbType,dataLen).advise()

    }.get(lookup, lambda: print('we do not support this trade place'))()

    print("==============================================")
    print("==============================================")
    print("==============================================")
    print("your data: ",Data)

   
