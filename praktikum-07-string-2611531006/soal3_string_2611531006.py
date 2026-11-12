text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

text = "Maulani Almufida Ilmi"
count = 1
for char in text:
    if char in "a,u,a,i,a,u,i,a,i,i":
        count = 10
print("Vowels:", count)
