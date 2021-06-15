# dynamic programming
# n, k, m = map(int, input().split())
n, k, m = 10, 5, 2  # 4
n, k, m = 13, 5, 3  # 3
n, k, m = 14, 5, 3  # 4
n, k, m = 30, 5, 7
n, k, m = map(int, input().split())

products = 0
rest = []

if k >= m:
    while n >= k:
        blanks = n // k
        n %= k  # or: n -= blanks

        for i in range(blanks):
            products += k // m
            rest.append(k % m)

        n += sum(rest)
        rest = []

print(products)
