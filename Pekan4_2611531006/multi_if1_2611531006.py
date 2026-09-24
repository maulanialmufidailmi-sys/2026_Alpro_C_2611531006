# Program ini menggunakan fungsi input()

umur_1006 = int(input("Input umur Anda: "))
sim_1006 = input("Apakah Anda sudah punya SIM C (y/t): ")[0]

if umur_1006 >= 18 and sim_1006 == "y":
    print("Anda sudah dewasa dan boleh mengendarai sepeda motor")

if umur_1006 >= 18 and sim_1006 != "y":
    print("Anda sudah dewasa dan tidak boleh mengendarai sepeda motor")

if umur_1006 < 18 and sim_1006 == "y":
    print("Anda belum cukup umur punya SIM")

if umur_1006 < 18 and sim_1006 != "y":
    print("Anda belum cukup umur bawa motor")