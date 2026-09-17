# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("\n==========================================")
print("3. OPERATOR BITWISE")
print("==========================================")

angka1 = int(input("Masukkan angka bitwise-1: "))
angka2 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1, "| biner =", bin(angka1))
print("angka2 =", angka2, "| biner =", bin(angka2))

# Bitwise AND
hasil = angka1 & angka2
print("\nBitwise AND (&)")
print(angka1, "&", angka2, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise OR
hasil = angka1 | angka2
print("\nBitwise OR (|)")
print(angka1, "|", angka2, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise XOR
hasil = angka1 ^ angka2
print("\nBitwise XOR (^)")
print(angka1, "^", angka2, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise NOT
hasil = ~angka1
print("\nBitwise NOT (~)")
print("~", angka1, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kiri
jumlah_geser = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil = angka1 << jumlah_geser
print("\nBitwise geser kiri (<<)")
print(angka1, "<<", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kanan
hasil = angka1 >> jumlah_geser
print("\nBitwise geser kanan (>>)")
print(angka1, ">>", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))