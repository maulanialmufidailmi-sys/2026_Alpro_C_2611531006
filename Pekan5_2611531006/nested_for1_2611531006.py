# Buat file dengan nama nested_for1_2611531006.py

batas_1006 = int(input("Masukkan nilai batas: "))
for line_1006 in range(1, batas_1006 + 1):
    for j_1006 in range(1, (-1 * line_1006 + batas_1006) + 1):
        print(".", end=" ")
    print(line_1006,)