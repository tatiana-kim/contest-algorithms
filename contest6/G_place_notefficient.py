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
    # n, m, t = 6, 7, 38  # 2
    # n, m, t = 5, 20, 46  # 1
    # n, m, t = 20, 10, 144  # 3
    # n, m, t = 50, 50, 899  # 4
    # n, m, t = 50, 50, 900  # 5 (not here?)
    # # test 17 takes a veeery long time:
    # n, m, t = 1600000000, 1450000000, 2310000003500000805  # answer: 700000007 (test 17)
    # n, m, t = 500, 1000, 100  # answer: 0 (test 13)
    l = n * m - t
    r = n * m
    for noused in range(l, r):
        answer = checkwalkway(noused, (n, m, t))
        if answer:
            return answer
    return 0


if __name__ == "__main__":
    print(main())
