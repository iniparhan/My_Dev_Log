'''
Mengirim email: Selamat datang!
Mengirim SMS: Selamat datang!
Mengirim push notification: Selamat datang!
'''

class Notifikasi:
    def __init__(self, pesan):
        self.pesan = pesan

    def kirim(self):
        print(self.pesan)
        
class Email(Notifikasi):
    def kirim(self):
        print("Mengirim email: " + self.pesan)

class SMS(Notifikasi):
    def kirim(self):
        print("Mengirim SMS: " + self.pesan)
        
class PushNotifikasi(Notifikasi):
    def kirim(self):
        print("Mengirim push notification: " + self.pesan)
        
def kirim_pesan_massal(pesan, daftar_notifikasi):
    for notifikasi in daftar_notifikasi:
        notifikasi = notifikasi(pesan)
        notifikasi.kirim()

if __name__ == '__main__':
    
    daftar_notifikasi = [Email, SMS, PushNotifikasi]
    kirim_pesan_massal("Selamat datang!", daftar_notifikasi)
    
