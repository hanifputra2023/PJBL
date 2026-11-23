import datetime
import os
import random
import string


# Template key yang akan dimiliki setiap data mahasiswa.
mahasiswa_template = {
    "nama": "nama",
    "nim": "00000000",
    "sks_lulus": 0,
    "lahir": datetime.datetime(1111, 1, 11),
}

# Dictionary utama untuk menyimpan banyak data mahasiswa.
data_mahasiswa = {}

# Perulangan agar pengguna dapat memasukkan lebih dari satu mahasiswa.
while True:
    # Membersihkan layar: "cls" untuk Windows dan "clear" untuk sistem lain.
    os.system("cls" if os.name == "nt" else "clear")
    print(f'{"SELAMAT DATANG":^20}')
    print(f'{"DATA MAHASISWA":^20}')
    print("-" * 20)

    # Membuat dictionary mahasiswa baru berdasarkan key pada template.
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    # Mengisi data mahasiswa dari input pengguna.
    mahasiswa["nama"] = input("Nama Mahasiswa: ")
    mahasiswa["nim"] = input("NIM Mahasiswa: ")
    mahasiswa["sks_lulus"] = int(input("SKS Lulus: "))

    # Meminta tanggal lahir dan mengubah setiap input menjadi integer.
    tahun_lahir = int(input("Tahun lahir (YYYY): "))
    bulan_lahir = int(input("Bulan lahir (1-12): "))
    tanggal_lahir = int(input("Tanggal lahir (1-31): "))
    # Menggabungkan tanggal lahir menjadi satu objek datetime.
    mahasiswa["lahir"] = datetime.datetime(
        tahun_lahir,
        bulan_lahir,
        tanggal_lahir,
    )

    # Membuat kode acak enam huruf kapital sebagai key mahasiswa.
    key = "".join(random.choice(string.ascii_uppercase) for _ in range(6))
    # Menyimpan data mahasiswa ke dictionary utama.
    data_mahasiswa.update({key: mahasiswa})

    # Menampilkan judul tabel.
    print(
        f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} "
        f"{'SKS Lulus':<10} {'Tanggal Lahir':<10}"
    )
    print("-" * 60)

    # Menampilkan semua mahasiswa yang sudah tersimpan.
    for key, mahasiswa in data_mahasiswa.items():
        nama = mahasiswa["nama"]
        nim = mahasiswa["nim"]
        sks = mahasiswa["sks_lulus"]
        # Mengubah tanggal lahir menjadi teks agar mudah dibaca.
        lahir = mahasiswa["lahir"].strftime("%x")

        print(f"{key:<6} {nama:<17} {nim:<8} {sks:^10} {lahir:^10}")

    print()
    # lower() membuat input Y dan y diperlakukan sama.
    is_done = input("Mau tambah lagi bro (y/n)? ").lower()
    # Berhenti jika pengguna memilih "n".
    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih")