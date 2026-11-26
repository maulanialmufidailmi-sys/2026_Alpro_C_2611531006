# 1. Baca kedua baris input dan pecah dengan split()
daftar_kelas = input().split()
daftar_kumpul = input().split()

# 2. Gunakan set untuk membuang nomor ganda & hitung yang sudah mengumpulkan
set_kelas = set(daftar_kelas)
set_kumpul = set(daftar_kumpul)
jumlah_kumpul = len(set_kumpul)

# 3. Gunakan operasi set untuk menghitung yang belum mengumpulkan
belum_kumpul = set_kelas - set_kumpul
jumlah_belum = len(belum_kumpul)

# Cetak ringkasan jumlah
print(f"Submitted: {jumlah_kumpul} students")
print(f"Not submitted: {jumlah_belum} students")

# 4. Telusuri daftar kelas dari depan dan cetak yang tidak ada di set pengumpul
for nomor in daftar_kelas:
    if nomor not in set_kumpul:
        print(nomor)