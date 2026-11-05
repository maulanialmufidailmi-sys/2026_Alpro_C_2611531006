# BACA height
height = int(input("Masukkan tinggi: "))

# UNTUK row DARI 1 SAMPAI height
for row in range(1, height + 1):
    
    # UNTUK column DARI 1 SAMPAI row
    for column in range(1, row + 1):
        # TAMPILKAN column DAN satu spasi, TANPA pindah baris
        print(column, end=" ")
        
    # PINDAH BARIS
    print()