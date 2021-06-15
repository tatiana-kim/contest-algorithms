"""
F_vents.py
"""

f = open("F/input3.txt", "r")
lines = f.readlines()

f.close()

lst = []
for line in lines:
	lst.append(line.strip("\n").split())

print(lst[-1])
