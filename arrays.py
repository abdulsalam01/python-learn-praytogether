# data structure -> array
data = 10
kumpulan_data1 = [10, 20, 30, 40, 50, 60, 100]
kumpulan_dataStr = ["abdul", "hanif"]
kumpulan_data2 = [1, 2, 3, 4]
# elemen -> nilai sesungguhnya
# index -> lokasi dari element dimulai dari 0
index = 0
# for i in kumpulan_data1:
#     print(f"angka {i}, index {index}")
#     # kumpulan_data1[index] = kumpulan_data1[index] + 10
#     index = index + 1

for i in kumpulan_dataStr:
    print(i + " salam")
# print(kumpulan_data1)

# array1: [1,2,3,4,5,6]
# array2: [3,4,5,6,7,8]

# result: 
# [4,6,8,10,12,14]

arr1 = [1,2,3,4,5,6]

# baris x kolom
arr2 = [ [10,20,30,50], [40,50,60], [70,80,90] ]
# max.index = panjang data - 1 -> 3
# buat 3 kotak
# tiap 1 kotak ternyata perlu 3 kotak kecil

for array_dimensi_luar in arr2: # [ [10,20,30], [40,50,60], [70,80,90] ]
    banyak_bilangan = 0
    for array_dimensi_dalam in array_dimensi_luar: # [10,20,30]
        # 10
        # 20
        # 30
        array_dimensi_luar[banyak_bilangan] = array_dimensi_luar[banyak_bilangan] + 1
        print(array_dimensi_luar[banyak_bilangan], end=" ")
        # print(array_dimensi_dalam + 1, end=" ")
        banyak_bilangan = banyak_bilangan + 1
    print("iterasi index max", banyak_bilangan - 1)

# tugas
# menjumlahkan kelompok data berdasarkan input
# scope boundary: panjang element array harus sama semua

# n = 3
# generate koleksi data ke-1 [1,2,3,4,5,6]
# generate koleksi data ke-2 [5,5,5,5,5,5]
# generate koleksi data ke-3 [7,7,7,7,7,7]

# result = koleksi data ke 1 + koleksi data ke 2 + koleksi data ke 3
# result = [13, 14, 15, 16, 17, 18, 19]

# procedure
def angka() -> None:
    hjaskhdsakjdhsakj + askjdasdkasl