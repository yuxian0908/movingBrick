if __name__ == "__main__":
    import sys
    from tradePlace.MaxMaiCoin import MaxMaiCoin
    from tradePlace.bitopro import bitopro


    # test
    tradePlace = "bitopro"
    lookingDataType = "All"
    lookingCoinType = "btc"
    

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
        "bitopro" : lambda: bitopro(lookingDataType,lookingCoinType).router()

        # abroad tradePlace
    }.get(tradePlace, lambda: print('we do not support this trade place'))()

    print("==============================================")
    print("==============================================")
    print("==============================================")
    print("your data: ",Data)

   
