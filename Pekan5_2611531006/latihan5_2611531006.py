# Meminta input tinggi segitiga dari pengguna
tinggi_1006 = int(input("Masukkan tinggi segitiga: "))

# Perulangan untuk setiap baris segitiga
for i in range(1, tinggi_1006 + 1):
    # Mencetak spasi di awal baris diikuti dengan bintang yang dipisahkan spasi
    print(" " * (tinggi_1006 - i) + "* " * i)