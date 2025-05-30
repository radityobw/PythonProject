import PySimpleGUI as pg
import os

if os.path.exists('agenda.txt'):
    with open('agenda.txt', 'r') as file:
        agendaku = file.readlines()
else:
    with open('agenda.txt', 'w') as file:
        file.writelines([])
    with open('agenda.txt', 'r') as file:
        agendaku = file.readlines()

#Elemen
label_input = pg.Text("Masukkan Agenda: ")
label_daftar = pg.Text("Daftar Agendaku: ")
box_input = pg.InputText(key='key_box_input', size=(40,1))
tombol_tambah = pg.Button("Tambah", key='key_tambah')
tombol_hapus = pg.Button("Hapus", key='key_hapus')
tombol_keluar =pg.Button("Keluar", key='key_keluar')
daftar_agenda = pg.Listbox(values=agendaku, key='daftar_agenda', size=(60,10))


#Window
window = pg.Window(title="Agendaku (By:Ryo)",
                   layout=[[label_input], [box_input, tombol_tambah], [tombol_hapus, tombol_keluar], [label_daftar], [daftar_agenda]],
                   size=(1000,600),
                   font=("Helvetica", 20))
while True:
    event, data = window.read()
    print(event)
    print(data)

    match event:
        case "key_tambah":
            #menambahkan agenda
            agenda_baru = data['key_box_input']
            agendaku.append(agenda_baru + '\n')
            window['daftar_agenda'].update(values=agendaku)
        case "key_hapus":
            #menghapus agenda
            if data['daftar_agenda']:
                agenda_dihapus = data['daftar_agenda'][0]
                agendaku.remove(agenda_dihapus)
                window['daftar_agenda'].update(agendaku)
        case "key_keluar":
            #keluar agenda
            with open('agenda.txt', 'w') as file:
                file.writelines(agendaku)
            break

window.close()


