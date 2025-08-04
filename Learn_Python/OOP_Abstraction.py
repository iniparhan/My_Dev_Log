from abc import ABC, abstractmethod

'''
Bayar 10000 dengan OVO... Berhasil!
'''

class MetodePembayaran(ABC):
    @abstractmethod
    def proses_pembayaran(self, jumlah):
        pass

class OVO(MetodePembayaran):
    def proses_pembayaran(self, jumlah):
        print(f"Bayar {jumlah} dengan OVO... Berhasil!")

class GoPay(MetodePembayaran):
    def proses_pembayaran(self, jumlah):
        print(f"Bayar {jumlah} dengan GoPay... Berhasil!")

class ShopeePay(MetodePembayaran):
    def proses_pembayaran(self, jumlah):
        print(f"Bayar {jumlah} dengan ShopeePay... Berhasil!")

if __name__ == '__main__':
    bayar_ovo = OVO()
    bayar_gopay = GoPay()
    bayar_shopee = ShopeePay()

    bayar_ovo.proses_pembayaran(10000)
    bayar_gopay.proses_pembayaran(10000)
    bayar_shopee.proses_pembayaran(10000)
