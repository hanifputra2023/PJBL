"""Aplikasi manajemen langganan."""

import datetime


data_langganan = []

def tambah_data_langganan():
    id_langganan = input("Masukkan ID Langganan: ")
    nama_langganan = input("Masukkan Nama Langganan: ")
    harga_langganan = input("Masukkan Harga Langganan: ")
    paket_langganan = input("Masukkan Paket Langganan: ")
    status_langganan = input("Masukkan Status Langganan: ")
    tanggal_berlangganan = input("Masukkan Tanggal Berlangganan: ")

    data_langganan.append({
        "ID": id_langganan,
        "Nama": nama_langganan,
        "Harga": harga_langganan,
        "Paket": paket_langganan,
        "Status": status_langganan,
        "Tanggal Berlangganan": tanggal_berlangganan
    })
    print("Data langganan berhasil ditambahkan.")