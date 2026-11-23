#Buatlah program dengan input dan fungsi untuk menghitung:
#a. Luas persegi panjang
#b. Volume persegi panjang
#c. Luas lingkaran
#d. Volume bola
print("====Luas Persegi Panjang====")
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas
input_panjang = float(input("Masukkan panjang persegi panjang: "))
input_lebar = float(input("Masukkan lebar persegi panjang: "))
luas = luas_persegi_panjang(input_panjang, input_lebar)
print(f"Luas persegi panjang adalah: {luas}")

luas_persegi_panjang(input_panjang, input_lebar)

print("====Volume Persegi Panjang====")
def volume_persegi_panjang(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

panjang = float(input("Masukkan Panjang: "))
lebar = float(input("Masukkan Lebar: "))
tinggi = float(input("Masukkan Tinggi: "))

volume = luas_persegi_panjang(panjang, lebar, tinggi)
print(f"Hasil Volumenya adalah {volume}")

volume_persegi_panjang(panjang, lebar, tinggi)


print("====Luas Lingkaran====")
def luas_lingkaran(Jari):
    jarijari = 22 / 7 * Jari**2
    return jarijari

Jari = float(input("Masukkan Jari Jari: "))
jarijari = luas_lingkaran(Jari)
print(f"Hasil Luas Lingkaran: {jarijari}")

hasil = luas_lingkaran(Jari)
hasil_akhir = hasil * 2
print(f"Hasil Luas Akhir: {hasil_akhir}")




def jari_jari_bola(diameter):
    r = diameter / 2
    return r

diameter = float(input("Masukkan Diameter Bola: "))
hasil_jari_jari = jari_jari_bola(diameter)

print(f"Hasil Jari Jari Bolanya: {hasil_jari_jari}")

def volume_bola(hasil_jari_jari):
    phi = 3.14
    volume = 4/3 * phi * hasil_jari_jari**3
    return volume

hasil_volume_bola = volume_bola(hasil_jari_jari)
print(f"Hasil Volume Bola ini: {hasil_volume_bola}") 