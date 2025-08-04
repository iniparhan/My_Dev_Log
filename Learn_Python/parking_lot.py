class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = {'username': 'cakboyo', 'password': 'pangerantampan'}
        self.is_login = False

    def login(self):
        if self.data['username'] == self.username and self.data['password'] == self.password:
            self.is_login = True
        else:
            self.is_login = False
        return self.is_login


class ParkingLot:
    def __init__(self, jenis_kendaraan=None, plat_nomor=None):
        self.jenis_kendaraan = jenis_kendaraan
        self.plat_nomor = plat_nomor

        self.koordinat_row = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.koordinat_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        self.isi_parkiran_lantai_1 = {}
        self.slot_parkiran_lantai_1 = {'motor': 30, 'mobil': 60}
        self.isi_parkiran_lantai_2 = {}
        self.slot_parkiran_lantai_2 = {'motor': 27, 'mobil': 63}
        self.isi_parkiran_lantai_3 = {}
        self.slot_parkiran_lantai_3 = {'motor': 30, 'mobil': 42, 'bus': 18}

    def koordinat_parkiran(self):
        '''
        Fungsi untuk menghasilkan koordinat parkiran
        
        karena slotnya banyak, aku ngakalin dengan membuat looping per koordinat-nya
        '''
        
        koordinat = []
        for row in self.koordinat_row:
            for column in self.koordinat_column:
                koordinat.append(f'{column}{row}')
        return koordinat

    def parkir_lantai_1(self):
        '''
        Denah parkir lantai 1
        
        - karena setiap lantai slot denahnya berbeda, aku ngakalin juga dengan looping sesuai dengan jenis kendaraan yang dapat ditampung
        - lalu setelah itu, mencari koordinat yang kosong, dan kemudian memasukkan slot yang kosong, plat nomor dan jenis kendaraannya
        '''
        
        koordinat = self.koordinat_parkiran()
        list_slot_parkir_motor = [f'{column}{row}' for row in range(3) for column in self.koordinat_column]
        list_slot_parkir_mobil = [slot for slot in koordinat if slot not in list_slot_parkir_motor]

        if self.jenis_kendaraan == 'motor' and self.slot_parkiran_lantai_1['motor'] > 0:
            for slot in list_slot_parkir_motor:
                if slot not in self.isi_parkiran_lantai_1:
                    self.isi_parkiran_lantai_1[slot] = [self.plat_nomor, self.jenis_kendaraan]
                    self.slot_parkiran_lantai_1['motor'] -= 1
                    break

        elif self.jenis_kendaraan == 'mobil' and self.slot_parkiran_lantai_1['mobil'] > 0:
            for slot in list_slot_parkir_mobil:
                if slot not in self.isi_parkiran_lantai_1:
                    self.isi_parkiran_lantai_1[slot] = [self.plat_nomor, self.jenis_kendaraan]
                    self.slot_parkiran_lantai_1['mobil'] -= 1
                    break
        else:
            print('Parkiran Penuh!!!')

    def parkir_lantai_2(self):
        '''
        Denah parkir lantai 2
        
        - karena setiap lantai slot denahnya berbeda, aku ngakalin juga dengan looping sesuai dengan jenis kendaraan yang dapat ditampung
        - lalu setelah itu, mencari koordinat yang kosong, dan kemudian memasukkan slot yang kosong, plat nomor dan jenis kendaraannya
        '''
        
        koordinat = self.koordinat_parkiran()
        list_slot_parkir_motor = [f'{column}{row}' for row in range(9) for column in ['A', 'B', 'C']]
        list_slot_parkir_mobil = [slot for slot in koordinat if slot not in list_slot_parkir_motor]

        if self.jenis_kendaraan == 'motor' and self.slot_parkiran_lantai_2['motor'] > 0:
            for slot in list_slot_parkir_motor:
                if slot not in self.isi_parkiran_lantai_2:
                    self.isi_parkiran_lantai_2[slot] = [self.plat_nomor, self.jenis_kendaraan]
                    self.slot_parkiran_lantai_2['motor'] -= 1
                    break

        elif self.jenis_kendaraan == 'mobil' and self.slot_parkiran_lantai_2['mobil'] > 0:
            for slot in list_slot_parkir_mobil:
                if slot not in self.isi_parkiran_lantai_2:
                    self.isi_parkiran_lantai_2[slot] = [self.plat_nomor, self.jenis_kendaraan]
                    self.slot_parkiran_lantai_2['mobil'] -= 1
                    break
        else:
            print('Parkiran Penuh!!!')

    def parkir_lantai_3(self):
        '''
        Denah parkir lantai 3
        
        - karena setiap lantai slot denahnya berbeda, aku ngakalin juga dengan looping sesuai dengan jenis kendaraan yang dapat ditampung
        - lalu setelah itu, mencari koordinat yang kosong, dan kemudian memasukkan slot yang kosong, plat nomor dan jenis kendaraannya
        '''
        
        koordinat = self.koordinat_parkiran()
        list_slot_parkir_motor = [f'{column}{row}' for row in range(6, 9) for column in self.koordinat_column]
        list_slot_parkir_bus = [f'{column}{row}' for row in range(0, 6) for column in ['H', 'I', 'J']]
        list_slot_parkir_mobil = [slot for slot in koordinat if slot not in list_slot_parkir_motor and slot not in list_slot_parkir_bus]

        if self.jenis_kendaraan == 'motor' and self.slot_parkiran_lantai_3['motor'] > 0:
            for slot in list_slot_parkir_motor:
                if slot not in self.isi_parkiran_lantai_3:
                    self.isi_parkiran_lantai_3[slot] = [self.plat_nomor, self.jenis_kendaraan]
                    self.slot_parkiran_lantai_3['motor'] -= 1
                    break

        elif self.jenis_kendaraan == 'mobil' and self.slot_parkiran_lantai_3['mobil'] > 0:
            for slot in list_slot_parkir_mobil:
                if slot not in self.isi_parkiran_lantai_3:
                    self.isi_parkiran_lantai_3[slot] = [self.plat_nomor, self.jenis_kendaraan]
                    self.slot_parkiran_lantai_3['mobil'] -= 1
                    break

        elif self.jenis_kendaraan == 'bus' and self.slot_parkiran_lantai_3['bus'] > 0:
            for slot in list_slot_parkir_bus:
                if slot not in self.isi_parkiran_lantai_3:
                    self.isi_parkiran_lantai_3[slot] = [self.plat_nomor, self.jenis_kendaraan]
                    self.slot_parkiran_lantai_3['bus'] -= 1
                    break
        else:
            print('Parkiran Penuh!!!')

    def cek_posisi_kendaraan(self):
        '''
        Cek posisi kendaraan
        
        Cuma sebagai pengecekan posisi kendaraan pada setiap lantainya    
        '''
    
        print('Pilih Lokasi:')
        pilihan = input('1. Lantai 1\n2. Lantai 2\n3. Lantai 3\nMasukkan Pilihan: ')

        if pilihan == '1':
            print('Lantai 1:')
            for lokasi, data in self.isi_parkiran_lantai_1.items():
                print(f'{lokasi}: {data[0]} ({data[1]})')
        elif pilihan == '2':
            print('Lantai 2:')
            for lokasi, data in self.isi_parkiran_lantai_2.items():
                print(f'{lokasi}: {data[0]} ({data[1]})')
        elif pilihan == '3':
            print('Lantai 3:')
            for lokasi, data in self.isi_parkiran_lantai_3.items():
                print(f'{lokasi}: {data[0]} ({data[1]})')
        else:
            print('Pilihan Tidak Tersedia')

    def total_semua_kendaraan(self):
        '''
        Total semua kendaraan
        
        kalau ini cuma untuk melihat total semua kendaraan
        '''
        
        total = len(self.isi_parkiran_lantai_1) + \
                len(self.isi_parkiran_lantai_2) + \
                len(self.isi_parkiran_lantai_3)
        print(f"Total semua kendaraan yang parkir: {total}")
        return total

    def total_pendapatan(self):
        '''
        Total Pendapatan
    
        Total pendapatan sesuai dengan tarif setiap kendaraan
        '''
        
        MOTOR = 2000
        MOBIL = 5000
        BUS = 10000

        total = 0
        semua_lantai = [
            self.isi_parkiran_lantai_1,
            self.isi_parkiran_lantai_2,
            self.isi_parkiran_lantai_3
        ]

        for lantai in semua_lantai:
            for data in lantai.values():
                jenis = data[1]
                if jenis == 'motor':
                    total += MOTOR
                elif jenis == 'mobil':
                    total += MOBIL
                elif jenis == 'bus':
                    total += BUS

        print(f"Pendapatan total saat ini: Rp {total:,}")
        return total

    def cek_ketersediaan_parkiran_setiap_jenis_kendaraan(self):
        '''
        Cek ketersediaan parkiran setiap jenis kendaraan
        '''
        print("Ketersediaan Parkiran:")
        print(f"Motor - Lantai 1: {self.slot_parkiran_lantai_1['motor']} slot")
        print(f"Motor - Lantai 2: {self.slot_parkiran_lantai_2['motor']} slot")
        print(f"Motor - Lantai 3: {self.slot_parkiran_lantai_3['motor']} slot")
        print(f"Mobil - Lantai 1: {self.slot_parkiran_lantai_1['mobil']} slot")
        print(f"Mobil - Lantai 2: {self.slot_parkiran_lantai_2['mobil']} slot")
        print(f"Mobil - Lantai 3: {self.slot_parkiran_lantai_3['mobil']} slot")
        print(f"Bus   - Lantai 3: {self.slot_parkiran_lantai_3['bus']} slot")



# =======================
#        MAIN CODE
# =======================

if __name__ == "__main__":

    # =================
    # Cek login
    # =================
    
    username = 'cakboyo'
    password = 'pangerantampan'
    
    login = Login(username, password)
    
    if login.login():
        print('Login Berhasil\n')
        isLogin = True
    else:
        print('Login Gagal, periksa kembali username dan password\n')
        isLogin = False
    
    # =================
    # global variable
    # =================
    parkiran = ParkingLot()
    
    # =================
    # Loop Program Utama
    # =================
    
    while isLogin:
        print('='*50)
        print('Selamat Datang Di Parkir Pilih Menu Berikut')
        print('='*50)
    
        pilihan = input('1. Parkir Kendaraan\n2. Laporan\n3. Keluar\nMasukkan Pilihan: ')
    
        if pilihan == '1':
            jenis_kendaraan = input('\nMasukkan Jenis Kendaraan \n1. motor\n2. mobil\n3. bus\nMasukkan Pilihan: ')
            plat_nomor = input('Masukkan Plat Nomor Kendaraan: ')
    
            if jenis_kendaraan == '1':
                jenis_kendaraan = 'motor'
                parkiran.jenis_kendaraan = jenis_kendaraan
                parkiran.plat_nomor = plat_nomor
    
                if parkiran.slot_parkiran_lantai_1['motor'] > 0:
                    parkiran.parkir_lantai_1()
                    print(f'{jenis_kendaraan} diparkir di lantai 1')
                elif parkiran.slot_parkiran_lantai_2['motor'] > 0:
                    parkiran.parkir_lantai_2()
                    print(f'{jenis_kendaraan} diparkir di lantai 2')
                elif parkiran.slot_parkiran_lantai_3['motor'] > 0:
                    parkiran.parkir_lantai_3()
                    print(f'{jenis_kendaraan} diparkir di lantai 3')
                else:
                    print('Parkiran Penuh!!!')
    
            elif jenis_kendaraan == '2':
                jenis_kendaraan = 'mobil'
                parkiran.jenis_kendaraan = jenis_kendaraan
                parkiran.plat_nomor = plat_nomor
    
                if parkiran.slot_parkiran_lantai_3['mobil'] > 0:
                    parkiran.parkir_lantai_3()
                    print(f'{jenis_kendaraan} diparkir di lantai 3')
                elif parkiran.slot_parkiran_lantai_2['mobil'] > 0:
                    parkiran.parkir_lantai_2()
                    print(f'{jenis_kendaraan} diparkir di lantai 2')
                elif parkiran.slot_parkiran_lantai_1['mobil'] > 0:
                    parkiran.parkir_lantai_1()
                    print(f'{jenis_kendaraan} diparkir di lantai 1')
                else:
                    print('Parkiran Penuh!!!')
    
            elif jenis_kendaraan == '3':
                jenis_kendaraan = 'bus'
                parkiran.jenis_kendaraan = jenis_kendaraan
                parkiran.plat_nomor = plat_nomor
    
                if parkiran.slot_parkiran_lantai_3['bus'] > 0:
                    parkiran.parkir_lantai_3()
                    print(f'{jenis_kendaraan} diparkir di lantai 3')
                else:
                    print('Parkiran Penuh!!!')
    
            else:
                print('Pilihan Tidak Tersedia')
                continue
    
        elif pilihan == '2':
            laporan = input(
                'Pilih Laporan\n'
                '1. Cek Posisi Kendaraan\n'
                '2. Total Semua Kendaraan\n'
                '3. Total Pendapatan\n'
                '4. Cek Ketersediaan Parkiran Setiap Jenis Kendaraan\n'
                'Masukkan Pilihan: '
            )
    
            if laporan == '1':
                parkiran.cek_posisi_kendaraan()
            elif laporan == '2':
                parkiran.total_semua_kendaraan()
            elif laporan == '3':
                parkiran.total_pendapatan()
            elif laporan == '4':
                parkiran.cek_ketersediaan_parkiran_setiap_jenis_kendaraan()
            else:
                print('Pilihan laporan tidak valid.')
    
        elif pilihan == '3':
            print('Terimakasih telah menggunakan program ini')
            break
        else:
            print('Pilihan menu tidak tersedia.')
