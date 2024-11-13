#Note về Data Type
#Str không có chức năng gán
s = 'Lian'
# Muon thay doi phai
s = 'B' + s[1:]
print(s)
#Chuyen doi qua laij giua list va string nhu sau
L = list(s)
print(L)
s1 = ''.join(L)
print(s1)
s2 = str(L)
print(s2)
