class AkunBank:
    def __init__(self, nomor_rekening, saldo):
        self.nomor_rekening = nomor_rekening
        self._saldo = saldo
        self.__pin = 123456

    def lihat_rekening(self):
        print("\nInfo Rekening:")
        print('Nomor Rekening:', self.nomor_rekening)
        print('Saldo: Rp.', f"{self._saldo:,}".replace(",", "."))

    def tambah_saldo(self, tambah):
        self._saldo += tambah
        print(f'\n✅ Anda berhasil menambah saldo senilai: Rp. {tambah:,}'.replace(",", "."))
        print(f"Saldo Anda sekarang: Rp. {self._saldo:,}".replace(",", "."))

    def tarik_saldo(self, tarik):
        if tarik <= self._saldo:
            self._saldo -= tarik
            print(f'\n✅ Anda berhasil menarik saldo senilai: Rp. {tarik:,}'.replace(",", "."))
            print(f"Sisa saldo Anda: Rp. {self._saldo:,}".replace(",", "."))
        else:
            print('❌ Saldo Anda tidak mencukupi!')

    def ubah_pin(self, pin_baru):
        if isinstance(pin_baru, int) and len(str(pin_baru)) >= 6:
            self.__pin = pin_baru
            print("✅ PIN berhasil diubah!")
        else:
            print("❌ PIN baru harus terdiri dari minimal 6 digit angka.")



    def verifikasi_pin(self, pin):
        return pin == self.__pin

    def get_pin(self):
        return self.__pin


# ✅ Fungsi verifikasi PIN dengan batas 3x percobaan
def verifikasi_pin_3x(akun):
    for _ in range(3):
        pin = input("Masukkan PIN Anda: ")
        if not pin.isdigit():
            print("❌ PIN harus berupa angka.")
            continue
        if len(pin) < 6:
            print("❌ PIN harus minimal 6 digit.")
            continue
        if akun.verifikasi_pin(int(pin)):
            return True
        else:
            print("❌ PIN salah.")
    print("🚫 Terlalu banyak percobaan. Akses ditolak.")
    return False

# Inisialisasi akun
akun = AkunBank("1234567890", 999999999999)

# Autentikasi awal sebelum menu
print("=== SELAMAT DATANG DI BANK RYO ===")
if not verifikasi_pin_3x(akun):
    exit()

# Menu utama
while True:
    print('\n======= MENU REKENING BANK =======')
    print('1. Lihat rekening')
    print('2. Tambah saldo')
    print('3. Tarik saldo')
    print('4. Ubah PIN')
    print('5. Keluar')
    print('==================================')
    pilihan = input("Masukkan nomor menu: ")

    if pilihan == '1':
        akun.lihat_rekening()

    elif pilihan == '2':
        try:
            tambah = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
            akun.tambah_saldo(tambah)
        except ValueError:
            print("❌ PIN harus berupa angka!")

    elif pilihan == '3':
        try:
            tarik = int(input("Masukkan jumlah saldo yang ingin ditarik: "))
            if verifikasi_pin_3x(akun):
                akun.tarik_saldo(tarik)
        except ValueError:
            print("❌ PIN harus berupa angka!")


    elif pilihan == '4':
        if verifikasi_pin_3x(akun):
            for _ in range(3):
                pin_baru = input("Masukkan PIN baru (minimal 6 digit): ")
                if not pin_baru.isdigit():
                    print("❌ PIN harus berupa angka!")
                    continue
                elif len(pin_baru) < 6:
                    print("❌ PIN harus minimal 6 digit.")
                    continue
                elif int(pin_baru) == akun.get_pin():  # ← Cek kesamaan dengan PIN lama
                    print("❌ PIN baru tidak boleh sama dengan PIN lama.")
                    continue
                konfirmasi = input("Konfirmasi PIN baru: ")
                if pin_baru != konfirmasi:
                    print("❌ Konfirmasi PIN tidak cocok.")
                    continue
                else:
                    akun.ubah_pin(int(pin_baru))
                    break
            else:
                print("🚫 Gagal mengubah PIN setelah 3 percobaan.")


    elif pilihan == '5':
        print('\n👋 Anda berhasil keluar dari rekening. Terima kasih!')
        break

    else:
        print("❌ Menu tidak ditemukan. Coba lagi.")