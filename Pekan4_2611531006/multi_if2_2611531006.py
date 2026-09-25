# Nama variabel ditambah 4 digit nim terakhir contoh: total_belanja_1006
# Program ini menggunakan fungsi input()
# Program ini menghitung diskon belanja

# Input dari user
total_belanja_1006 = float(input("Input total belanja (Rp): "))

# Input status member (mengecek apakh user mengetuik 'y' atau 'ya'
input_member_1006 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member = input_member_1006 in ['y', 'ya']

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_1006 = input("Apakah Anda memiliki kode promo? (y/t): ").strip().lower()
kode_promo_valid = input_promo_1006 in ['y', 'ya']

total_diskon_persen_1006 = 0

# Multi-If terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_1006 > 1000000:
    total_diskon_persen_1006 += 10 # Diskon belanja besar

if is_member:
    total_diskon_persen_1006 += 5 # Diskon member

if kode_promo_valid:
    total_diskon_persen_1006 += 15 # Diskon kode voucher

# Menghitung nasional diskon dan total bayar
nominal_diskon_1006 = total_belanja_1006 * (total_diskon_persen_1006 / 100)
total_bayar_1006 = total_belanja_1006 - nominal_diskon_1006

# Output hasil
print(f"Total diskon : {total_diskon_persen_1006}% = Rp {nominal_diskon_1006:,.0f}")
print(f"Total bayar : Rp {total_bayar_1006:,.0f}")

print(f"Total diskon yang anda dapatkan adalah {total_diskon_persen_1006}%")
# Output: Total diskon yang anda dapatkan adalah: 30% jika belanja > 1 juta, member, dan memiliki kode valid 
