f = open("input.txt", "r")
next(f)  # pass the first line
# read the sequence of chars in a list and making them integers
seq = [int(i) for i in next(f).strip().split()]
f.close()
