#Aplikasi Manajemen Langganan
#fiturnya fungsi
#1. menambah data langganan
#2. melihat data langganan
#3. mengedit data langganan
#4. menghapus data langganan
#5. mencari data langganan
#6. menampilkan ringkasan pengeluaran

data_langganan = [
    "ID", ""
    "Nama", ""
    "Harga", ""
    "Paket", ""
    "Status", ""
    "Tanggal Berlangganan", ""
]

def tambah_data_langganan():
    id_langganan = input("Masukkan ID Langganan: ")
    nama_langganan = input("Masukkan Nama Langganan: ")
    harga_langganan = input("Masukkan Harga Langganan: ")
    jenis_paket_langganan = input("Masukkan Paket Langganan: ")
    status_langganan = input("Masukkan Status Langganan: ")
    tanggal_berlangganan = input("Masukkan Tanggal Berlangganan: ")
    

    data_langganan.append({
        "ID": id_langganan,
        "Nama": nama_langganan,
        "Harga": harga_langganan,
        "Paket": jenis_paket_langganan,
        "Status": status_langganan,
        "Tanggal Berlangganan": tanggal_berlangganan
    })
    print("Data langganan berhasil ditambahkan.")

tambah_data_langganan()