#1
#  Buat file dengan nama jumlah_genap_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_1006 = int(input("Maukkan nilai batas: "))

jumlah_1006 = 0
for i_1006 in range(1, ulang_1006 + 1):
    if i_1006 % 2 == 0:
        print(i_1006, end="")
        jumlah_1006 = jumlah_1006 + i_1006
        
        if i_1006 < ulang_1006:
            print("+", end="")
        else:
            print("=", jumlah_1006, end="")
print()
print("Jumlah =", jumlah_1006)