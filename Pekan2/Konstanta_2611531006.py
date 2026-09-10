# Buat file dengan nama Konstanta_2611531006
# Program ini menggunakan konstanta untuk menghitun luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1006

from typing import Final
PI: Final = 3.14
print("Pi: %f" % (PI))
jari_1006 = float(input("Masukkan nilai jari-jari: "))
luas_1006 = PI * jari_1006
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1006,luas_1006))