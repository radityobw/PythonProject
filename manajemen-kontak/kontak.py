"Ini adalah fungsi/logika utama aplikasi kontak"

import dokumen

class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()

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
        dokumen.menyimpan_kontak(isi=self.kontak)