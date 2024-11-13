#collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
from collections import  namedtuple

from pyodbc import connect

# Student = namedtuple('Student',['Name','Age','Maso'])
# Student1 = Student('Tấn','42','TDh1')
# print(Student1.Name)
# print(Student1[1])
#Dung hàm make()
family = namedtuple('family',['Ten','Tuoi','Lop'])
import  csv
with open("Document/Csvtest.csv","r",encoding="utf-8") as csvfile:
    csv_reder = csv.reader(csvfile)
    for fem in map(family._make,csv_reder):
        print(fem.Ten)

#Vi du them ve map
mylist = [1,2,3,4,5]
mylist1 = map(lambda x:x*2,mylist)
print(list(mylist1))
#Lay du liệu từ một SQL Server
import pyodbc
connection_string = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-7E0C4GH\SQLEXPRESS;"
    "Database=DXSP;"
    "UID=sa;"
    "PWD=binbong1215;"
)
try:
    conn = pyodbc.connect(connection_string)
    print("Ket noi OK")
except Exception as e:
    print(e)

Account = namedtuple('Account',['id','UserName','PassWord','Type'])
cusor = conn.cursor()
query = "Select * from Account"
cusor.execute(query)
for acc in map(Account._make,cusor.fetchall()):
    print(list(acc))