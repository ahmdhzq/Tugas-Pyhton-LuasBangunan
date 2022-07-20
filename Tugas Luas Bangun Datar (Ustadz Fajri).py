# Nama    : Ahmad Haziq MU'izzaddin Wafiq
# Jurusan : Pengembangan Perangkat Lunak (PPL)
# Tugas   : Menghitung luas Bangun Datar

nama = input("Masukan Nama : ")
nim = input("Masukan NIM : ")

print()
print("="*30)
print("Welcome ",nama)
print("Your NIM ",nim)
print("="*30)

# soal 1
print("\nQuestion No.1\nDiketahui sisi = 6, sebutkan Nama dan hitunglah luas Bangun Datar tersebut!")
namaBD1 = input("Nama Bangun Datar = ") 
persegi1 = eval(input("Sisi : "))
persegi2 = eval(input("Sisi : "))
print("Bangun Datar tersebut adalah", namaBD1, "dan Luas Bangun Datar Tersebut adalah",persegi1 * persegi2)

# soal 2
print("\nQuestion No.2\nDiketahui Alas = 7, Tinggi = 8, Sebutkan Nama dan luas Bangun Datar tersebut!")
namaBD2 = input("Nama Bangun Datar = ") 
alasSgt = eval(input("Alas : "))
tinggiSgt = eval(input("Tinggi : "))
print("Bangun Datar tersebut adalah", namaBD2, "dan Luas Bangun Datar Tersebut adalah",(alasSgt * tinggiSgt)/2)

# soal 3
print("\nQuestion No.3\nDiketahui Panjang = 4, Lebar = 9, Sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
namaBD3 = input("Nama Bangun Datar = ") 
panjangPP = eval(input("Panjang : "))
lebarPP = eval(input("Lebar : "))
print("Bangun Datar tersebut adalah", namaBD3, "dan Luas Bangun Datar Tersebut adalah",panjangPP * lebarPP)

# soal 4
print("\nQuestion No.4\nDiketahui Jari-jari 56, Sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
namaBD4 = input("Nama Bangun Datar = ") 
pi = eval(input("π  : "))
jariJari = eval(input("r : "))
print("Bangun Datar tersebut adalah", namaBD4, "dan Luas Bangun Datar Tersebut adalah",pi * jariJari * jariJari)

# soal 5
print("\nQuestion No.5\nDiketahui Diagonal I = 4, Diagonal II = 8, Sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
namaBD5 = input("Nama Bangun Datar = ") 
d1 = eval(input("Diagonal I  : "))
d2 = eval(input("Diagonal II : "))
print("Bangun Datar tersebut adalah", namaBD5, "dan Luas Bangun Datar Tersebut adalah",(d1*d2)/2)

# soal 6
print("\nQuestion No.6\nDiketahui Sisi AB dan CD sejajar, sisi AB = 6, sisi CD = 8, tinggi = 3, Sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
namaBD6 = input("Nama Bangun Datar = ") 
sisiAB = eval(input("Sisi AB : "))
sisiCD = eval(input("Sisi CD : "))
tinggiTrs = eval(input("Tinggi : "))
print("Bangun Datar tersebut adalah", namaBD6, "dan Luas Bangun Datar Tersebut adalah",(sisiAB+sisiCD)*tinggiTrs/2)

# soal 7
print("\nQuestion No.7\nDiketahui sebuah jajar genjang dengan alas = 9, tinggi = 7, hitunglah Luas Bangun Datar tersebut!") 
alasJG = eval(input("Alas  : "))
tinggiJG = eval(input("Tinggi : "))
print("Luas Jajar Genjang adalah",alasJG*tinggiJG)

print()
print("."*43)
print("."," "*39,".")
print(".'Thank You Very Much For Your Attention'.")
print("."," "*39,".")
print("."*43)
