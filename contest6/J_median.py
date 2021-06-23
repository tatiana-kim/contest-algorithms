def binary(a, b, n):
    lefta = leftb = 0
    righta = rightb = n - 1

    if n == 1:
        return min(a[0], b[0])
    if n == 2:
        s = sorted(a + b)
        return s[1]

    while ((righta - lefta) + 1) > 2:
        # find median for a and median b
        # if length of list is even:
        length = (righta - lefta) + 1
        if length % 2 == 0:
            ma = (lefta + righta) // 2
            mb = (leftb + rightb) // 2 + 1
        # if odd:
        else:
            ma = (lefta + righta) // 2
            mb = (leftb + rightb) // 2
        #
        if a[ma] > b[mb]:
            righta = ma
            leftb = mb
        else:
            lefta = ma
            rightb = mb


    s = sorted(a[lefta: righta+1] + b[leftb: rightb+1])
    return s[1]


def permutate(arr, n, l):
    for i in range(n):
        for j in range(i+1, n):
            print(binary(arr[i], arr[j], l))


n, l = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
permutate(arr, n, l)


# def permutate_file(arr, n, l):
#     f = open("J/output6-3.txt", "w")
#     for i in range(n):
#         for j in range(i+1, n):
#             answer = binary(arr[i], arr[j], l)
#             f.writelines(f'\n{answer}')
#     f.close()


# f = open("J/input6.txt", "r")
# n, l = [int(i) for i in next(f).strip().split()]
# lines = f.readlines()
# arr = []
# for line in lines:
#     arr.append([int(i) for i in line.strip().split()])
# f.close()

# permutate_file(arr, n, l)
# permutate(arr, n, l)














# n, l = 6, 1
# arr = [[120], [120], [130], [130], [120], [120]]
# permutate(arr, n)


# n, l = 3, 6
# arr1 = [[1, 4, 7, 10, 13, 16], [0, 2, 5, 9, 14, 20], [1, 7, 16, 16, 21, 22]]
# permutate(arr1, n)

# a = [1, 4, 7, 10, 13, 16]
# b = [0, 2, 5, 9, 14, 20]
# c = [1, 7, 16, 16, 21, 22]
# print(binary(a, b))
# print(binary(a, c))
# print(binary(b, c))

# -----------------------
# n, l = 4, 20
# arr2 = [[-1128, -869, -492, -103, 119, 250, 291, 592, 980, 1249, 1553, 1800, 1947, 2030, 2342, 2610, 2961, 2984, 3337, 3663],
#      [-1492, -1414, -1408 -1238, -1103, -996, -856, -745, -491, -455, -261, 4, 215, 272, 372, 451, 624, 706, 826, 921],
#      [67, 105, 115, 142, 216, 250, 293, 342, 395, 415, 520, 539, 572, 650, 651, 672, 742, 809, 874, 902],
#      [-1434, -1357, -1217, -1163, -983, -975, -715, -528, -379, -376, -178, -1, 24, 278, 499, 636, 707, 881, 923, 1171]
#     ]
# permutate(arr2, n)

# a = [-1128, -869, -492, -103, 119, 250, 291, 592, 980, 1249, 1553, 1800, 1947, 2030, 2342, 2610, 2961, 2984, 3337, 3663]
# b =[-1492, -1414, -1408, -1238, -1103, -996, -856, -745, -491, -455, -261, 4, 215, 272, 372, 451, 624, 706, 826, 921 ]
# c =[67, 105, 115, 142, 216, 250, 293, 342, 395, 415, 520, 539, 572, 650, 651, 672, 742, 809, 874, 902]
# d = [-1434, -1357, -1217, -1163, -983, -975, -715, -528, -379, -376, -178, -1, 24, 278, 499, 636, 707, 881, 923, 1171]
# print(binary(a, b))
# print(binary(a, c))
# print(binary(a, d))
# print(binary(b, c))
# print(binary(b, d))
# print(binary(c, d))




