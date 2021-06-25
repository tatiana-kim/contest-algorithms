def right_bin_search(left, right, check, checkparams):
    while left < right:
        middle = (left + right + 1) // 2
        if check(middle, checkparams):
            left = middle
        else: 
            right = middle - 1
    return left


def checkwalkway(largeur, params):
    n, m, t = params
    return n * m - ((n - 2 * largeur) * (m - 2 * largeur)) <= t


def main():
    n, m, t = [int(input()) for i in range(3)]
    l = 0
    r = min(n, m) // 2
    print(right_bin_search(l, r, checkwalkway, (n, m, t)))


def main_infile():
    f = open("G/input.txt", "r")
    lines = f.readlines()
    answer = [int(line.strip()) for line in lines]
    print(answer)
    f.close()


def tests(algo):
    l = 0

    n, m, t = 6, 7, 38  # 2
    r = min(n, m) // 2
    algo(l, r, checkwalkway, (n, m, t)) == 2, "WA :("

    n, m, t = 5, 20, 46  # 1
    r = min(n, m) // 2
    algo(l, r, checkwalkway, (n, m, t)) == 1, "WA :("

    n, m, t = 20, 10, 144  # 3
    r = min(n, m) // 2
    algo(l, r, checkwalkway, (n, m, t)) == 3, "WA :("

    n, m, t = 50, 50, 899  # 4
    r = min(n, m) // 2
    algo(l, r, checkwalkway, (n, m, t)) == 4, "WA :("

    n, m, t = 50, 50, 900  # 5 (not here?)
    r = min(n, m) // 2
    algo(l, r, checkwalkway, (n, m, t)) == 5, "WA :("

    n, m, t = 500, 1000, 100  # (test 13)
    r = min(n, m) // 2
    algo(l, r, checkwalkway, (n, m, t)) == 0, "WA :("

    n, m, t = 1600000000, 1450000000, 2310000003500000805  # (test 17)
    r = min(n, m) // 2
    algo(l, r, checkwalkway, (n, m, t)) == 700000007, "WA :("


if __name__ == "__main__":
    main()

# if you want read input from file: replace main() call by main_infile() call
# if you want launch tests replace main() by tests(right_bin_search)
