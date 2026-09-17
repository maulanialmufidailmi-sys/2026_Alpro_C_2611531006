# Program assignment dalam python

angka1 = int(input("Input angka-1:"))
angka2 = int(input("Input angka-2:"))

print("\nNilai awal angka1 =", angka1)
print("Nilai awal angka2 =", angka2)

# Assignement biasa
hasil = angka1
print("\nAssignment Biasa (=)")
print("Hasil =", hasil)

# Assignment penambahan
hasil = angka1
hasil += angka2
print("\nAssignment Penambahan (+=)")
print("Hasil =", hasil)

# Assignment pengurangan
hasil = angka1
hasil -= angka2
print("\nAssignment Pengurangan (-=)")
print("Hasil =", hasil)

# Assignment perkalian
hasil = angka1
hasil *= angka2
print("\nAssignment Perkalian (*=)")
print("Hasil =", hasil)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2 != 0:
    hasil = angka1
    hasil /= angka2
    print("\nAssignment Pembagian (/=)")
    print("Hasil =", hasil)
    # Operator tambahan
    hasil = angka1
    hasil //= angka2
    print("\nAssignment Pembagian Bulat (//=)")
    print("Hasil =", hasil)
    hasil = angka1
    hasil %= angka2
    print("\nAssignment Sisa Bagi (%=)")
    print("Hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0.")
    
# Operator tambahan: assignment perpangkatan
hasil = angka1
hasil **= angka2
print("\nAssignment Perpangkatan (**=)")
print("Hasil =", hasil)