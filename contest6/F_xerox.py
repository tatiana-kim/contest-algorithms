# n = number of copies to print
# x = number of seconds what the first xerox need to print one copy
# y = number of seconds what the second xerox need to print one copy

def left_bin_search(left, right, check, checkparams):
    x, y = checkparams[1:]
    while left < right:
        middle = (left + right) // 2
        if check(middle, checkparams):
            right = middle
        else: left = middle + 1
    return left + min(x, y)


def checktime(totaltime, params):
    n, x, y = params
    return (totaltime // x) + (totaltime // y) >= n - 1


def main():
    n, x, y = list(map(int, input().split()))
    left = 0
    right = n * max(x, y)
    print(left_bin_search(left, right, checktime, (n, x, y)))


def tests(algo):
    left = 0

    n, x, y = 4, 1, 1
    right = n * max(x, y)
    assert algo(left, right, checktime, (n, x, y)) == 3, "WA :("
    print("Test 1: Ok")

    n, x, y = 5, 1, 2
    right = n * max(x, y)
    assert algo(left, right, checktime, (n, x, y)) == 4, "WA :("
    print("Test 2: Ok")


if __name__ == "__main__":
    main()

# if You want to launch the test,
# replace "main()" by "tests(left_bin_search)" in the last line
