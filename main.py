if __name__ == "__main__":
    import sys
    from tradePlace.MaxMaiCoin import MaxMaiCoin
    from tradePlace.bitopro import bitopro

    tradePlace = "MaxMaiCoin"
    lookingDataType = "All"
    lookingCoinType = "ltc"
    
    # print('enter the trading place')
    # tradePlace = input("input:")

    # print('enter what type of data you want to look up')
    # lookingDataType = input("input:")

    # print('enter what type of coin you want to look up')
    # lookingCoinType = input("input:")

    Data = {
        "MaxMaiCoin" : lambda: MaxMaiCoin(lookingDataType,lookingCoinType).router(),
        "bitopro" : lambda: bitopro(lookingDataType,lookingCoinType).router()

    }.get(tradePlace, lambda: print('we do not support this trade place'))()

    print("==============================================")
    print("==============================================")
    print("==============================================")
    print("your data: ",Data)

   
