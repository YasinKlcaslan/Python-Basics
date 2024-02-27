#tuple : Sonradan eleman eklenemeyen listelerdir.
student = ("Bro",21,"male")

print(student.count("Bro")) # tuple'daki elemanın kaç kere yazıldığını gösterir.
print(student.index("Bro")) # tuple'daki istenen elemanın indexini yazdırır.
print(student)

for x in student:
    print(x, end=" ")

if "Bro" in student:
    print("\nBro is here")
print("######################")

# set : Küme. Sırasızdır(Her yazdırıldığında farklı çıktılar çıkar.).
utensils = {"fork", "spoon", "knife"}
print(utensils)
for x in utensils:
    print(x)

utensils.add("plate") # Kümeye eleman ekler.
utensils.remove("fork") # Kümeden eleman çıkarır. Eğer kümede silinecek eleman yoksa hata verir.
utensils.discard("fork") # Kümeden eleman çıkarır. Eğer kümede silinecek eleman yoksa hata vermez.
print(utensils)

set1 = {"white" ,"yellow", "red" ,"black"}
set2 = {"white" ,"yellow", "blue", "grey"}
print(set2.intersection(set1)) # 2 küme arasındaki aynı olan elemanları yazdırır. KÜMELERİN KESİŞİMİ
print(set2.union(set1)) # 2 küme içindeki elemanların hepsini yazdırır. KÜMELERİN BİRLEŞİMİ
print(set2.difference(set1)) # 2 küme içindeki farklı elemanları yazdırır. KÜMELERİN FARKI
set1.update(set2) # 2 kümeyi birbirine ekler
print(set1) 

print(set("ABCDEFG")) # Girilen string bu şekilde charlara bölünür.
print("######################")

# dictionary: {key : value}. Keyler string veya integer olmalı fakat valuelar her şey olabilir.
dict = {"Name" : "Yasin" , "Age" : 20 , "Hobies" : ["Entertainment", "Sofware", "Games"]}
print(dict)
print(dict["Name"])
dict["Name"] = "Ahmet"
print(dict)
dict.update({"Name": "Mehmet", "Age" : 30}) # Sözlüğü güncellemek için kullanılır.
print(dict)
dict["ID"] = 12345
print(dict)
del dict["ID"] # Sözlükteki keyleri silmek için kullanılır.
print(dict)

for i in dict: # Keyleri yazdırmak için kullanılan for.
    print(i, end=" ")
print()    
for i in dict: # Valueları yazdırmak için kullanılan for.
    print(dict[i], end=" ")   
print()
print(dict.keys()) # Keyleri yazdırır.
print(dict.values()) # Valueları yazdırır.   
print(dict.items()) # Keyleri ve valueları yazdırır.
dict.get("Name") # Böyle bir key olup olmadığını kontrol eder.