if __name__ == "__main__":
    import sys
    import MaxMaiCoin

    # tradePlace = sys.argv[1]
    # lookingDataType = sys.argv[2]
    
    print('enter the trading place')
    tradePlace = input("input:")

    print('enter what type of data you want to look up')
    lookingDataType = input("input:")

    print('enter what type of coin you want to look up')
    lookingCoinType = input("input:")

    Data = {
        "MaxMaiCoin" : lambda: MaxMaiCoin.router(lookingDataType,lookingCoinType),

    }.get(tradePlace, lambda: print('we do not have this trade place'))()

    print(Data)

    # python3 main.py MaxMaiCoin Tick