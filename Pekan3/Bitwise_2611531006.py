# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("======================================")
print("3. OPERATOR BITWISE")
print("======================================")

angka1_1006 = int(input("Masukkan angka bitwise-1: "))
angka2_1006 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =",angka1_1006,"| biner =",bin(angka1_1006))
print("angka1 =",angka2_1006,"| biner =",bin(angka2_1006))

# Bitwise AND
hasil_1006 = angka1_1006 & angka2_1006
print("\nBitwise AND (&)")
print(angka1_1006,"&",angka2_1006,hasil_1006)
print("Biner hasil =",bin(hasil_1006))
print("Biner hasil (8 bit) =",format(hasil_1006,"08b"))

# Bitwise OR
hasil_1006 = angka1_1006 | angka2_1006
print("\nBitwise OR (|)")
print(angka1_1006,"|",angka2_1006,hasil_1006)
print("Biner hasil =",bin(hasil_1006))
print("Biner hasil (8 bit) =",format(hasil_1006,"08b"))

# Bitwise XOR
hasil_1006 = angka1_1006 ^ angka2_1006
print("\nBitwise XOR (^)")
print(angka1_1006,"^",angka2_1006,hasil_1006)
print("Biner hasil =",bin(hasil_1006))
print("Biner hasil (8 bit) =",format(hasil_1006,"08b"))

# Bitwise NOT
hasil_1006 = ~angka1_1006
print("\nBitwise NOT (~)")
print(angka1_1006,"~",angka2_1006,hasil_1006)
print("Biner hasil =",bin(hasil_1006))
print("Biner hasil (8 bit) =",format(hasil_1006,"08b"))

# Bitwise geser kiri
jumlah_geser_1006 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_1006 = angka1_1006 << jumlah_geser_1006
print("\nBitwise geser kiri (<<)")
print(angka1_1006,"<<",jumlah_geser_1006,"=",hasil_1006)
print("Biner hasil =",bin(hasil_1006))
print("Biner hasil (8 bit) =",format(hasil_1006,"08b"))

# Bitwise geser kanan
hasil_1006 = angka1_1006 >> jumlah_geser_1006
print("\nBitwise geser kanan (>>)")
print(angka1_1006,">>",jumlah_geser_1006,"=",hasil_1006)
print("Biner hasil =",bin(hasil_1006))
print("Biner hasil (8 bit) =",format(hasil_1006,"08b"))
