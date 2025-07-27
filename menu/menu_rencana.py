from data.tempat_wisata_data import tempat_wisata
from data.rencana_kunjungan_data import rencana_kunjungan
from datetime import datetime

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

def lihat_rencana_kunjungan():
    """
    Menampilkan semua rencana kunjungan wisata yang telah dibuat.

    Jika tidak ada data, akan memberi pesan bahwa data kosong.
    """
    print("\n--- Daftar Rencana Kunjungan ---")
    if not rencana_kunjungan:
        print("Tidak ada rencana kunjungan yang tersedia.")
        return

    for tema, detail in rencana_kunjungan.items():
        print(f"\n Tema: {tema}")
        print(f"   Tanggal: {detail['tanggal_mulai']} s.d. {detail['tanggal_akhir']}")

        daftar = detail.get("daftar_wisata", [])
        if not daftar:
            print("   Tempat wisata: (kosong)")
        else:
            print("   Tempat wisata:")
            for id_wisata in daftar:
                wisata = tempat_wisata.get(id_wisata)
                if wisata:
                    print(f"     - {wisata['nama']} ({wisata['lokasi']})")
                else:
                    print(f"     - [ID {id_wisata}] tidak ditemukan")

def buat_rencana_kunjungan():
    """
    Membuat rencana kunjungan baru lengkap dengan tema, tanggal mulai, dan tanggal akhir.

    Melakukan validasi duplikat tema, validasi tanggal, serta konfirmasi penyimpanan.
    """
    # Menampilkan daftar rencana yang ada
    lihat_rencana_kunjungan()

    print("\n--- Buat Rencana Kunjungan Baru ---")
    tema = input("Masukkan tema rencana kunjungan: ").strip()

    # Cek duplikat tema
    if tema in rencana_kunjungan:
        print("Tema rencana sudah ada. Gunakan tema lain.")
        return

    # Input dan validasi tanggal
    tanggal_mulai = input("Masukkan tanggal mulai (YYYY-MM-DD): ").strip()
    tanggal_akhir = input("Masukkan tanggal akhir (YYYY-MM-DD): ").strip()

    try:
        tgl_mulai = datetime.strptime(tanggal_mulai, "%Y-%m-%d")
        tgl_akhir = datetime.strptime(tanggal_akhir, "%Y-%m-%d")
        if tgl_akhir < tgl_mulai:
            print("Tanggal akhir tidak boleh sebelum tanggal mulai.")
            return
    except ValueError:
        print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
        return

    # Tampilkan tempat wisata
    if not tempat_wisata:
        print("Tidak ada tempat wisata tersedia.")
        return

    print("\nPilih tempat wisata yang ingin dikunjungi:")
    for id, info in tempat_wisata.items():
        print(f"{id}. {info['nama']} - {info['lokasi']} ({info['kategori']})")

    ids_input = input("Masukkan ID tempat wisata dipisah koma (misal: 1,3): ")
    try:
        ids = [int(i.strip()) for i in ids_input.split(",") if int(i.strip()) in tempat_wisata]
    except ValueError:
        print("Input ID tidak valid.")
        return

    if not ids:
        print("Tidak ada tempat wisata valid yang dipilih.")
        return

    # Konfirmasi
    konfirmasi = input("Simpan rencana ini? (Y/N): ").strip().lower()
    if konfirmasi == "y":
        rencana_kunjungan[tema] = {
            "tanggal_mulai": tanggal_mulai,
            "tanggal_akhir": tanggal_akhir,
            "daftar_wisata": ids
        }
        print("Rencana kunjungan berhasil disimpan.")
    else:
        print("Rencana tidak disimpan.")

def edit_rencana_kunjungan():
    """
    Mengedit rencana kunjungan berdasarkan tema yang sudah ada.

    Menampilkan data lama, menerima input baru, melakukan validasi dan konfirmasi sebelum update.
    """

    # Menampilkan daftar rencana yang ada
    lihat_rencana_kunjungan()  

    print("\n--- Edit Rencana Kunjungan ---")

    if not rencana_kunjungan:
        print("Tidak ada rencana kunjungan yang tersedia untuk diedit.")
        return

    tema = input("Masukkan tema rencana yang ingin diedit: ").strip()

    if tema not in rencana_kunjungan:
        print("Rencana dengan tema tersebut tidak ditemukan.")
        return

    data_lama = rencana_kunjungan[tema]
    print(f"Data saat ini:")
    print(f"- Tanggal: {data_lama['tanggal_mulai']} s.d. {data_lama['tanggal_akhir']}")
    print("- Tempat wisata:")
    for id_wisata in data_lama["daftar_wisata"]:
        wisata = tempat_wisata.get(id_wisata)
        if wisata:
            print(f"  - {wisata['nama']} ({wisata['lokasi']})")

    # Input data baru (boleh kosong)
    tanggal_mulai = input("Tanggal mulai baru (kosongkan jika tidak diubah): ").strip()
    tanggal_akhir = input("Tanggal akhir baru (kosongkan jika tidak diubah): ").strip()
    daftar_baru_input = input("Masukkan ID tempat wisata baru (pisah koma, kosongkan jika tidak diubah): ").strip()

    # Validasi tanggal jika diisi
    tgl_mulai_final = data_lama["tanggal_mulai"]
    tgl_akhir_final = data_lama["tanggal_akhir"]

    try:
        if tanggal_mulai:
            tgl_mulai_obj = datetime.strptime(tanggal_mulai, "%Y-%m-%d")
            tgl_mulai_final = tanggal_mulai
        else:
            tgl_mulai_obj = datetime.strptime(tgl_mulai_final, "%Y-%m-%d")

        if tanggal_akhir:
            tgl_akhir_obj = datetime.strptime(tanggal_akhir, "%Y-%m-%d")
            tgl_akhir_final = tanggal_akhir
        else:
            tgl_akhir_obj = datetime.strptime(tgl_akhir_final, "%Y-%m-%d")

        if tgl_akhir_obj < tgl_mulai_obj:
            print("Tanggal akhir tidak boleh sebelum tanggal mulai.")
            return
    except ValueError:
        print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
        return

    # Validasi tempat wisata baru (jika diubah)
    daftar_wisata_final = data_lama["daftar_wisata"]
    if daftar_baru_input:
        try:
            ids = [int(i.strip()) for i in daftar_baru_input.split(",") if int(i.strip()) in tempat_wisata]
            if not ids:
                print("Tidak ada tempat wisata valid yang dipilih.")
                return
            daftar_wisata_final = ids
        except ValueError:
            print("Input ID tidak valid.")
            return

    # Konfirmasi
    konfirmasi = input("Simpan perubahan? (Y/N): ").strip().lower()
    if konfirmasi == "y":
        rencana_kunjungan[tema] = {
            "tanggal_mulai": tgl_mulai_final,
            "tanggal_akhir": tgl_akhir_final,
            "daftar_wisata": daftar_wisata_final
        }
        print("Rencana kunjungan berhasil diperbarui.")
    else:
        print("Perubahan dibatalkan.")

def hapus_rencana_kunjungan():
    """
    Menghapus rencana kunjungan berdasarkan tema.

    Memvalidasi apakah tema tersedia dan meminta konfirmasi sebelum menghapus.
    """

    # Menampilkan daftar rencana yang ada
    lihat_rencana_kunjungan()

    print("\n--- Hapus Rencana Kunjungan ---")

    if not rencana_kunjungan:
        print("Tidak ada rencana kunjungan yang tersedia untuk dihapus.")
        return

    tema = input("Masukkan tema rencana yang ingin dihapus: ").strip()

    if tema not in rencana_kunjungan:
        print("Rencana dengan tema tersebut tidak ditemukan.")
        return

    data = rencana_kunjungan[tema]
    print(f"\nAnda akan menghapus rencana:")
    print(f"- Tema: {tema}")
    print(f"- Tanggal: {data['tanggal_mulai']} s.d. {data['tanggal_akhir']}")
    print(f"- Jumlah tempat wisata: {len(data['daftar_wisata'])}")

    konfirmasi = input("Yakin ingin menghapus? (Y/N): ").strip().lower()
    if konfirmasi == "y":
        del rencana_kunjungan[tema]
        print("Rencana kunjungan berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

def jalankan_menu_rencana():
    """
    Menangani input pengguna untuk sub-menu rencana kunjungan.
    """
    while True:
        tampilkan_menu_rencana()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            lihat_rencana_kunjungan()
        elif pilihan == "2":
            buat_rencana_kunjungan()
        elif pilihan == "3":
            edit_rencana_kunjungan()
        elif pilihan == "4":
            hapus_rencana_kunjungan()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")
