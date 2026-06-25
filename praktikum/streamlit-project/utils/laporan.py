import csv
from datetime import datetime

FILE_TRANSAKSI = "data/transaksi.csv"

def laporan_harian():
    today = datetime.now().strftime("%Y-%m-%d")
    total = 0
    transaksi_hari_ini = []
    try:
        with open(FILE_TRANSAKSI, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                tanggal = row[0].split()[0]
                if tanggal == today:
                    transaksi_hari_ini.append(row)
                    total += int(row[3])
    except FileNotFoundError:
        pass
    return transaksi_hari_ini, total
