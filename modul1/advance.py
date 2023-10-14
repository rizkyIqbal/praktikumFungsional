data_buku = [("Atomic Habit", "Budi Doremi"), ("Filosofi Teras", "Yovi Pramudita")]

userAdmin = [("rizky@mail", "123"), ("iqbal@mail", "321")]
userPengguna = [("risk", "123"), ("iqbal", "321")]

peminjaman_buku = {}
is_login = False


def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    data_buku.append((judul, penulis))
    print("Buku berhasil ditambahkan.")


def tampilkan_daftar_buku():
    print("\nDaftar Buku Tersedia:")
    # print(data_buku[0])
    # for i in  data_buku:
    #     print(i)
    for i, buku in enumerate(data_buku):
        print(f"{i + 1}. Judul: {buku[0]}, Penulis: {buku[1]}")


def pinjam_buku(username):
    tampilkan_daftar_buku()
    pilihan = int(input("\nPilih buku yang ingin dipinjam (nomor): ")) - 1

    if 0 <= pilihan < len(data_buku):
        buku_dipinjam = data_buku[pilihan]
        if buku_dipinjam not in peminjaman_buku.values():
            peminjaman_buku[username] = buku_dipinjam
            print(f"Buku '{buku_dipinjam[0]}' berhasil dipinjam oleh {username}.")
        else:
            print("Buku ini sudah dipinjam oleh pengguna lain.")
    else:
        print("Nomor buku tidak valid.")


def kembalikan_buku(username):
    if username in peminjaman_buku:
        buku_dikembalikan = peminjaman_buku.pop(username)
        print(f"Buku '{buku_dikembalikan[0]}' berhasil dikembalikan oleh {username}.")
    else:
        print("Anda tidak memiliki buku yang sedang dipinjam.")


while True:
    # if is_login == True:
    print("\nMenu:")
    print("1. Admin - Tambah Buku")
    print("2. User - Pinjam Buku")
    print("3. User - Kembalikan Buku")
    print("4. Keluar")

    akun = input("Masukkan jenis akun (admin/user): ").lower()

    if akun == "admin":
        emailAdmin = input("Masukkan Email Admin: ")
        passwordAdmin = input("Masukkan Password Admin: ")
        for i, user in enumerate(userAdmin):
            if emailAdmin == user[0] and passwordAdmin == user[1]:
                # is_login == True
                admin_pilihan = input("Masukkan menu admin (1 - Tambah Buku): ")
                if admin_pilihan == "1":
                    tambah_buku()
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
            else:
                print("Autentikasi Gagal")
    elif akun == "user":
        usernameUser = input("Masukkan Username Pengguna: ")
        passwordUser = input("Masukkan Password Pengguna: ")
        # username = input("Masukkan nama pengguna: ")
        for i, user in enumerate(userPengguna):
            if usernameUser == user[0] and passwordUser == user[1]:
                # is_login == True
                user_pilihan = input(
                    "Masukkan menu user (2 - Pinjam Buku, 3 - Kembalikan Buku): "
                )
                if user_pilihan == "2":
                    pinjam_buku(usernameUser)
                elif user_pilihan == "3":
                    kembalikan_buku(usernameUser)
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
        print("Autentikasi Gagal")
    elif akun == "keluar":
        break
    else:
        print("Akun tidak valid. Silakan coba lagi.")
