import email

kontak1 = {'nama': 'Radit', 'no HP': '090909090909', 'email': 'nibbler@gmail.com'}
kontak2 = {'nama': 'Tya', 'no HP': '080808080808', 'email': 'cupcake@gmail.com'}
kontak = [kontak1, kontak2]

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
        # melihat semua kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f"\n{num}. {item['nama']} ({item['no HP']}, {item['email']})")
        else:
            print("\nKontak kosong!")

    elif pilihan == '2':

        while True:  # sub-loop untuk penambahan kontak
            nama = input('Masukkan nama kontak yang baru: ')
            no_HP = input('Masukkan no HP kontak yang baru: ')
            email = input('Masukkan email kontak yang baru: ')

            konfirmasi = input('Apakah informasi sudah benar? (ya/tidak/kembali): ')

            if konfirmasi == 'ya':
                kontakBaru = {'nama': nama, 'no HP': no_HP, 'email': email}
                kontak.append(kontakBaru)
                print("\nKontak baru berhasil ditambahkan!")
                break  # keluar dari sub-loop setelah berhasil

            elif konfirmasi == 'tidak':
                print("\nSilakan masukkan ulang data kontak.")
                continue  # ulangi sub-loop

            elif konfirmasi == 'kembali':
                break

            else:
                print("\nInput salah! Silakan pilih 'ya' atau 'tidak'.")

    elif pilihan == '3':

        if not kontak:
            print("\nKontak kosong!")
            continue

        while True:  # sub-loop untuk penghapusan kontak

            for num, item in enumerate(kontak, start=1):
                print(f"\n{num}. {item['nama']} ({item['no HP']}, {item['email']})")

            try:
                iHapus = int(input('\nMasukkan angka kontak yang akan dihapus: '))

                if iHapus < 1 or iHapus > len(kontak):
                    print("Nomor kontak tidak valid!")

                    continue
            except ValueError:
                print("Input harus berupa angka!")
                continue

            konfirmasi = input('Apakah Anda yakin ingin menghapus kontak? (ya/tidak/kembali): ')

            if konfirmasi == 'ya':
                del kontak[iHapus - 1]
                print('\nKontak berhasil dihapus!')
                break  # keluar dari sub-loop

            elif konfirmasi == 'tidak':
                print("\nPenghapusan dibatalkan. Silakan pilih ulang.")
                continue  # ulangi sub-loop

            elif konfirmasi == 'kembali':
                break

            else:
                print("\nInput salah! Silakan pilih 'ya' atau 'tidak'.")

    elif pilihan == '4':
        # keluar dari kontak
        break

    else:
        print('\nInput yang Anda masukkan salah!')