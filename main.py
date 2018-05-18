if __name__ == "__main__":
    import sys
    import MaxMaiCoin

    data = ""

    tradePlace = sys.argv[1]
    lookingDataType = sys.argv[2]

    Data = {
        "MaxMaiCoin" : lambda: MaxMaiCoin.router(lookingDataType),
    }.get(tradePlace, lambda: print('we do not have this trade place'))()

    print(Data)

    # python3 main.py MaxMaiCoin Tick