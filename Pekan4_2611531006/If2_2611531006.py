# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1006
# Program ini menggunakan fungsi input() 

ipk_1006= float(input("input IPK Anda = "))

if ipk_1006 > 2.75:
    print("Anda lulus sangat memuaskan dengan IPK " + str(ipk_1006))
else:
    print("Anda tidak lulus")
print("Program selesai")