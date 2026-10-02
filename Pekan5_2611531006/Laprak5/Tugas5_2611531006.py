# Nama Berkas: tugas5_2611531006.py
# Program Pola Jam Pasir Kristal Palindromik Berbingkai

print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

# Input nilai N secara dinamis
n_1006 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Bingkai Pembatas Horizontal Atas
print("#", end="")
for i_1006 in range(4 * n_1006 + 5):
    print("=", end="")
print("#")

# Fase 1: Jam Pasir Atas (Baris N turun sampai 1)
for baris_1006 in range(n_1006, 0, -1):
    print("| ", end="")
    
    # Spasi penyeimbang kiri: 2 * (N - baris)
    for spasi_1006 in range(2 * (n_1006 - baris_1006)):
        print(" ", end="")
        
    # Deret angka mundur (baris turun ke 1)
    for angka_1006 in range(baris_1006, 0, -1):
        print(angka_1006, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju (1 naik ke baris)
    for angka_1006 in range(1, baris_1006 + 1):
        print(" ", end="")
        print(angka_1006, end="")
        
    # Spasi penyeimbang kanan: 2 * (N - baris)
    for spasi_1006 in range(2 * (n_1006 - baris_1006)):
        print(" ", end="")
        
    print(" |")

# Fase 2: Poros Titik Pusat Jam Pasir (Singularity)
print("|", end="")

# Spasi penyeimbang kiri: 2 * N + 1
for spasi_1006 in range(2 * n_1006 + 1):
    print(" ", end="")
    
print("<*>", end="")

# Spasi penyeimbang kanan: 2 * N + 1
for spasi_1006 in range(2 * n_1006 + 1):
    print(" ", end="")
    
print("|")

# Fase 3: Jam Pasir Bawah (Baris 1 naik sampai N)
for baris_1006 in range(1, n_1006 + 1):
    print("| ", end="")
    
    # Spasi penyeimbang kiri: 2 * (N - baris)
    for spasi_1006 in range(2 * (n_1006 - baris_1006)):
        print(" ", end="")
        
    # Deret angka mundur (baris turun ke 1)
    for angka_1006 in range(baris_1006, 0, -1):
        print(angka_1006, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju (1 naik ke baris)
    for angka_1006 in range(1, baris_1006 + 1):
        print(" ", end="")
        print(angka_1006, end="")
        
    # Spasi penyeimbang kanan: 2 * (N - baris)
    for spasi_1006 in range(2 * (n_1006 - baris_1006)):
        print(" ", end="")
        
    print(" |")

# Fase 4: Bingkai Pembatas Horizontal Bawah
print("#", end="")
for i_1006 in range(4 * n_1006 + 5):
    print("=", end="")
print("#")