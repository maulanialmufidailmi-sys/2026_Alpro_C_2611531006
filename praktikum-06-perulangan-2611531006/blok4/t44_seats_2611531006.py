# Membaca input blocked_seat
blocked_seat = int(input("Masukkan blocked_seat: "))

# Nested loop untuk baris dan kursi
for row in range(1, 4):
    print(f"Row {row}:", end=" ")
    for seat in range(1, 6):
        if seat == blocked_seat:
            break
        print(seat, end=" ")
    print()  # Berpindah ke baris baru setelah selesai satu Row