# Buat nama Perulangan_for3_2611531006.py

ulang_1006 = int(input("Masukkan jumlah perulangan: "))

jumlah_1006 = 0
for i_1006 in range(1, ulang_1006 + 1):
    print(i_1006, end=" ")
    jumlah_1006 = jumlah_1006 + 1

    if 1 < ulang_1006:
        print(" + ", end=" ")
    else:
        print(" + ", jumlah_1006, end=" ")
print()
print("Jumlah =", jumlah_1006)