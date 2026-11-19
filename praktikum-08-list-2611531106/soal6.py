LAST_DIGIT = 6  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

# Membaca 7 pengeluaran harian
for i in range(7):
    pengeluaran = int(input(f"Day {i + 1}: "))
    expenses.append(pengeluaran)

# Menghitung total, tertinggi, dan jumlah hari di atas batas secara manual
total = 0
highest_amount = expenses[0]
highest_day = 1
days_above_limit = 0

for i in range(len(expenses)):
    amount = expenses[i]
    total += amount
    
    # Menggunakan > agar jika ada nilai sama, hari pertama tetap dipertahankan
    if amount > highest_amount:
        highest_amount = amount
        highest_day = i + 1
        
    if amount > daily_limit:
        days_above_limit += 1

average = total / 7

# Mencetak 5 baris output sesuai format
print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest_amount})")
print(f"Days above limit: {days_above_limit}")