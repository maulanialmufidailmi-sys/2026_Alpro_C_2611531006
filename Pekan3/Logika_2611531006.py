# Program operator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_1006 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_1006 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 = ",a1_1006)
print("A2 = ",a2_1006)

# Konjungsi: bernilai True jika keduanya True
hasil_1006 = a1_1006 and a2_1006
print("\nKonjungsi (AND)")
print("A1 and A2 =",hasil_1006)

# Disjungsi: bernilai True jika salah satunya False
hasil_1006 = a1_1006 or a2_1006
print("\nDisjungsi (OR)")
print("A1 or A2 =",hasil_1006)

# Negasi A1: membalik nilai A1
hasil_1006 = not a1_1006
print("\nNegasi A1(NOT)")
print("not A1",hasil_1006)

# Negasi A2: membalik nilai A2
hasil_1006 = not a2_1006
print("\nNegasi A2(NOT)")
print("not A2",hasil_1006)

# XOR: bernilai True jika kedua nilai berbeda
hasil_1006 = a1_1006 != a2_1006
print("\nDisjungsi Ekslusif (XOR)")
print("A1 XOR A2",hasil_1006)
