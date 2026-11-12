# Meminta input kalimat dari pengguna
kalimat = input("Masukkan kalimat: ")

# Menghapus spasi dan mengubah semua huruf menjadi huruf kecil
teks_bersih = kalimat.replace(" ", "").lower()

# Memeriksa apakah teks sama jika dibalik menggunakan slicing [::-1]
if teks_bersih == teks_bersih[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")