# Buat program untuk kondisional if_elif_else1_nim.py
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1006
# Program ini menggunakan fungsi input()

umur_1006 = int(input("Input umur Anda: "))
sim_1006 = input("Apakah anda sudah punya sim C: :)[0]")

if umur_1006 >= 18 and sim_1006 == "y":
    print("Anda sudah dewasa dan boleh mengendarai sepeda motor")
elif umur_1006 >= 18 and sim_1006 != "y":
    print("Anda sudah dewasa dan tidak boleh mengendarai sepeda motor")
elif umur_1006 < 18 and sim_1006 == "y":
    print("Anda belum cukup umur punya SIM")
else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program selesai")