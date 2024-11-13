import  platform
import os
import psutil
print("He dieu hanh",platform.system())
print("Phien ban HDH",platform.release())
print("Ten phien ban HDH",platform.version())
print("So bit cau Laptop",platform.processor())
print("Ten may tinh",platform.node())
print("Ten day du",platform.uname())
print(os.environ)
print(psutil.cpu_count(logical=True))
print(psutil.cpu_count(logical=False))
ram = psutil.virtual_memory()
print("Dung luong Ram",ram.total / (1024**3),"GB")
print("Dung luong Ram dang dung",ram.used / (1024**3),"GB")
net = psutil.net_if_addrs()
print("Infomation NeT")
for interfsce_nam,interface_address in net.items():
    for address in interface_address:
        if address.family == psutil.AF_LINK:
            print(f"Interfacename:{interfsce_nam}")