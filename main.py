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

    # test
    tradePlace = "MaxMaiCoin"
    lookingDataType = "Tick"
    lookingCoinType = "ltc"
    
    # prod
    # print('enter the trading place')
    # tradePlace = input("input:")

    # print('enter what type of data you want to look up')
    # lookingDataType = input("input:")

    # print('enter what type of coin you want to look up')
    # lookingCoinType = input("input:")

    Data = {
        # local tradePlace
        "MaxMaiCoin" : lambda: MaxMaiCoin(lookingDataType,lookingCoinType).router(),
        "bitopro" : lambda: bitopro(lookingDataType,lookingCoinType).router(),

        # abroad tradePlace
        "binance" : lambda: binance(lookingDataType,lookingCoinType).router(),
        "bitfinex" : lambda: bitfinex(lookingDataType,lookingCoinType).router(),
        "cex" : lambda: cex(lookingDataType,lookingCoinType).router(),
        "HitBTC" : lambda: HitBTC(lookingDataType,lookingCoinType).router(),
        "poloniex" : lambda: poloniex(lookingDataType,lookingCoinType).router(),
        "bittrex" : lambda: bittrex(lookingDataType,lookingCoinType).router(),

        # advise 
        "advise" : lambda: moveBrick().advise()

    }.get(tradePlace, lambda: print('we do not support this trade place'))()

    print("==============================================")
    print("==============================================")
    print("==============================================")
    print("your data: ",Data)

   
