from abc import ABCMeta, abstractmethod

class tradePlace(metaclass = ABCMeta):
    
    @abstractmethod
    def router(self):
        pass

    @abstractmethod
    def Tick(self):
        pass

    @abstractmethod
    def Bid(self):
        pass

    @abstractmethod
    def Ask(self):
        pass

    @abstractmethod
    def Volumns(self): 
        pass