from decimal import Decimal

def formula(target,base,charges,wantVolumn,dataIndex):
    return (target[dataIndex]['bid']/base[dataIndex]['ask'])*Decimal(0.99)-Decimal(charges)/Decimal(wantVolumn)

class fees:
    def __init__(self,tradePlace,lookingCoinType):
        self.tradePlace = tradePlace
        self.lookingCoinType = lookingCoinType
        return
    def routes(self, wantVolumn):
        Data = {
            "MaxMaiCoin" : lambda: self.MaxMaiCoin(),
            "bitopro" : lambda: self.bitopro(),
            "binance" : lambda: self.binance(),
            "bitfinex" : lambda: self.bitfinex(),
            "cex" : lambda: self.cex(),
            "HitBTC" : lambda: self.HitBTC(),
            "poloniex" : lambda: self.poloniex(),
            "bittrex" : lambda: self.bittrex(),
        }.get(self.tradePlace, lambda: print('we do not support this data type'))()
        return Data

    def MaxMaiCoin(self):
        fee = 0      
        if self.lookingCoinType=="btc":
            fee = 0.0005
        elif self.lookingCoinType=="ltc":
            fee = 0.01
        elif self.lookingCoinType=="eth":
            fee = 0.01
        return fee
        
    def bitopro(self):
        fee = 0      
        if self.lookingCoinType=="btc":
            fee = 0.0005
        elif self.lookingCoinType=="ltc":
            fee = 0.01
        elif self.lookingCoinType=="eth":
            fee = 0.01
        return fee
        
    def binance(self):  
        fee = 0      
        if self.lookingCoinType=="btc":
            fee = 0.0005
        elif self.lookingCoinType=="ltc":
            fee = 0.01
        elif self.lookingCoinType=="eth":
            fee = 0.01
        return fee

    def bitfinex(self):
        fee = 0      
        if self.lookingCoinType=="btc":
            fee = 0.0004
        elif self.lookingCoinType=="ltc":
            fee = 0.001
        elif self.lookingCoinType=="eth":
            fee = 0.0027 
        return fee

    # unknown
    def cex(self):
        fee = 0      
        if self.lookingCoinType=="btc":
            fee = 0.0005
        elif self.lookingCoinType=="ltc":
            fee = 0.01
        elif self.lookingCoinType=="eth":
            fee = 0.01
        return fee
        
    # unknown
    def HitBTC(self):
        fee = 0      
        if self.lookingCoinType=="btc":
            fee = 0.0005
        elif self.lookingCoinType=="ltc":
            fee = 0.01
        elif self.lookingCoinType=="eth":
            fee = 0.01
        return fee
        
    # unknown
    def poloniex(self):
        fee = 0      
        if self.lookingCoinType=="btc":
            fee = 0.0005
        elif self.lookingCoinType=="ltc":
            fee = 0.01
        elif self.lookingCoinType=="eth":
            fee = 0.01
        return fee
        
    # unknown
    def bittrex(self):
        fee = 0      
        if self.lookingCoinType=="btc":
            fee = 0.0005
        elif self.lookingCoinType=="ltc":
            fee = 0.01
        elif self.lookingCoinType=="eth":
            fee = 0.01
        return fee        