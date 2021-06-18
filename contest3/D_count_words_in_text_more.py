import re

f = open("D/input.txt")

text = []
for i in f.readlines():
    a = i.strip()
    a = re.split('[; , .]', a)
    a = ' '.join(a).split()
    text += a

print(len(set(text)))

f.close()
