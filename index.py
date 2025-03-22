a = 10
b = a + 10

obj = {
    "nama": "abdul salam",
    "usia": 10,
}

# percabangan
# AND
# 1 0 -> 0
# 0 1 -> 0
# 1 1 -> 1
# 0 0 -> 0

# OR
# 1 0 -> 1
# 0 1 -> 1
# 1 1 -> 1
# 0 0 -> 0
if a >= 10 or obj["usia"] > 10:
    print("nilai a lebih dari 10")
else:
    print("nilai a lebih kecil dari 10")

print(obj["nama"])

schema = {
    'H': 'Ke atas',
    'I': 'Ke bawah',
}

# time complexity, space complexity -> Big O Notation

def recursion():
    lokasi = input("Masukkan lokasi (H untuk hutan, G untuk gurun, P untuk pegunungan): ")
    
    if lokasi > 'H':
        print("Berjalanlah 100 langkah ke utara.")
    elif lokasi < 'G':
        print("Berjalanlah 50 langkah ke timur.")
    elif lokasi >= 'P':
        print("Mendakilah 20 langkah ke atas.")
    else:
        recursion()
    
    # lebih dari 1
    match lokasi:
        case "H": print("Atas")
        case "G": print("Bawah")
        case "J": print("Bawah")
        case _: recursion()

# perulangan.
# 1,2,3,4,5,
# print(1)
# print(2)
# print(3)
# print(4)

# proses dengan pattern sama, tapi output/logic nya berbeda
# ketika buat variable -> ada kotak dalam memory komputer
# istilah untuk nomor yang dimulai dari 0 -> index
n = 10
x = (1, "x", "1", True) # tupple -> seperti list

# for x in range(1, n + 1, 2):
#     print(x)

# n = 5
# i = 1
# x = "sabtu"
# while(x != "sabtu"):
#     print(i)
    
#     i = i + 1
# iteration-1
# i = 1
# n = 5
# apakah 1 <= 5, betul
# maka print
# maka nilai i = 1 + 1 => 2

# iteration-2
# i = 2
# n = 5
# apakah 2 <= 5, betul
# maka print
# maka nilai i = 2 + 1 => 3

# buatlah program untuk mencetak bilangan genap dari 1-100.
for x in range(1, 101, 1):
    if x % 2 != 0: # pakai modulus
        print(x)

for x in range(1,5):
    for j in range(1,5):
        print("*", end="")
    print()

# 1. buat segitiga dengan konsep loop
# jadi masukan n = 5
# *
# **
# ***
# ****
# *****

# 2. pengulangan yang recursion, tidak pakai recursion -> tapi pakai loops/pengulangan

nama = "robby"