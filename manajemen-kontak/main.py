# MANAJEMEN KONTAK
"Ini adalah user interface kontak dan fungsi kunci untuk menjalankannya"

import kontak
def main():
    kontakku = kontak.Kontak()

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

if __name__ == "__main__":
    main()