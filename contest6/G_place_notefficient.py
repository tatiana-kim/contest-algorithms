# that algorithm works but take a very long time. So not efficient

def checkwalkway(tothrow, params):
    n, m, t = params
    k = tothrow // 2 + 1
    a = [tothrow // i for i in range(1, k) if tothrow % i == 0] + [1]
    ln = len(a)

    for i in range(ln):  # [6, 3, 2, 1]
        if ((n - a[i]) % 2 == 0) and ((m - (a[ln - 1 - i])) % 2 == 0):
            if ((n - a[i]) // 2) == ((m - (a[ln - 1 - i])) // 2):
                return (n - a[i]) // 2

    return False


def main():
    n, m, t = [int(input()) for i in range(3)]
    l = n * m - t
    r = n * m
    for noused in range(l, r):
        answer = checkwalkway(noused, (n, m, t))
        if answer:
            return answer
    return 0


if __name__ == "__main__":
    print(main())
