#kondisi di python
if 5 * 2 == 10:
    print("benar")
else :
    print("salah")

if 10 % 2 == 0:
    print("bilangan genap")
#perulangan di python
for i in range(5):
    print("perulangan ke -", i)

#array:
nama = ["kipin", "bima", "el"]
print(nama[0]) #outputnya kipin
print(nama[1]) #outputnya bima 
print(nama[2]) #outputnya el

#menambahkan data di array
#.append(_isi)
nama.append("rizal")
print(nama) #outputnya ['kipin', 'bima', 'el', 'rizal']

#looping array:
for n in nama:
    print(n)
#outputnya:
#kipin
#bima
#el
#rizal

#string literals:
#f"ror${variabel}"
nama_depan = "kipin"
nama_belakang = "kipon"
print(f"hai nama lengkap saya adalah {nama_depan} {nama_belakang}")
#outputnya: hai nama lengkap saya adalah kipin kipon