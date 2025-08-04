class RekeningBank():
    def __init__(self, saldo):
        self.__saldo = saldo

    def setoran(self, setoran):
        self.__saldo += setoran
        
    def penarikan(self, penarikan):
        self.__saldo -= penarikan
        
    def getSaldo(self):
        return self.__saldo
    
    
if __name__ == '__main__':
    bank_parhan = RekeningBank(1000000)
    
    bank_parhan.setoran(100000)
    print(bank_parhan.getSaldo())
    bank_parhan.penarikan(50000)
    print(bank_parhan.getSaldo())
    
