def binary(a, b, n):
    lefta = leftb = 0
    righta = rightb = n - 1

    if n == 1:
        return min(a[0], b[0])

    while ((righta - lefta) + 1) > 2:
        length = (righta - lefta) + 1
        ma = (lefta + righta) // 2
        mb = (leftb + rightb) // 2
        if length % 2 == 0:
            mb += 1
        if a[ma] > b[mb]:
            righta = ma
            leftb = mb
        else:
            lefta = ma
            rightb = mb

    s = sorted(a[lefta: righta+1] + b[leftb: rightb+1])
    return s[1]


def main():
    arr = []
    n, l = map(int, input().split())
    for i in range(n):
        x1, d1, a, c, m = map(int, input().split())
        x = [x1] + [0 for i in range(l-1)]
        d = [d1] + [0 for i in range(l-1)]
        for i in range(1, l):
            d[i] = (a * d[i - 1] + c) % m
            x[i] = x[i - 1] + d[i - 1]
        arr.append(x)

    for i in range(n):
        for j in range(i+1, n):
            print(binary(arr[i], arr[j], l))

main()
