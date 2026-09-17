# Buat program untuk operator aritmatika dalam Python

angka1 = int(input("Input angka-1: "))
angka2 = int(input("Input angka-2: "))

# Penjumlahan
hasil = angka1 + angka2
print ("\nOperator penjumlahan")
print ("Hasil =", hasil)

# Pengurangan
hasil = angka1 - angka2
print ("\nOperator pengurangan")
print ("Hasil =", hasil)

# Perkalian
hasil = angka1 * angka2
print("\nOperator Perkalian")
print("Hasil =", hasil)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2 != 0:
    hasil = angka1 / angka2
    print("\nOperator Pembagian")
    print("Hasil =", hasil)

    hasil = angka1 // angka2
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil)

    hasil = angka1 % angka2
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil = angka1 ** angka2
print("\nOperator Pangkat")
print("Hasil =", hasil)