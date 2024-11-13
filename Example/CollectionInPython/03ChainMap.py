#Group dict
from  collections import ChainMap
dic1 ={'a':1,'b':2}
dic2 ={'c':3,'d':4}
chain = ChainMap(dic1,dic2)
print(chain)
print(chain['a'])
chain['e'] = 5
print(chain)
print(list(chain.values()))
print(list(chain.keys()))
#Mọi thao tác thay đổi chỉ xẩy ra ở Dict đầu tiên
#Các phương thức và thuộc tính #Chainmap(),