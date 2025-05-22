class AkunBank:
    def __init__(self, nomor_rekening, saldo):
        self.nomor_rekening = nomor_rekening
        self._saldo = saldo
        self.__pin = 1234

    def lihat_rekening(self):
        print('\nRekening:', self.nomor_rekening)
        print('Saldo: Rp.', f"{self._saldo:,}".replace(",", "."))

    def tambah_saldo(self, tambah):
        self._saldo += tambah
        print(f'✅ Anda berhasil menambah saldo senilai: Rp. {tambah:,}'.replace(",", "."))
        print(f"Saldo Anda sekarang: Rp. {self._saldo:,}".replace(",", "."))

    def tarik_saldo(self, tarik, pin):
        if pin == self.__pin:
            if tarik <= self._saldo:
                self._saldo -= tarik
                print(f'✅ Anda berhasil menarik saldo senilai: Rp. {tarik:,}'.replace(",", "."))
                print(f"Sisa saldo Anda: Rp. {self._saldo:,}".replace(",", "."))
            else:
                print('❌ Saldo Anda tidak mencukupi!')
        else:
            print('❌ PIN yang Anda masukkan salah!')

    def ubah_pin(self, pin_lama, pin_baru):
        if pin_lama == self.__pin:
            self.__pin = pin_baru
            print("✅ PIN berhasil diubah!")
        else:
            print('❌ PIN lama yang Anda masukkan salah!')

    def verifikasi_pin(self, pin):
        return pin == self.__pin


# Inisialisasi akun
akun = AkunBank("1234567890", 0)

# 🔐 Verifikasi PIN sebelum akses menu
print("=== SELAMAT DATANG DI BANKKU ===")
for _ in range(3):  # Maksimal 3 percobaan
    try:
        pin_masuk = int(input("Masukkan PIN Anda untuk masuk: "))
        if akun.verifikasi_pin(pin_masuk):
            print("✅ PIN benar. Akses diberikan.")
            break
        else:
            print("❌ PIN salah.")
    except ValueError:
        print("❌ PIN harus berupa angka.")
else:
    print("🚫 Terlalu banyak percobaan. Akses ditolak.")
    exit()  # Keluar dari program jika 3x gagal

# Menu utama
while True:
    print('\n===== Menu Rekening Bank =====')
    print('1. Lihat rekening')
    print('2. Tambah saldo')
    print('3. Tarik saldo')
    print('4. Ubah PIN')
    print('5. Keluar')
    pilihan = input("Masukkan nomor menu: ")

    if pilihan == '1':
        akun.lihat_rekening()

    elif pilihan == '2':
        try:
            tambah = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
            akun.tambah_saldo(tambah)
        except ValueError:
            print("❌ Masukkan harus berupa angka!")

    elif pilihan == '3':
        try:
            tarik = int(input("Masukkan jumlah saldo yang ingin ditarik: "))
            pin = int(input("Masukkan PIN Anda: "))
            akun.tarik_saldo(tarik, pin)
        except ValueError:
            print("❌ Input harus berupa angka!")

    elif pilihan == '4':
        try:
            pin_lama = int(input("Masukkan PIN lama Anda: "))
            pin_baru = int(input("Masukkan PIN baru: "))
            akun.ubah_pin(pin_lama, pin_baru)
        except ValueError:
            print("❌ Input PIN harus berupa angka!")

    elif pilihan == '5':
        print('\n👋 Anda berhasil keluar dari rekening. Terima kasih!')
        break

    else:
        print("❌ Menu tidak ditemukan. Coba lagi.")