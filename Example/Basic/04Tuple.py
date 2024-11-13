#Tuple giống như List nhưng nó có tính bất biến
#Khai báo một tuple như sau
mytuple = (1,2,3,4,5)
print(mytuple)
print(mytuple[1:3])
print(mytuple[0::2])
print(mytuple.count(2))
print(mytuple.index(4))
a,b,*c = mytuple
print(a)
print(b)
print(c)
#Tuple nhanh và tốn ít dữ liệu
#Tuple là bất biến