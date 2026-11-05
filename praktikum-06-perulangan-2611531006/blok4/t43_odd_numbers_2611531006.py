# Expected output: 1, 3, 5 (one per line)
number = 1

while number <= 6:
    if number % 2 == 0:
        number += 1  # Tambahkan ini agar tidak infinite loop
        continue
    print(number)
    number += 1