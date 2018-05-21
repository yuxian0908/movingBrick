if __name__ == "__main__":
    import sys
    import tradePlace.MaxMaiCoin as MaxMaiCoin
    import tradePlace.bitopro as bitopro

    tradePlace = "bitopro"
    lookingDataType = "Ask"
    lookingCoinType = "ltc"
    
    # print('enter the trading place')
    # tradePlace = input("input:")

    # print('enter what type of data you want to look up')
    # lookingDataType = input("input:")

    # print('enter what type of coin you want to look up')
    # lookingCoinType = input("input:")

    Data = {
        "MaxMaiCoin" : lambda: MaxMaiCoin.router(lookingDataType,lookingCoinType),
        "bitopro" : lambda: bitopro.router(lookingDataType,lookingCoinType)

    }.get(tradePlace, lambda: print('we do not support this trade place'))()

    print("your data: ",Data)

   

    # test google authenticator
    def test():
        import time
        import pyotp
        totp = pyotp.TOTP("LNZREXIQXPNXUESK") 
        print(totp.now()) 
        print(totp.verify(totp.now()))
        totp.provisioning_uri("alice@google.com") 
    test()