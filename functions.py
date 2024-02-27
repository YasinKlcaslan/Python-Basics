def function(isim):
    print("Merhaba " + isim)
    print("Ben bir fonksiyonum.")

isim = input("İsminiz nedir?: ")
function(isim)

num1 = int(input("num1:"))
num2 = int(input("num2:"))

def multi (num1,num2):
    return num1*num2

print(multi(num1,num2))