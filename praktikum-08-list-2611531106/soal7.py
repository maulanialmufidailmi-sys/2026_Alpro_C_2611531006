menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

# 1. Baca data dengan nested loop dan simpan ke dalam list 2D sales
for day in range(1, number_of_days + 1):
    daily_sales = []
    for menu in menus:
        qty = int(input(f"Day {day}, {menu}: "))
        daily_sales.append(qty)
    sales.append(daily_sales)

# 2. Cetak total porsi setiap hari (traversal per baris)
print("Total per day:")
for i in range(number_of_days):
    daily_total = 0
    for j in range(len(menus)):
        daily_total += sales[i][j]
    print(f"Day {i + 1}: {daily_total}")

# 3. Hitung total setiap menu (traversal per kolom) dan simpan sebagai list of tuple
menu_totals = []
for j in range(len(menus)):
    menu_total = 0
    for i in range(number_of_days):
        menu_total += sales[i][j]
    menu_totals.append((menus[j], menu_total))

print(f"Total per menu: {menu_totals}")

# 4. Cari menu terlaris (jika sama, pilih yang muncul lebih dulu)
best_menu = menu_totals[0][0]
max_total = menu_totals[0][1]

for name, total in menu_totals:
    if total > max_total:
        max_total = total
        best_menu = name

print(f"Best seller: {best_menu} ({max_total})")