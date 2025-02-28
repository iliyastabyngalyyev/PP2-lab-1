import re

text = "abc abc abcxyz abcdfd bcv"
pattern = r"c"
matches = re.findall(pattern, text)
print(matches)

