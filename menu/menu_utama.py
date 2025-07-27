from menu.menu_wisata import jalankan_menu_wisata
from menu.menu_rencana import jalankan_menu_rencana

def tampilkan_menu_utama():
    """
    Menampilkan menu utama aplikasi JelajahNusantara.
    """
    print("\n=== JelajahNusantara - Menu Utama ===")
    print("1. Kelola Tempat Wisata")
    print("2. Kelola Rencana Kunjungan")
    print("3. Keluar")

def jalankan_menu_utama():
    """
    Loop utama untuk navigasi dari menu utama ke sub-menu.
    """
    while True:
        tampilkan_menu_utama()
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            jalankan_menu_wisata()
        elif pilihan == "2":
            jalankan_menu_rencana()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan JelajahNusantara!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
