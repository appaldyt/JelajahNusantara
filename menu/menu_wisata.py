from data.tempat_wisata_data import tempat_wisata

def tampilkan_menu_wisata():
    """
    Menampilkan sub-menu pengelolaan data tempat wisata.
    """
    print("\n=== Kelola Tempat Wisata ===")
    print("1. Lihat semua tempat wisata")
    print("2. Tambah tempat wisata")
    print("3. Edit tempat wisata")
    print("4. Hapus tempat wisata")
    print("5. Kembali ke Menu Utama")

def lihat_tempat_wisata():
    """
    Menampilkan seluruh daftar tempat wisata dari data dictionary.
    """
    if not tempat_wisata:
        print("Tidak ada data tempat wisata.")
        return

    print("\n--- Daftar Tempat Wisata ---")
    for id, info in tempat_wisata.items():
        print(f"{id}. {info['nama']} - {info['lokasi']} ({info['kategori']})")

def tambah_tempat_wisata():
    """
    Menambahkan tempat wisata baru ke dalam dictionary.

    Akan mengecek duplikat nama, meminta konfirmasi sebelum menyimpan.
    """
    #Lihat tempat wisata sebelum tambah
    lihat_tempat_wisata()

    print("\n--- Tambah Tempat Wisata Baru ---")
    nama = input("Masukkan nama tempat wisata: ").strip()
    lokasi = input("Masukkan lokasi (kota/provinsi): ").strip()
    kategori = input("Masukkan kategori (Alam/Budaya/Pantai/dll): ").strip()

    # Cek duplikat berdasarkan nama (case insensitive)
    for data in tempat_wisata.values():
        if data["nama"].lower() == nama.lower():
            print("Gagal: Tempat wisata dengan nama ini sudah ada.")
            return

    # Konfirmasi simpan
    konfirmasi = input("Simpan data ini? (Y/N): ").strip().lower()
    if konfirmasi == "y":
        id_baru = max(tempat_wisata.keys(), default=0) + 1
        tempat_wisata[id_baru] = {
            "nama": nama,
            "lokasi": lokasi,
            "kategori": kategori
        }
        print("Data tempat wisata berhasil disimpan.")
    else:
        print("Data tidak disimpan.")

def edit_tempat_wisata():
    """
    Mengedit data tempat wisata berdasarkan ID.

    Memeriksa apakah ID valid, menampilkan data lama,
    meminta input perubahan, dan konfirmasi update.
    """

    #Lihat tempat wisata sebelum edit
    lihat_tempat_wisata()

    print("\n--- Edit Tempat Wisata ---")
    try:
        id_edit = int(input("Masukkan ID tempat wisata yang ingin diedit (Exp: 1/2/3): "))
    except ValueError:
        print("Input tidak valid. ID harus berupa angka.")
        return

    if id_edit not in tempat_wisata:
        print("Data tidak ditemukan. Pastikan ID benar.")
        return

    data_lama = tempat_wisata[id_edit]
    print(f"Data saat ini: {data_lama['nama']} - {data_lama['lokasi']} ({data_lama['kategori']})")

    # Input data baru (boleh dikosongkan)
    nama_baru = input("Nama baru (kosongkan jika tidak diubah): ").strip()
    lokasi_baru = input("Lokasi baru (kosongkan jika tidak diubah): ").strip()
    kategori_baru = input("Kategori baru (kosongkan jika tidak diubah): ").strip()

    # Konfirmasi update
    konfirmasi = input("Update data ini? (Y/N): ").strip().lower()
    if konfirmasi == "y":
        if nama_baru:
            data_lama["nama"] = nama_baru
        if lokasi_baru:
            data_lama["lokasi"] = lokasi_baru
        if kategori_baru:
            data_lama["kategori"] = kategori_baru

        print("Data berhasil diperbarui:")
        print(f"{id_edit}. {data_lama['nama']} - {data_lama['lokasi']} ({data_lama['kategori']})")
    else:
        print("Update dibatalkan.")

def hapus_tempat_wisata():
    """
    Menghapus data tempat wisata berdasarkan ID.

    Mengecek apakah data kosong, memvalidasi ID,
    dan meminta konfirmasi sebelum menghapus.
    """
    
    if not tempat_wisata:
        print("Tidak ada data tempat wisata untuk dihapus.")
        return

    # Tampilkan daftar tempat wisata sebelum hapus
    lihat_tempat_wisata()

    print("\n--- Hapus Tempat Wisata ---")

    try:
        id_hapus = int(input("Masukkan ID tempat wisata yang ingin dihapus (Exp: 1/2/3): "))
    except ValueError:
        print("Input tidak valid. ID harus berupa angka.")
        return

    if id_hapus not in tempat_wisata:
        print("Data dengan ID tersebut tidak ditemukan.")
        return

    data = tempat_wisata[id_hapus]
    print(f"Anda akan menghapus: {data['nama']} - {data['lokasi']} ({data['kategori']})")
    konfirmasi = input("Yakin ingin menghapus? (Y/N): ").strip().lower()

    if konfirmasi == "y":
        del tempat_wisata[id_hapus]
        print("Data berhasil dihapus.")
    else:
        print("Data tidak jadi dihapus.")


def jalankan_menu_wisata():
    """
    Menangani input pengguna untuk sub-menu tempat wisata.
    """
    while True:
        tampilkan_menu_wisata()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            lihat_tempat_wisata()
        elif pilihan == "2":
            tambah_tempat_wisata()
        elif pilihan == "3":
            edit_tempat_wisata()
        elif pilihan == "4":
            hapus_tempat_wisata()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")
