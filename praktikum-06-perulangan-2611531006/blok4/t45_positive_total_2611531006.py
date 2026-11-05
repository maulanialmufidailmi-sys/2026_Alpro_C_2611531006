total = 0

while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
        # Bilangan negatif menghentikan loop
        break
    elif number == 0:
        # Bilangan 0 dilewati
        continue
    else:
        # Bilangan positif ditampilkan dan dijumlahkan
        print(f"Positive number: {number}")
        total += number

# Setelah loop selesai, tampilkan Total
print(f"Total: {total}")