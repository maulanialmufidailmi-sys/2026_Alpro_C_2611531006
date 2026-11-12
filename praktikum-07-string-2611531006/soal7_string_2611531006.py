# Menyimpan data ke dalam variabel
name = "maulani almufida ilmi"
nim = "2611531006"
username = "maulani123"

# Mengambil tahun angkatan dari 2 digit pertama NIM menggunakan slicing
intake = "20" + nim[:2]

# Menampilkan kartu mahasiswa dengan lebar 30 karakter
print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)