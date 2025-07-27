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

def jalankan_menu_wisata():
    """
    Menangani input pengguna untuk sub-menu tempat wisata.
    """
    while True:
        tampilkan_menu_wisata()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            print(">> Fitur: Lihat tempat wisata [BELUM DIIMPLEMENTASI]")
        elif pilihan == "2":
            print(">> Fitur: Tambah tempat wisata [BELUM DIIMPLEMENTASI]")
        elif pilihan == "3":
            print(">> Fitur: Edit tempat wisata [BELUM DIIMPLEMENTASI]")
        elif pilihan == "4":
            print(">> Fitur: Hapus tempat wisata [BELUM DIIMPLEMENTASI]")
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")
