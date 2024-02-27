print("ali Mehmet AYŞE 1 2 3 123")

a = 1
print(a)
print(type(a))

b = 1.0
print(b)
print(type(b))

c = "abc"
print(c)
print(type(c))

d = 'd'
print(d)
print(type(d))

e = False
print(e)
print(type(e))

#print("a" + 1) # bunu kullanamazsın cast etmen lazım.
print("a"+str(1))

name,age,are_u_human = "yasin",20,True
print(name,age,are_u_human)

ali = veli = mehmet = ayşe = fatma = 20
print(ali,veli,mehmet,ayşe,fatma)

print(len("ali")) # len = length inputun uzunluğunu verir.

Bro = "Bro"
print(Bro.find("B")) # find fonksiyonu kelimedeki harfi bulmanı sağlar. (ÖNEMLİ: Kelimeleri her zaman 0. indexten başlat.)
print(Bro.replace("B","K")) # replace fonksiyonu kelimedeki istediğin bir harfi başka bir harfle değiştirmeni sağlar. hatta harfi silip yerine boşluk bile atayabilirsin.

ahmet = "ahmetmehmet"
ahmet2 = ahmet[2:10:3] # string slice işlemi [start:stop:step].
print(ahmet2)
print(ahmet[0:10:4]) #ikisi de olur.