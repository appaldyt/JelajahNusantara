def tampilkan_menu_rencana():
    """
    Menampilkan sub-menu pengelolaan rencana kunjungan wisata.
    """
    print("\n=== Kelola Rencana Kunjungan ===")
    print("1. Lihat semua rencana kunjungan")
    print("2. Buat rencana kunjungan baru")
    print("3. Edit rencana kunjungan")
    print("4. Hapus rencana kunjungan")
    print("5. Kembali ke Menu Utama")

def jalankan_menu_rencana():
    """
    Menangani input pengguna untuk sub-menu rencana kunjungan.
    """
    while True:
        tampilkan_menu_rencana()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            print(">> Fitur: Lihat semua rencana kunjungan [BELUM DIIMPLEMENTASI]")
        elif pilihan == "2":
            print(">> Fitur: Buat rencana kunjungan baru [BELUM DIIMPLEMENTASI]")
        elif pilihan == "3":
            print(">> Fitur: Edit rencana kunjungan [BELUM DIIMPLEMENTASI]")
        elif pilihan == "4":
            print(">> Fitur: Hapus rencana kunjungan [BELUM DIIMPLEMENTASI]")
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")
