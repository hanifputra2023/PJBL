## Fungsi dengan argumen
## def nama_fungsi(argumen1, argumen2):
##     # kode yang dijalankan

def hello_world(nama):
    print(f"Hello, Selamat Datang, {nama}!")
hello_world("Nanda")

def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_2
    print(f"Hasil penjumlahan {angka_1} + {angka_2} = {hasil}")

tambah(5, 3)

def say_hi(list_perserta):
    data_perserta = list_perserta.copy()
    for peserta in data_perserta:
        print(f"Halo, {peserta}!")

kumpulan_mahasiswa = ["Nanda", "Rizki", "Dewi", "Budi"]

say_hi(kumpulan_mahasiswa)
