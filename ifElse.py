name = input("Adın ne? ") 
print("Senin adın: " + name)

if name == "Yasin":
    print("A")
elif name == "Ali" and name == "Veli": # pek doğru olmadı ama and konusu anlaşılsın yeter.
    print("B")
elif name == "Ayşe" or name == "Fatma":
    print("C")   
elif not(name == "Kemal"):
    print("D")
else:
    print("E")

age = int(input("Kaç yaşındasın? ")) # eğer kullanıcıdan sayı girmesini istiyorsan int veya float cast etmen gerekir.
print("Senin yaşın: " + str(age)) # consala bir şey yazdırmak istiyorsan strnin yanına int veya float koyamazsın cast etmen gerekir. DOĞRU.
# print("Senin yaşın: " + age) YANLIŞ.

if age >= 18:
    print("Yetişkinsin.")
elif age <= 0:
    print("Daha doğmamışsın bile.")
else: 
    print("Çocuksun.")    


    