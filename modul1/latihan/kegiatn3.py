# # Fungsi Hitung Nilai Akhir

# def hitung_nilai_akhir(uts, uas):
#     return 0.4 * uts + 0.6 * uas

# # Fungsi untuk menghitung semua nilai akhir


# def hitung_semua_nilai_akhir(data_mahasiswa):
#     data_nilai_akhir = {}
#     for nama, nilai in data_mahasiswa.items():
#         nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
#         data_nilai_akhir[nama] = nilai_akhir
#     return data_nilai_akhir

# # Fungsi untuk menampilkan hasil nilai akhir


# def tampilkan_nilai_akhir(data_nilai_akhir):
#     print("Hasil Nilai Akhir Mahasiswa:")
#     for nama, nilai_akhir in data_nilai_akhir.items():
#         print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

# # Program utama


# def main():
#     data_mahasiswa = {
#         'Mahasiswa1': {'uts': 80, 'uas': 85},
#         'Mahasiswa2': {'uts': 75, 'uas': 90},
#         'Mahasiswa3': {'uts': 90, 'uas': 70},
#         # Masukkan data mahasiswa lainnya di sini
#     }

#     data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)

#     tampilkan_nilai_akhir(data_nilai_akhir)


# if __name__ == "__main__":
#     main()


# fungsi htung nilai ahir
def hitung_nilai_akhir(uts, uas):
    return (uts+uas)/2


# fungsi hitung akhir semua mahasiswa
def hitung_akhir_semua_mahasiswa(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai["uts"],nilai["uas"])

        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir
    # data_nilai_akhir = {nama, nilai akhir}

    

#nilai ahir 1 mahasiswa
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama,nilai_akhir))

def main():
    data_mahasiswa ={
        #data mahasiswa
        'Yovi Pramudita': {'uts': 80, 'uas': 90},
        'Yovi Arema': {'uts': 80, 'uas': 90},
        'Yovi': {'uts': 80, 'uas': 90},
        'Yovi Gay': {'uts': 80, 'uas': 90},
        'Yovi Bagus': {'uts': 80, 'uas': 90},
    }

    data_nilai_akhir = hitung_akhir_semua_mahasiswa(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
