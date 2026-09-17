# Program operator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1= input("input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2= input("Input nilal boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1)
print("A2", a2)

# Konjungsi: bernilai True Jika keduanya True
hasil = a1 and a2
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil)

# Disjungsi: bernilai True jika salah satunya True
hasil = a1 or a2
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil)

# Negasi A1: membalik nilai A1
hasil = not a1
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil)

# Negasi A2: membalik nilai A2
hasil = not a2
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil)

# XOR: bernilai True jika kedua nilai berbeda
hasil = a1 != a2
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", has