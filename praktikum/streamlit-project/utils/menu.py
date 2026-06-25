import os
import csv

FILE_MENU = "data/menu.csv"

def load_menu():
    if not os.path.exists(FILE_MENU):
        return []
    with open(FILE_MENU, "r", newline="") as file:
        reader = csv.reader(file)
        return list(reader)

def tambah_menu(nama, harga, stok):
    os.makedirs("data", exist_ok=True)
    with open(FILE_MENU, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nama, harga, stok])

def hapus_menu(nama):
    menu = load_menu()
    with open(FILE_MENU, "w", newline="") as file:
        writer = csv.writer(file)
        for m in menu:
            if m[0] != nama:
                writer.writerow(m)

def ubah_menu(nama_lama, nama_baru, harga_baru, stok_baru):
    menu = load_menu()
    ditemukan = False
    with open(FILE_MENU, "w", newline="") as file:
        writer = csv.writer(file)
        for m in menu:
            if m[0] == nama_lama:
                final_nama = nama_baru.strip() if nama_baru.strip() else nama_lama
                writer.writerow([final_nama, harga_baru, stok_baru])
                ditemukan = True
            else:
                writer.writerow(m)
    return ditemukan
