print("====Volume Persegi Panjang====")
def volume_persegi_panjang(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

panjang = float(input("Masukkan Panjang: "))
lebar = float(input("Masukkan Lebar: "))
tinggi = float(input("Masukkan Tinggi: "))

volume = volume_persegi_panjang(panjang, lebar, tinggi)
print(f"Hasil Volumenya adalah {volume}")

volume_persegi_panjang(panjang, lebar, tinggi)