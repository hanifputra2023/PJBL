"""Aplikasi manajemen langganan."""

import datetime


data_langganan = []

def tambah_data_langganan():
    id_langganan = input("Masukkan ID Langganan: ")
    nama_langganan = input("Masukkan Nama Langganan: ")
    harga_langganan = input("Masukkan Harga Langganan: ")
    jenis_paket = input("Masukkan Jenis Paket: ")
    status_langganan = input("Masukkan Status Langganan: ")
    tahun = int(input("Masukkan Tahun Berlangganan: "))
    bulan = int(input("Masukkan Bulan Berlangganan (1-12): "))
    tanggal = int(input("Masukkan Tanggal Berlangganan (1-31): "))
    tanggal_berlangganan = datetime.datetime(tahun, bulan, tanggal)

    data_langganan.append({
        "ID": id_langganan,
        "Nama": nama_langganan,
        "Harga": harga_langganan,
        "Jenis_Paket": jenis_paket,
        "Status": status_langganan,
        "Tanggal Berlangganan": tanggal_berlangganan
    })
    print("Data langganan berhasil ditambahkan.")

def lihat_data_langganan():
    if len(data_langganan) == 0:
        print("Tidak ada data langganan.")
    else:
        print("Data Langganan:")
        for langganan in data_langganan:
            print(f"ID: {langganan['ID']}")
            print(f"Nama: {langganan['Nama']}")
            print(f"Harga: {langganan['Harga']}")
            print(f"Jenis_Paket: {langganan['Jenis_Paket']}")
            print(f"Status: {langganan['Status']}")
            print(
                "Tanggal Berlangganan: "
                f"{langganan['Tanggal Berlangganan'].strftime('%Y-%m-%d')}"
            )
            print("------------------------")

def mengedit_data_langganan():
    id_cari = input("Masukkan ID Langganan yang ingin diedit: ")

    for langganan in data_langganan:
        if langganan["ID"] == id_cari:
            langganan["Nama"] = input("Masukkan Nama baru: ")
            langganan["Harga"] = input("Masukkan Harga baru: ")
            langganan["Jenis_Paket"] = input("Masukkan Paket baru: ")
            langganan["Status"] = input("Masukkan Status baru: ")
            tahun = int(input("Masukkan Tahun baru: "))
            bulan = int(input("Masukkan Bulan baru (1-12): "))
            tanggal = int(input("Masukkan Tanggal baru (1-31): "))
            langganan["Tanggal Berlangganan"] = datetime.datetime(tahun, bulan, tanggal)
            print("Data langganan berhasil diedit.")
            return

    print("Data dengan ID tersebut tidak ditemukan.")

if __name__ == "__main__":
    tambah_data_langganan()
    lihat_data_langganan()