import datetime


# Setiap dictionary menyimpan data satu mahasiswa.
mahasiswa1 = {
    "nama": "Ucup Surucup",
    "nim": "19022001",
    "sks_lulus": 130,
    "beasiswa": False,
    "lahir": datetime.datetime(2001, 4, 10),
}

mahasiswa2 = {
    "nama": "Azan Magrib",
    "nim": "19022002",
    "sks_lulus": 140,
    "beasiswa": True,
    "lahir": datetime.datetime(2002, 10, 10),
}

mahasiswa3 = {
    "nama": "Slamet Dunia Akhirat",
    "nim": "19022003",
    "sks_lulus": 100,
    "beasiswa": True,
    "lahir": datetime.datetime(1977, 5, 10),
}

# Dictionary bertingkat: key luar adalah kode mahasiswa,
# sedangkan value-nya adalah dictionary data mahasiswa.
data_mahasiswa = {
    "MAH001": mahasiswa1,
    "MAH002": mahasiswa2,
    "MAH003": mahasiswa3,
}

# Menampilkan judul tabel dengan lebar kolom yang sudah ditentukan.
print(f'{"KEY":<6} {"Nama":<20} {"SKS":<3} {"Beasiswa":<9} {"Lahir":<10}')
# Membuat garis pemisah di bawah judul tabel.
print("-" * 60)

# Mengambil key dan data setiap mahasiswa untuk ditampilkan.
for key, mahasiswa in data_mahasiswa.items():
    nama = mahasiswa["nama"]
    sks = mahasiswa["sks_lulus"]
    beasiswa = mahasiswa["beasiswa"]
    # Mengubah objek tanggal menjadi teks dengan format tanggal lokal.
    lahir = mahasiswa["lahir"].strftime("%x")

    print(f"{key:<6} {nama:<20} {sks:<3} {str(beasiswa):<9} {lahir:<10}")