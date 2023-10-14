book_data = {}
peminjaman = {}


def add_buku():
    judul = input("Title: ")
    penulis = input("Author: ")
    bidang = input("Genre: ")

    book_id = len(book_data) + 1

    book_data[book_id] = {"Title": judul, "Author": penulis, "Genre": bidang }
    print(f"This book with ID {book_id} successfuly added ")


def pinjam_buku():
    tampilkan_daftar_buku()
    id_buku = int(input("Input the ID of the book you want to borrow: "))
    nama_peminjam = input("Input your name: ")      

    if id_buku in book_data:
        title = book_data[id_buku]["Title"]
        if id_buku in peminjaman: 
            print(f"The book with ID {id_buku} is already borrowed by {peminjaman[id_buku]['Peminjam']}.")
        else:
            peminjaman[id_buku] = {"Title": title, "Peminjam": nama_peminjam}
            print(f"{title} has been borrowed by {nama_peminjam}.")
    else:
        print("The book with that ID is not available.")

     

def pengembalian():
    nama_peminjam = input("Input your name: ")

#show the list books that someones borrow
    borrowed_books = []
    for id_buku, data in peminjaman.items():
        if data["Peminjam"] == nama_peminjam:
            borrowed_books.append({"ID Buku": id_buku, "Title": data["Title"]})

    if len(borrowed_books) == 0:
        print("No books have been borrowed by that name.")
    else:
        print(f"Books borrowed by {nama_peminjam}:")
        for buku in borrowed_books:
            print(f"ID: {buku['ID Buku']}, Title: {buku['Title']}")

        id_buku_kembali = int(input("Input the ID of the book you want to return: "))
        for buku in borrowed_books:
            if buku["ID Buku"] == id_buku_kembali:
                buku_ditemukan = True
                del peminjaman[id_buku_kembali]
                print(f"The book with ID {id_buku_kembali} has been returned.")
                break

        if not buku_ditemukan:
            print("Book with that ID is not valid.")


def tampilkan_daftar_buku():
    print("\nList of books:")
    if not book_data:
        print("Theres no any book here")
        
    else :
        for id_buku, buku_info in book_data.items():
            print(f"ID: {id_buku}, Title: {buku_info['Title']}, Writer: {buku_info['Author']}, Genre: {buku_info['Genre']}")
while True:
    print("\n1. Login as admin")
    print("2. Login as user")

    choose_login = input("Your Choice: ")

    if choose_login == "1":
        print("\nHello Admin!")
        print("1. Add book")
        print("2. See the list of book")

        admin_choose = input("Your choice: ")
        if admin_choose == "1":
            add_buku()
        elif admin_choose == "2":
            tampilkan_daftar_buku()

    elif choose_login == "2":
        print("\nHello User!")
        print("What you want to do?")
        print("1. See the list of books")
        print("2. Return a book")
        print("3. Borrow a book")
        choose = input("I want to: ")

        if choose == "1":
            tampilkan_daftar_buku()
        elif choose == "2":
            pengembalian()
        elif choose == "3":
            pinjam_buku()
