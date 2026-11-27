
"""Personal Subscription Manager."""

import datetime


data_langganan = []


# Membuat ID otomatis
def buat_id_langganan():
    id_baru = len(data_langganan) + 1
    return id_baru


# Menambahkan langganan aplikasi
def tambah_data_langganan():
    id_langganan = buat_id_langganan()

    nama = input("Masukkan Nama Aplikasi: ")
    harga = float(input("Masukkan Harga Langganan: "))
    paket = input("Masukkan Jenis Paket: ")

    periode = input("Periode (Bulanan/Tahunan): ")
    status = input("Status (Aktif/Nonaktif): ")

    tahun = int(input("Masukkan Tahun Berlangganan: "))
    bulan = int(input("Masukkan Bulan Berlangganan 1 - 12 : "))
    tanggal = int(input("Masukkan Tanggal Berlangganan 1 - 31 : "))

    try:
        tanggal_langganan = datetime.datetime(
            tahun, bulan, tanggal
        )
    except ValueError:
        print("Tanggal tidak valid!")
        return

    data_langganan.append({
        "ID": id_langganan,
        "Nama_Aplikasi": nama,
        "Harga": harga,
        "Paket": paket,
        "Periode": periode,
        "Status": status,
        "Tanggal": tanggal_langganan
    })

    print("\nLangganan berhasil ditambahkan!")
    print("ID Langganan:", id_langganan)


# Melihat seluruh langganan
def lihat_data_langganan():
    if len(data_langganan) == 0:
        print("Belum ada data langganan.")
        return

    print("\n================ DAFTAR LANGGANAN ================")

    print(
        f"{'ID':<5} {'Aplikasi':<17} {'Paket':<13} "
        f"{'Harga':<15} {'Periode':<12} {'Status':<10} {'Tanggal':<12}"
    )
    print("-" * 85)

    for langganan in data_langganan:
        print(
            f"{langganan['ID']:<5} "
            f"{langganan['Nama_Aplikasi']:<17} "
            f"{langganan['Paket']:<13} "
            f"Rp{langganan['Harga']:<13,.0f} "
            f"{langganan['Periode']:<12} "
            f"{langganan['Status']:<10}"
            f" {langganan['Tanggal'].strftime('%Y-%m-%d'):<12}"
        )

    print("-" * 85)
    print("Total langganan:", len(data_langganan))


# Mengedit langganan
def mengedit_data_langganan():
    nama_cari = input("Masukkan Nama Aplikasi yang ingin diedit: ")

    for langganan in data_langganan:
        if langganan["Nama_Aplikasi"].lower() == nama_cari.lower():
            print("\nPilih data yang ingin diubah:")
            print("1. Nama Aplikasi")
            print("2. Harga")
            print("3. Paket")
            print("4. Periode")
            print("5. Status")
            print("6. Tanggal")

            pilihan = input("Pilihan: ")

            if pilihan == "1":
                langganan["Nama_Aplikasi"] = input("Nama Aplikasi baru: ")

            elif pilihan == "2":
                langganan["Harga"] = float(input("Harga baru: "))

            elif pilihan == "3":
                langganan["Paket"] = input("Paket baru: ")

            elif pilihan == "4":
                langganan["Periode"] = input("Periode baru: ")

            elif pilihan == "5":
                langganan["Status"] = input("Status baru: ")

            elif pilihan == "6":
                tahun = int(input("Tahun baru: "))
                bulan = int(input("Bulan baru: "))
                tanggal = int(input("Tanggal baru: "))

                try:
                    langganan["Tanggal"] = datetime.datetime(
                        tahun, bulan, tanggal
                    )
                except ValueError:
                    print("Tanggal tidak valid!")
                    return

            else:
                print("Pilihan tidak valid.")
                return

            print("Langganan berhasil diedit.")
            return

    print("Langganan tidak ditemukan.")


# Menghapus langganan
def menghapus_data_langganan():
    nama_cari = input("Masukkan Nama Aplikasi yang ingin dihapus: ")

    for langganan in data_langganan:
        if langganan["Nama_Aplikasi"].lower() == nama_cari.lower():

            data_langganan.remove(langganan)

            print("Langganan berhasil dihapus.")
            return

    print("Langganan tidak ditemukan.")


# Mencari langganan
def mencari_data_langganan():
    nama_cari = input("Masukkan Nama Aplikasi yang ingin dicari: ")

    ditemukan = False

    for langganan in data_langganan:
        if langganan["Nama_Aplikasi"].lower() == nama_cari.lower():

            print("\n================ DATA LANGGANAN DITEMUKAN ================")
            print(
                f"{'ID':<5} {'Aplikasi':<17} {'Paket':<13} "
                f"{'Harga':<15} {'Periode':<12} {'Status':<10} {'Tanggal':<12}"
            )
            print("-" * 85)
            print(
                f"{langganan['ID']:<5} "
                f"{langganan['Nama_Aplikasi']:<17} "
                f"{langganan['Paket']:<13} "
                f"Rp{langganan['Harga']:<13,.0f} "
                f"{langganan['Periode']:<12} "
                f"{langganan['Status']:<10}"
                f" {langganan['Tanggal'].strftime('%Y-%m-%d'):<12}"
            )
            print("-" * 85)

            ditemukan = True

    if ditemukan == False:
        print("Langganan tidak ditemukan.")


# Menghitung pengeluaran
def ringkasan_pengeluaran():
    total = 0
    jumlah_aktif = 0

    print("\n================ RINGKASAN LANGGANAN ================")
    print(
        f"{'ID':<5} {'Aplikasi':<17} {'Paket':<13} "
        f"{'Harga':<15} {'Periode':<12} {'Status':<10} {'Tanggal':<12}"
    )
    print("-" * 85)

    for langganan in data_langganan:
        print(
                    f"{langganan['ID']:<5} "
                    f"{langganan['Nama_Aplikasi']:<17} "
                    f"{langganan['Paket']:<13} "
                    f"Rp{langganan['Harga']:<13,.0f} "
                    f"{langganan['Periode']:<12} "
                    f"{langganan['Status']:<10}"
                    f" {langganan['Tanggal'].strftime('%Y-%m-%d'):<12}"
                )
        if langganan["Status"].lower() == "aktif":

            jumlah_aktif += 1
            
            if langganan["Periode"].lower() == "bulanan":
                total += langganan["Harga"]

            elif langganan["Periode"].lower() == "tahunan":
                total += langganan["Harga"] / 12

    print("-" * 85)
    print("Total seluruh langganan:", len(data_langganan))
    print("Total langganan aktif:", jumlah_aktif)
    print(f"Estimasi pengeluaran per bulan: Rp{total:,.0f}")


# Menu utama
def main():
    while True:
        print("\n====================================")
        print("     Manajemen Langganan Aplikasi     ")
        print("====================================")
        print("1. Tambah Langganan")
        print("2. Lihat Semua Langganan")
        print("3. Edit Langganan")
        print("4. Hapus Langganan")
        print("5. Cari Langganan")
        print("6. Ringkasan Pengeluaran")
        print("7. Keluar")
        print("====================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data_langganan()

        elif pilihan == "2":
            lihat_data_langganan()

        elif pilihan == "3":
            mengedit_data_langganan()

        elif pilihan == "4":
            menghapus_data_langganan()

        elif pilihan == "5":
            mencari_data_langganan()

        elif pilihan == "6":
            ringkasan_pengeluaran()

        elif pilihan == "7":
            print("Terima kasih telah menggunakan aplikasi.")
            break

        else:
            print("Pilihan tidak valid.")


main()
