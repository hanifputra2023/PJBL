#template fungsi kembalian
#def nama_fungsi(argumen1, argumen2):
#    # kode yang dijalankan
#   return nilai_kembalian

def kuadrat(input_angka):
    hasil_kuadrat = input_angka ** 2
    return hasil_kuadrat

y = kuadrat(5)
print(f"Hasil kuadrat dari 5 adalah: {y}")

print(kuadrat(10))

z = 10 + kuadrat(3)
print(f"Hasil dari 10 + kuadrat(3) adalah: {z}")

def fungsi_tambah(angka_1, angka_2):
    return angka_1 + angka_2
a = fungsi_tambah(10, 5)
print(f"Hasil penjumlahan 10 + 5 adalah: {a}")

def operasi_matematika(angka_1, angka_2):
    hasil_penjumlahan = angka_1 + angka_2
    hasil_pengurangan = angka_1 - angka_2
    hasil_perkalian = angka_1 * angka_2
    hasil_pembagian = angka_1 / angka_2
    return hasil_penjumlahan, hasil_pengurangan, hasil_perkalian, hasil_pembagian

k,l,m,n = operasi_matematika(10, 5)
print(f"Hasil penjumlahan: {k}")
print(f"Hasil pengurangan: {l}")
print(f"Hasil perkalian: {m}")
print(f"Hasil pembagian: {n}")