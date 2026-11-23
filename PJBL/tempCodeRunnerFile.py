"""Aplikasi manajemen langganan."""

import datetime


data_langganan = []

def tambah_data_langganan():
    id_langganan = input("Masukkan ID Langganan: ")
    nama_langganan = input("Masukkan Nama Langganan: ")
    harga_langganan = input("Masukkan Harga Langganan: ")
    jenis_paket = input("Masukkan Jenis Paket: ")
    status_langganan = input("Masukkan Status Langganan: ")
    tanggal_berlangganan = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data_langganan.append({
        "ID": id_langganan,
        "Nama": nama_langganan,
        "Harga": harga_langganan,
        "Jenis_Paket": jenis_paket,
        "Status": status_langganan,
        "Tanggal Berlangganan": tanggal_berlangganan
    })
    print("Data langganan berhasil ditambahkan.")
tambah_data_langganan()

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
            print(f"Tanggal Berlangganan: {langganan['Tanggal Berlangganan']}")
            print("------------------------")

def mengedit_data_langganan():
    id_cari = input("Masukkan ID Langganan yang ingin diedit: ")

    for langganan in data_langganan:
        if langganan["ID"] == id_cari:
            langganan["Nama"] = input("Masukkan Nama baru: ")
            langganan["Harga"] = input("Masukkan Harga baru: ")
            langganan["Jenis_Paket"] = input("Masukkan Paket baru: ")
            langganan["Status"] = input("Masukkan Status baru: ")
            langganan["Tanggal Berlangganan"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Data langganan berhasil diedit.")
            return

print("Data tidak ada tersebut tidak ditemukan.")


if __name__ == "__main__":
    tambah_data_langganan()
    lihat_data_langganan()