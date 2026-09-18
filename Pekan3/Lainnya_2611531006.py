# Program keanggotaan dan identitas dalam python

print("======================================")
print("1. OPERATOR KEANGGOTAAN")
print("======================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_1006 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_1006 = [int(angka.strip()) for angka in input_data_1006.split(',')]

nilai_dicari_1006 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_1006 = nilai_dicari_1006 in data_1006
print("\nOperator keanggotaan IN")
print(nilai_dicari_1006,"in",data_1006,"=",hasil_1006)

# Operator not in
hasil_1006 = nilai_dicari_1006 not in data_1006
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_1006,"not in",data_1006,"=",hasil_1006)

print("======================================")
print("2. OPERATOR IDENTIAS")
print("======================================")

# objek1 menggunakan list dari input perngguna
object1_1006 = data_1006

# objek2 merujuk pada objek yang sama dengan objek1
object2_1006 = object1_1006

# objek3 memiliki isi sama, tetapi merupakan objek baru
object3_1006 = data_1006.copy()

print("object1 =",object1_1006)
print("object2 =",object2_1006)
print("object3 =",object3_1006)

# Operator is
hasil_1006 = object1_1006 is object2_1006
print("\nOperator identitas IS")
print("objek1 is objek2 =",hasil_1006)

# Operator is not
hasil_1006 = object1_1006 is not object2_1006
print("\nOperator identitas IS NOT")
print("objek1 is not objek2 =",hasil_1006)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =",object1_1006 is object3_1006)
print("objek1 == objek3 =",object1_1006 == object3_1006)
