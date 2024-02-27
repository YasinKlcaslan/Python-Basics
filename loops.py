#WHILE LOOP: sonsuza kadar giden kodlar için kullanılır.
name = ""

while len(name) == 0:
    name = input("Adın ne? : ")

print("Senin adın: " + name)

#FOR LOOP: belli bir aralıkta olan kodlarda kullanılır.
for i in range(10,15): #in range(start,stop,step) step girilmediği zaman step 1 olarak kabul edilir.
    print(i)

for i in range(5): # start noktası yazılmadığı zaman start noktası 0 olarak kabul edilir.
    print(i)

for i in range(10,5,-1):
    print(i) 

#NESTED LOOP
satir = int(input("Satır sayısı giriniz: "))
sutun = int(input("Sütun sayısı giriniz: "))

for i in range(satir):
    for k in range(sutun):
        print("*", end=" ")
    print()    