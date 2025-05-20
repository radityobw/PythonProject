# MANAJEMEN AGENDA

def buat_agenda(agenda, agenda_baru):
    agenda.append(agenda_baru)
    print("Agenda baru telah dibuat!")

def lihat_agenda(agenda):
    print("\nDaftar Agendaku: ")
    for i, agenda in enumerate(agenda):
        if len(agenda) == 0:
            print("Agenda Kosong")
        else:
            print(f"{i+1}. {agenda}")


agenda = []
def main():
    print("\n---------------------")
    print("Agendaku (By: Ryo):")
    print("---------------------")
    print("1. Buat Agenda")
    print("2. Lihat Agenda")
    print("3. Keluar dari Agenda")


    pilihan = input("Masukkan pilihan (1, 2, 3): ")
    print("---------------------")

    if pilihan == "1":
        agenda_baru = input("\nMasukkan agenda baru: ")
        buat_agenda(agenda, agenda_baru)
        return True
    elif pilihan == "2":
        lihat_agenda(agenda)
        return True
    elif pilihan == "3":
        return False
    else:
        print("Input salah!")
        return True

while True:
    if not main():
        print("Anda telah keluar dari Agenda")
        break


