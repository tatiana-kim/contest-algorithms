# C_most_frequent_word.py

f = open("C/input.txt", "r")
words = f.read().strip().split()
f.close()

count = {}
maxval = -1
tmp = ""
for i in words:
    if i not in count:
        count[i] = 0
    count[i] += 1
    
    if count[i] > maxval:
        maxval = count[i]
        tmp = i  # intermediate result = one of most frequent word

most_frequent_words = []
for i, j in count.items():
    if j == maxval:
        most_frequent_words.append(i)
        if i < tmp:
        	tmp = i

print(tmp)
