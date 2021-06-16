"""
F_vents.py
"""
# read data
f = open("F/input.txt", "r")
lines = f.readlines()

f.close()

lst = []
for line in lines:
    lst.append(line.strip("\n").split())

if not lst[-1]:
    lst[:] = lst[:-1]

# create a dictionnary and write the data
d = {}
for i in lst:
    if i[0] not in d:
        d[i[0]] = {i[1]: int(i[2])}
    elif i[1] not in d[i[0]]:
        d[i[0]][i[1]] = int(i[2])
    else:  # i[1] in d[i[0]]
        d[i[0]][i[1]] += int(i[2])

# print the answer
for name, value in sorted(d.items()):
    print(f'{name}:')
    for product, amount in sorted(value.items()):
        print(product, amount)


"""
Ivanov:
envelope 5
marker 3
paper 17
Petrov:
envelope 20
pens 5
"""