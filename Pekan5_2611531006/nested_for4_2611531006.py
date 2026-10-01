# Buat file dengan nama nested_for4_2611531006.py

tinggi_1006 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1006 % 2 !=0:
    print("Tinggi harus bilangan genap!")
else:
    a_1006 = tinggi_1006
    c_1006 = a_1006
    lebar_1006 = (2 * tinggi_1006) - 2
   
    for i_1006 in range(1, tinggi_1006 + 1):
        b_1006 = c_1006 + 1

        for j_1006 in range(1, lebar_1006 + 1):

            #Baris atas dan bawah
            if i_1006 == 1 or i_1006 == tinggi_1006:
                if j_1006 == 1 or j_1006 == lebar_1006:
                    print("#", end="")
                else:
                    print("=", end="")

            #Baris isi
            else:
                if j_1006 == 1 or  j_1006 == lebar_1006:
                    print("|", end="")
                else:
                    if j_1006 == c_1006:
                        print("<", end="")
                    elif j_1006 == b_1006:
                        print(">", end="")
                    elif j_1006 == (lebar_1006 - c_1006):
                        print("<", end="")
                    elif j_1006 == (lebar_1006 - c_1006 + 1):
                        print(">", end="")
                    elif j_1006 > b_1006 and j_1006< (lebar_1006 - c_1006):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()

        # Logika asli Java
        a_1006 -= 2

        if a_1006 <= 0:
            c_1006 = (-a_1006) +2
        else:
            c_1006 = a_1006