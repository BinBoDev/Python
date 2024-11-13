#list là một collection
# Tạo  một list
list1 = [1,2,3,4,5]
list2 =["Tấn","Dung","Bống","Bin"]
#Truy cập các phần tử trong list bằng index
print(list2[1])
print(list2[-1]) # truy cập phần tử cuối list
# Thay đổi các phần tử trong  list
list1[4] = 6
print(list1)
#append() thêm vào cuối list
list1.append(7)
#insert(index,value)
list1.insert(0,0);
print(list1)

#xóa phần tử
# list1.pop()
# print(list1)
list1.remove(7)
print(list1)
#Duyệt list vơí vòng lặp for
for num in list1:
    print(num)
# Sử dụng enumerate để có cả index và value
for index,num in enumerate(list1):
    print(f"{index} <-> {num}")
#Toán tử trong list gồm '+' và '*' để cộng 2 list và lặp lại
print(list1*2)
#slice trong list cú pháp list[start,end,step]
print(list1[:3])

#comprehension
listEvenSub = [x for x in list1 if x%2 == 0]
print(listEvenSub)