#Đặc trưng cảu Set là các phần tử là duy nhất,không lặp lại và không có thứ tự
from itertools import starmap

set1 ={1,2,3,4}
set2 = {6,2,3,5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set2.__class__)

print(set.__doc__)
