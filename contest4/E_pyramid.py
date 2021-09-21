n = int(input())

choosed_blocks = {}  # only different widths having the maximum heights
for i in range(n):
    width, height = list(map(int, input().split()))
    if width in choosed_blocks:
        choosed_blocks[width] = max(choosed_blocks[width], height)
    else:
    	choosed_blocks[width] = height

answer = sum(choosed_blocks.values())
print(answer)


#----------------------------------------
# sample inputs:
"""
3
3 1
2 2
3 3
"""
"""
10
46 64
29 46
2 66
3 18
47 2
47 79
54 44
45 56
93 62
99 34
"""

#----------------------------------------
# solution from stackoverflow:
# d = {}

# for a in range(int(input())):
#   [h, w] = map(int, input().split(" "))
#   print([h, w])
#   d[h] = max(d.get(h, w), w)
#   print(d[h])

# print("d:", d)

# print(sum(d.values()))
