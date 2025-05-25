"Ini adalah file yang otomatis menambahkan, menyimpan dan memanage hasil kontak"

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