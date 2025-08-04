class Pegawai():
    def __init__(self, nama, NIP):
        self.nama = nama
        self.NIP = NIP
        
    def tampilkan_info(self):
        print("Nama: ", self.nama)
        print("NIP: ", self.NIP)
        
class PegawaiTetap(Pegawai):
    def __init__(self, nama, NIP, gaji_bulanan):
        super().__init__(nama, NIP)
        self.gaji = gaji_bulanan
        
    def tampilkan_info(self):
        super().tampilkan_info()    
        print(f'Gaji Bulanan: Rp {self.gaji}')
    
class PegawaiMagang(Pegawai):
    def __init__(self, nama, NIP, gaji_per_jam, jumlah_jam):
        super().__init__(nama, NIP)
        self.gaji_per_jam = gaji_per_jam
        self.jumlah_jam = jumlah_jam
        
    def hitung_gaji(self):
        super().tampilkan_info()
        self.total = self.gaji_per_jam * self.jumlah_jam
        print(f'Gaji Magang: {self.gaji_per_jam} x {self.jumlah_jam} jam = {self.total}')

if __name__ == '__main__':
    budi = PegawaiTetap('Budi', '12345', 5000000)
    anton = PegawaiMagang('anton', '54321', 100000, 5)
    
    budi.tampilkan_info()
    print("\n")
    anton.hitung_gaji()
