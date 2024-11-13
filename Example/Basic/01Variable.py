#Phân biệt chữ hoa chữ thường
# x= 12
# X= 'Bian'
# print(x)
# print(X)
#Casting trong python giữa các kiểu : int,float,string,tuple,set,list,...
# a = "10"
# print(int(a) +1)
#Chuyển đổi các kiểu tuple,list,set
# mylist = list((1,2,3)) #Chuyển từ tuple sang list
# mytuple = tuple([1,2,3]) #Chuyển từ list sang tuple
# myset = set((1,2,3)) #Chuyển từ tuple sang set
# print(mylist)
# print(myset)
# print(mytuple)
#Type của biến
# x= 3
# y= 3.14
# z = "Bian"
# mylist = [1,2,3]
# mytuple = (1,2,3)
# myset = {1,2,3}
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(mylist))
# print(type(mytuple))
# print(type(myset))
#Bạn có thể khai báo nhiều biến như sau
# x,y,z = 1,2,3
# x,y,z = "Bian","Bong","Bin"
# print(x)
# print(y)
# print(z)
#Unpack Collection
#Unpack tuple
# person = ("Bong",12,"6A1")
# x,y,z = person
# print(x)
# print(y)
# print(z)
#Có thể dùng dấu "*" để đại diện cho các phần tử còn lại
# numbers = (1,2,3,4,5,6,7,8,9,10)
# x,*y,z = numbers
# print(x)
# print(y)
# print(z)
#Unpack trong vòng lặp for theo ví dụ sau
# mylist = [(1,2),(3,4),(5,6)]
# for x,y in mylist:
#     print(f"x:{x} y:{y}")
#
#Unpack trong Dictionary
# myDic = {"name":"Bống","age":"13","class":"7A1"}
# key = list(myDic)
# print(key)
# value = list(myDic.values())
# print(value)
# for key,value in myDic.items():
#     print(f"{key}:{value}")

#Nhiều layer chồng nhau
# mylist = [(("Bống"),(13,"7A1")),(("Bin"),(9,"4E"))]
# for name,(age,lop) in mylist:
#     print(f"Tên là {name} ,{age} tuổi học lớp {lop}  ")

