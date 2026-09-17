# Program keanggotaan dan identitas dalam python

print("==================================")
print("1.OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma'
Input_data = input("Input beberapa data, pisahkan dengan koma:")

# Mengubah input menjadi list integer
data = [int(angka.strip()) for angka in Input_data.split(",")]

nilai_dicari = int(input("Masukkan angka yang ingin dicari:"))

# Operator in
hasil = nilai_dicari in data
print("\nOperator keanggotaan IN")
print(nilai_dicari, "in data =", hasil)

#Operator not in
hasil = nilai_dicari not in data
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari, "not in", data, "=", hasil)
print("==================================")
print("2.OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1 = data

# objek2 merujuk pada objek yang sama dengan objek1
objek2 = objek1

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3 = data.copy()

print("objek1 =", objek1)
print("objek2 =", objek2)
print("objek3 =", objek3)

# Operator is
hasil = objek1 is objek2
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil)

# Operator is not
hasil = objek1 is not objek3
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1 is objek3)
print("objek1 == objek3 =", objek1 == objek3)