import re

with open("/Users/kydyrtabyngalyyev/Desktop/ll6588/lab5/Новая папка 2/row.txt", encoding= "utf-8") as row:
    file = row.read()
a = re.findall(r"[a-zа-я]+_[a-zа-я]+" , file)
for i in a:
    print (i, end=" ")
