number_of_rows = 4
seats_per_row = 5
# Write your code below

# Membuat denah 4 baris x 5 kursi dengan list terpisah di tiap baris
denah = [["." for _ in range(seats_per_row)] for _ in range(number_of_rows)]
seats_taken = 0

while True:
    # Menampilkan denah kursi saat ini
    for i in range(number_of_rows):
        print(f"Row {i + 1}: {' '.join(denah[i])}")
    
    # Meminta input nomor baris
    row = int(input("Row (0 to stop): "))
    if row == 0:
        break
    
    # Meminta input nomor kursi
    seat = int(input("Seat: "))
    
    # Validasi rentang baris (1-4) dan kursi (1-5)
    if row < 1 or row > number_of_rows or seat < 1 or seat > seats_per_row:
        print("Invalid seat.")
    # Cek apakah kursi sudah terisi ('X')
    elif denah[row - 1][seat - 1] == "X":
        print("Seat already taken.")
    # Jika valid dan kosong, isi dengan 'X'
    else:
        denah[row - 1][seat - 1] = "X"
        seats_taken += 1
        print("Seat booked.")

# Mencetak total kursi yang dipesan setelah loop berhenti
print(f"Seats taken: {seats_taken}")