# ==========================================
# SISTEM TRANSAKSI TOKO
# Nama : Maulani Almufida Ilmi
# NIM  : _1006
# ==========================================

print("=== SISTEM TRANSAKSI TOKO ===")

# Input pelanggan
nama_1006 = input("Nama Pelanggan : ")
status_1006 = input("Status (member/nonmember) : ")
harga_1006 = float(input("Total Belanja : Rp"))
jumlah_1006 = int(input("Jumlah Barang : "))
promo_1006 = input("Kode Promo : ")

# Data promo
daftar_promo_1006 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# Perbandingan
member_1006 = status_1006 == "member"
belanja_1006 = harga_1006 >= 200000
barang_1006 = jumlah_1006 >= 3

# Membership
promo_ada_1006 = promo_1006 in daftar_promo_1006
promo_tidak_ada_1006 = promo_1006 not in daftar_promo_1006

# Logika
diskon_ok_1006 = member_1006 and belanja_1006
promo_ok_1006 = barang_1006 or promo_ada_1006
bukan_member_1006 = not member_1006

# Aritmatika
diskon_1006 = harga_1006 * 10 / 100 if diskon_ok_1006 else 0
total_1006 = harga_1006 - diskon_1006
rata_1006 = harga_1006 / jumlah_1006
sisa_1006 = jumlah_1006 % 2

# Penugasan
poin_1006 = 0
poin_1006 += int(harga_1006 // 10000)

# Identity
a_1006 = ["member"]
b_1006 = ["member"]

# Bitwise
kode_1006 = 0

if member_1006:
    kode_1006 |= 1

if belanja_1006:
    kode_1006 |= 2

if barang_1006:
    kode_1006 |= 4

if promo_ada_1006:
    kode_1006 |= 8

# AND dan XOR
cek_member_1006 = kode_1006 & 1
cek_promo_1006 = kode_1006 & 8
hasil_xor_1006 = kode_1006 ^ 11

# ==========================================
# HASIL
# ==========================================

print("\n=== DATA PELANGGAN ===")
print("Nama          :", nama_1006)
print("Status        :", status_1006)
print("Total Belanja : Rp", harga_1006)
print("Jumlah Barang :", jumlah_1006)
print("Kode Promo    :", promo_1006)

print("\n=== HASIL VALIDASI ===")
print("Belanja >= 200000 :", belanja_1006)
print("Barang >= 3       :", barang_1006)
print("Member            :", member_1006)
print("Promo tersedia    :", promo_ada_1006)
print("Dapat Diskon      :", diskon_ok_1006)
print("Dapat Promo       :", promo_ok_1006)
print("Bukan Member      :", bukan_member_1006)

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon 10%        : Rp", diskon_1006)
print("Total Bayar       : Rp", total_1006)
print("Rata-rata Barang  : Rp", rata_1006)
print("Sisa Pembagian    :", sisa_1006)
print("Poin              :", poin_1006)

print("\n=== OPERATOR IDENTITY ===")
print("a is b            :", a_1006 is b_1006)
print("a is not b        :", a_1006 is not b_1006)
print("a == b            :", a_1006 == b_1006)

print("\n=== OPERATOR BITWISE ===")
print("Kode Biner        :", format(kode_1006, "04b"))
print("Kode Desimal      :", kode_1006)
print("Cek Member (&)    :", format(cek_member_1006, "04b"))
print("Cek Promo (&)     :", format(cek_promo_1006, "04b"))
print("Hasil XOR (^)     :", format(hasil_xor_1006, "04b"))