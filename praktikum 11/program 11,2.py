import datetime


# Template berisi nama-nama key dan nilai awal data mahasiswa.
mahasiswa_template = {
    "nama": "nama",
    "nim": 0,
    "sks_lulus": 0,
    "lahir": datetime.datetime(1111, 1, 11),
}

# Disiapkan untuk menampung banyak data mahasiswa pada latihan berikutnya.
data_mahasiswa = {}

# Menampilkan judul program.
print(f'{"SELAMAT DATANG":^20}')
print(f'{"DATA MAHASISWA":^20}')
print("-" * 20)

# Membuat dictionary baru dengan key yang sama seperti template.
# Nilai awal setiap key adalah None.
mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)

# Mengisi data mahasiswa dari input pengguna.
mahasiswa["nama"] = input("Nama Mahasiswa: ")
mahasiswa["nim"] = input("NIM Mahasiswa: ")
mahasiswa["sks_lulus"] = int(input("SKS Lulus: "))

# Input tanggal lahir diubah dari teks menjadi bilangan bulat.
tahun_lahir = int(input("Tahun lahir (YYYY): "))
bulan_lahir = int(input("Bulan lahir (1-12): "))
tanggal_lahir = int(input("Tanggal lahir (1-31): "))

# Membuat objek datetime dari tahun, bulan, dan tanggal lahir.
mahasiswa["lahir"] = datetime.datetime(
    tahun_lahir,
    bulan_lahir,
    tanggal_lahir,
).strftime("%x")  # Mengubah objek datetime menjadi teks agar mudah dibaca.

print(mahasiswa)