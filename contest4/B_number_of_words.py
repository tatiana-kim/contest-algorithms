# B_number_of_words.py
f = open("input.txt", "r")

words = f.read().strip().split()
count = {}

for i in words:
    if i not in count:
        count[i] = 0
    print(count[i], end=" ")
    count[i] += 1

f.close()
