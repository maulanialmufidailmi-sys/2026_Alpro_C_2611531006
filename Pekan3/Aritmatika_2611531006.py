# Buat program untuk operator aritmatika dalam Python

angka1_1006 = int(input("Input angka-1: "))
angka2_1006 = int(input("Input angka-2: "))

# Penjumlahan
hasil_1006 = angka1_1006 + angka2_1006
print("\nOperator Penjumlahan")
print("Hasil =",hasil_1006)

# Pengurangan
hasil_1006 = angka1_1006 - angka2_1006
print("\nOperator Pengurangan")
print("Hasil =",hasil_1006)

# Perkalian
hasil_1006 = angka1_1006 * angka2_1006
print("\nOperator Perkalian")
print("Hasil =",hasil_1006)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_1006 != 0:
    hasil_1006 = angka1_1006 / angka2_1006
    print("\nOperator Pembagian")
    print("Hasil =",hasil_1006)

    hasil_1006 = angka1_1006 // angka2_1006
    print("\nOperator Pembagian Bulat")
    print("Hasil =",hasil_1006)

    hasil_1006 = angka1_1006 % angka2_1006
    print("\nOperator Sisa Bagi")
    print("Hasil =",hasil_1006)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_1006 = angka1_1006 ** angka2_1006
print("\nOperator Pangkat")
print("Hasil =",hasil_1006)
