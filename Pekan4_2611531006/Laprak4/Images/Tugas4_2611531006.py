# =========================================================
# SISTEM LOKET TERPADU & AUDIT TRANSAKSI EKSPEDISI WAHANA
# =========================================================

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# -------------------------------
# 1. Input Data Pengunjung
# -------------------------------
nama_1006 = input("Masukkan Nama Pengunjung        : ")
umur_1006 = int(input("Input umur anda                 : "))
sim_1006 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].strip().lower()
jumlah_tiket_1006 = int(input("Masukkan jumlah tiket           : "))

# if tunggal - validasi kelogisan jumlah tiket
if jumlah_tiket_1006 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")

# -------------------------------
# 2. Pemilihan Wahana (match-case)
# -------------------------------
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")
paket_1006 = int(input("Masukkan nomor paket (1-5)      : "))

match paket_1006:
    case 1:
        nama_wahana_1006 = "Wahana Safari Rimba"
        harga_satuan_1006 = 50000
    case 2:
        nama_wahana_1006 = "Wahana Arung Jeram"
        harga_satuan_1006 = 75000
    case 3:
        nama_wahana_1006 = "Wahana Motor ATV Ekstrim"
        harga_satuan_1006 = 120000
    case 4:
        nama_wahana_1006 = "Wahana Roller Coaster Kilat"
        harga_satuan_1006 = 100000
    case 5:
        nama_wahana_1006 = "Wahana All-Access VIP"
        harga_satuan_1006 = 220000
    case _:
        print("Paket wahana tidak valid!")
        sys.exit()

# -------------------------------
# 3. Input Member & Promo
# -------------------------------
is_member_1006 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_1006 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# -------------------------------
# 4. Validasi Izin Kendali Wahana
#    (if - elif - else, operator logika and/!=)
# -------------------------------
if paket_1006 == 3 and umur_1006 >= 17 and sim_1006 == 'y':
    status_akses_1006 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
elif paket_1006 == 3 and umur_1006 >= 17 and sim_1006 != 'y':
    status_akses_1006 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."
elif paket_1006 == 3 and umur_1006 < 17 and sim_1006 == 'y':
    status_akses_1006 = "Identitas tidak valid: Belum cukup umur memiliki SIM."
elif paket_1006 == 3 and umur_1006 < 17 and sim_1006 != 'y':
    status_akses_1006 = "Anda belum cukup umur dan tidak boleh bawa motor ATV."
elif paket_1006 != 3 and umur_1006 >= 10:
    status_akses_1006 = "Anda memenuhi syarat umur untuk menikmati wahana ini."
else:
    status_akses_1006 = "Anda belum cukup umur untuk menikmati wahana ini."

# -------------------------------
# 5. Akumulasi Diskon Bertingkat
#    (Multi-IF terpisah, bisa ditumpuk)
# -------------------------------
subtotal_1006 = harga_satuan_1006 * jumlah_tiket_1006
total_diskon_persen_1006 = 0

if subtotal_1006 >= 200000:
    total_diskon_persen_1006 += 10  # Diskon Belanja Besar

if is_member_1006 in ['y', 'ya']:
    total_diskon_persen_1006 += 5  # Diskon Member

if kode_promo_valid_1006 in ['y', 'ya']:
    total_diskon_persen_1006 += 15  # Diskon Voucher Promo

if jumlah_tiket_1006 >= 5:
    total_diskon_persen_1006 += 5  # Diskon Tambahan Rombongan

nominal_diskon_1006 = subtotal_1006 * (total_diskon_persen_1006 / 100)
total_bayar_1006 = subtotal_1006 - nominal_diskon_1006

# -------------------------------
# 6. Evaluasi Kelulusan Audit (if - else)
# -------------------------------
if total_bayar_1006 > 300000:
    catatan_layanan_1006 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_1006 = "Terima kasih telah berkunjung."

# -------------------------------
# 7. Output Rincian
# -------------------------------
print(f"\n--- KELAYAKAN PENGENDARA WAHANA ---")
print(f"Status Akses: {status_akses_1006}")

print(f"\n--- Rincian Pembayaran ---")
print(f"Wahana Dipilih   : {nama_wahana_1006}")
print(f"Subtotal Belanja : Rp {subtotal_1006:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_1006}% (Rp {nominal_diskon_1006:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_1006:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_1006}")
print("Program Selesai")