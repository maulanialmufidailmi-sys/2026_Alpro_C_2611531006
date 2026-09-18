# Program assignment dalam python

angka1_1006 = int(input("Input angka-1: "))
angka2_1006 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =",angka1_1006)
print("Nilai angka2 =",angka2_1006)

# Assigment biasa
hasil_1006 = angka1_1006 
print("\nAssigment biasa (=)")
print("Hasil =",hasil_1006)

# Assigment penambahan
hasil_1006 = angka1_1006 
hasil_1006 += angka2_1006 
print("\nAssigment penambahan (+=)")
print("Hasil =",hasil_1006)

# Assigment pengurangan
hasil_1006 = angka1_1006 
hasil_1006 -= angka2_1006 
print("\nAssigment pengurangan (-=)")
print("Hasil =",hasil_1006)

# Assigment perkalian
hasil_1006 = angka1_1006 
hasil_1006 *= angka2_1006
print("\nAssigment perkalian (*=)")
print("Hasil =",hasil_1006)

# Assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_1006 != 0:
    hasil_1006 = angka1_1006 
    hasil_1006 /= angka2_1006
    print("\nAssigment pembagian (/=)")
    print("Hasil =",hasil_1006)
    # Operator tambahan
    hasil_1006 = angka1_1006 
    hasil_1006 //= angka2_1006
    print("\nAssigment pembagian bulat (//=)")
    print("Hasil =",hasil_1006)
    hasil_1006 = angka1_1006 
    hasil_1006 %= angka2_1006
    print("\nOperator sisa bagi (%=)")
    print("Hasil =",hasil_1006)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assigment perpangkatan
hasil_1006 = angka1_1006 
hasil_1006 **= angka2_1006
print("\nOperator perpangkatan (**=)")
print("Hasil =",hasil_1006)
