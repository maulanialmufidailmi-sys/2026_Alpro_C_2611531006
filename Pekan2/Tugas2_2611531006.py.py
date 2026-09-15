from typing import Final

# Deklarasi Konstanta (Penggunaan Final)
BATAS_LULUS_1006: Final[float] = 75.0

# === INPUT DATA PRAKTIKAN ===
print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

# String
nama_1006 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_1006 = input("Masukkan Jenis Kelamin (L/P): ")

# Multiline String untuk alamat
print("Masukkan Alamat Domisili (tekan Enter 3x untuk baris):")
jalan_1006 = input("  Jalan/Kampus : ")
kecamatan_1006 = input("  Kecamatan    : ")
kota_1006 = input("  Kota         : ")

alamat_1006 = f"""{jalan_1006},
Kecamatan {kecamatan_1006},
Kota {kota_1006}"""

# Numerik (Type Casting int & float)
umur_1006 = int(input("Masukkan Umur : "))
skor_tes_1006 = float(input("Masukkan Skor Tes Awal : "))

# Bilangan Kompleks (Token Identifikasi)
token_id_1006: complex = 100 + 3j

# Boolean (Evaluasi Status Kelulusan)
status_lulus_1006: bool = skor_tes_1006 >= BATAS_LULUS_1006


# === OUTPUT DATA & PEMERIKSAAN TIPE DATA ===
print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa : {nama_1006} | Tipe: {type(nama_1006)}")
print(f"Jenis Kelamin  : {jenis_kelamin_1006} | Tipe: {type(jenis_kelamin_1006)}")
print(f"Alamat Domisili:\n{alamat_1006} | Tipe: {type(alamat_1006)}")
print(f"Umur           : {umur_1006} tahun | Tipe: {type(umur_1006)}")
print(f"Skor Tes Awal  : {skor_tes_1006} | Tipe: {type(skor_tes_1006)}")
print(f"ID Token Sinyal: {token_id_1006} | Tipe: {type(token_id_1006)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai: {BATAS_LULUS_1006}")
print(f"Apakah Dinyatakan Lulus?: {status_lulus_1006} | Tipe: {type(status_lulus_1006)}")