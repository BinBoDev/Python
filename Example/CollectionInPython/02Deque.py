#Deque có thể hiểu là hàng đợi list 2 đầu với tốc độ truy cập nhanh với các lệnh append() và pop()
#phân biệt append() và appendleft() cũng như pop() và popleft()
from  collections import  deque
d = deque([1,2,3,4])
d.append(5)
print(d)
d.appendleft(0)
d.rotate(3)
print(d)