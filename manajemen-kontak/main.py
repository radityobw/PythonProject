# MANAJEMEN KONTAK
import os

# Dapatkan path folder tempat file main.py berada
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KONTAK_PATH = os.path.join(BASE_DIR, 'kontak.txt')

# Cek apakah file sudah ada, jika tidak, buat file kosong
if not os.path.exists(KONTAK_PATH):
    with open(KONTAK_PATH, 'w') as f:
        pass  # buat file kosong



def membuka_kontak(path=KONTAK_PATH):
    with open(path, 'r') as file:
        kontak = file.readlines()
        return kontak

def menyimpan_kontak(path=KONTAK_PATH, isi=[]):
    with open(path, 'w') as file:
        file.writelines(isi)

class Kontak:
    def __init__(self):
        self.kontak = membuka_kontak()

    def melihat_kontak(self):
        # melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f"\n{num}. " + item)
        else:
            print("\nKontak kosong!")

    def menambah_kontak(self):
        while True:  # sub-loop untuk penambahan kontak
            nama = input('Masukkan nama kontak yang baru: ')
            no_HP = input('Masukkan no HP kontak yang baru: ')
            email = input('Masukkan email kontak yang baru: ')
            konfirmasi = input('Apakah informasi sudah benar? (ya/tidak/kembali): ')

            if konfirmasi == 'ya':
                kontakBaru = f'{nama} ({no_HP}, {email})' + '\n'
                self.kontak.append(kontakBaru)
                print("\nKontak baru berhasil ditambahkan!")
                break  # keluar dari sub-loop setelah berhasil
            elif konfirmasi == 'tidak':
                print("\nSilakan masukkan ulang data kontak.")
                continue  # ulangi sub-loop
            elif konfirmasi == 'kembali':
                break
            else:
                print("\nInput salah! Silakan pilih 'ya', 'tidak' atau 'kembali'.")
                continue

    def menghapus_kontak(self):
        while True:  # sub-loop untuk penghapusan kontak
            self.melihat_kontak()

            try:
                iHapus = int(input('\nMasukkan angka kontak yang akan dihapus: '))
                if iHapus < 1 or iHapus > len(self.kontak):
                    print("Nomor kontak tidak valid!")
                    continue
            except ValueError:
                print("Input harus berupa angka!")
                continue

            konfirmasi = input('Apakah Anda yakin ingin menghapus kontak? (ya/tidak/kembali): ')
            if konfirmasi == 'ya':
                del self.kontak[iHapus - 1]
                print('\nKontak berhasil dihapus!')
                break  # keluar dari sub-loop
            elif konfirmasi == 'tidak':
                print("\nPenghapusan dibatalkan. Silakan pilih ulang.")
                continue  # ulangi sub-loop
            elif konfirmasi == 'kembali':
                break
            else:
                print("\nInput salah! Silakan pilih 'ya', 'tidak' atau 'kembali'.")
                continue

    def keluar_kontak(self):
        menyimpan_kontak(isi=self.kontak)

kontakku = Kontak()

while True:
    print('\n------------------------')
    print("Menu Kontak (By: Ryo)")
    print('------------------------')
    print("1. Melihat semua kontak")
    print("2. Menambahkan kontak")
    print("3. Menghapus kontak")
    print("4. Keluar dari kontak")
    print('------------------------')

    pilihan = input("Masukkan pilihan menu kontak (1,2,3,4): ")

    if pilihan == '1':
        kontakku.melihat_kontak()

    elif pilihan == '2':
        kontakku.menambah_kontak()

    elif pilihan == '3':
        if not kontakku.kontak:
            print("\nKontak kosong!")
            continue
        kontakku.menghapus_kontak()

    elif pilihan == '4':
        # keluar dari kontak
        kontakku.keluar_kontak()
        break

    else:
        print('\nInput yang Anda masukkan salah!')