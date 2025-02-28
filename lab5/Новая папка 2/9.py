import re

def spaces(text):
    res = ""
    pattern = re.compile(r"[a-zа-я\d]+|[A-ZА-Я][a-zа-я]*")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += " " + word
        else:
            res += word
    return res
with open("/Users/kydyrtabyngalyyev/Desktop/ll6588/lab5/Новая папка 2/row.txt", "r", encoding="utf-8") as row:
    file = row.read()
a = spaces(file)
print(a)