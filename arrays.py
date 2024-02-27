#ARRAYS
array = ["ahmet","mehmet","ali","ayşe","fatma"]

# arraydeki elemanları tek tek yazdırma.
for i in array:
    print(i, end = " ")

print(array[0])
print(array[1])
print(array[2])
print(array[3])
print(array[4])
# print(array[5]) hata "list index out of range".

# array.append("abcd") arraye eleman eklemek için kullanılır.
# array.remove("ali") arrayden eleman silmek için kullanılır.
# array.pop() arraydeki son elemanı siler.
# array.insert(0,"eleman") arraydeki istenilen indexe istenilen elemanı ekler.

#MULTIPLE ARRAYS: bir arrayin elemanlarının arraylerden oluşması
array1 = ["ali","veli","mehmet","ahmet"]
array2 = ["ayşe","fatma","hatice","nur"]
array3 = [array1,array2]
# array3 = [["ali","veli","mehmet","ahmet"],["ayşe","fatma","hatice","nur"]]
print(array3[1][3])
