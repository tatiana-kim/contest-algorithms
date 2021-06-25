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
    # n, m, t = 6, 7, 38  # 2
    # n, m, t = 5, 20, 46  # 1
    # n, m, t = 20, 10, 144  # 3
    # n, m, t = 50, 50, 899  # 4
    # n, m, t = 50, 50, 900  # 5 (not here?)
    # n, m, t = 1600000000, 1450000000, 2310000003500000805  # answer: 700000007 (test 17)
    # n, m, t = 500, 1000, 100  # answer: 0 (test 13)
    l = 0
    r = (min(n, m) // 2)
    print(right_bin_search(l, r, checkwalkway, (n, m, t)))


def main_infile():
    f = open("G/input.txt", "r")
    lines = f.readlines()
    answer = [int(line.strip()) for line in lines]
    print(answer)
    f.close()

if __name__ == "__main__":
    main()
    # main_infile()
