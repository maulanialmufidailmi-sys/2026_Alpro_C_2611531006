phone = "081234567890"
masked = phone[:4] + "*" * 4 + phone[-3 :]
print(masked)

phone = "081234567890"
jumlah_bintang = len(phone) - 7
masked = phone[:4] + "*" * jumlah_bintang + phone[-3 :]
print(masked)
