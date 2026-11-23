import datetime
import os
import random
import string

perpustakaan_sederhana = {
    "Judul_Buku" : "judul_buku",
    "Penulis" : "penulis",
    "Tahun_Terbit" : 0,
    "Tanggal_Terakhir_Pinjam" : datetime.datetime(1111, 1, 11),
    "Status" : "status",
}

data_perpustakaan = {}

while True:
    #os.system("cls" if os.name == "nt" else "clear")
    print(f'{"SELAMAT DATANG":^20}')
    print(f'{"DATA PERPUSTAKAAN":^20}')
    print("-" * 20)

    buku = dict.fromkeys(perpustakaan_sederhana.keys())
    buku["Judul_Buku"] = input("Judul Buku: ")
    buku["Penulis"] = input("Penulis: ")
    tahun_terbit = int(input("Tahun Terbit (YYYY): "))
    bulan_terbit = int(input("Bulan Terbit (1-12): "))
    tanggal_terbit = int(input("Tanggal Terbit (1-31): "))
    buku["Tahun_Terbit"] = datetime.datetime(
        tahun_terbit,
        bulan_terbit,
        tanggal_terbit,
    )
    buku["Status"] = input("Status (Tersedia/Tidak Tersedia): ")
    tahun_pinjam = int(input("Tahun terakhir pinjam (YYYY): "))
    bulan_pinjam = int(input("Bulan terakhir pinjam (1-12): "))
    tanggal_pinjam = int(input("Tanggal terakhir pinjam (1-31): "))
    buku["Tanggal_Terakhir_Pinjam"] = datetime.datetime(
        tahun_pinjam,
        bulan_pinjam,
        tanggal_pinjam,
    )

    key = "".join(random.choice(string.ascii_uppercase) for _ in range(6))
    data_perpustakaan.update({key: buku})

    print(
        f"\n{'KEY':<8} {'Judul Buku':<30} {'Penulis':<25} "
        f"{'Tahun Terbit':<14} {'Status':<18} {'Tanggal Terakhir Pinjam':<24}"
    )
    print("-" * 122)

    for key, buku in data_perpustakaan.items():
        judul_buku = buku["Judul_Buku"][:30]
        penulis = buku["Penulis"][:25]
        tahun_terbit = buku["Tahun_Terbit"].strftime("%d-%m-%Y")
        status = buku["Status"][:18]
        tanggal_terakhir_pinjam = buku["Tanggal_Terakhir_Pinjam"].strftime(
            "%d-%m-%Y"
        )

        print(
            f"{key:<8} {judul_buku:<30} {penulis:<25} "
            f"{tahun_terbit:<14} {status:<18} {tanggal_terakhir_pinjam:<24}"
        )

    print()
    is_done = input("Apakah Anda ingin menambahkan data lagi? (y/n): ").lower()
    if is_done.lower() != 'y':
        break

print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")