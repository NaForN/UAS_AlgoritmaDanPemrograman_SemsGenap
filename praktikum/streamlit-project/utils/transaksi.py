import os
import csv
from datetime import datetime
from utils.menu import load_menu 
FILE_TRANSAKSI = "data/transaksi.csv"
FILE_MENU = "data/menu.csv"

def catat_transaksi(menu, jumlah, total):
    os.makedirs("data", exist_ok=True)
    with open(FILE_TRANSAKSI, "a", newline="") as file:
        writer = csv.writer(file)
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([waktu, menu, jumlah, total])

    
    data_menu = load_menu()
    with open(FILE_MENU, "w", newline="") as file:
        writer = csv.writer(file)
        for m in data_menu:
            if m[0] == menu:
                stok_baru = int(m[2]) - jumlah
                if stok_baru < 0:
                    stok_baru = 0
                writer.writerow([m[0], m[1], stok_baru])
            else:
                writer.writerow(m)

def load_transaksi():
    if not os.path.exists(FILE_TRANSAKSI):
        return []
    with open(FILE_TRANSAKSI, "r", newline="") as file:
        reader = csv.reader(file)
        return list(reader)
