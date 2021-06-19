def left_bin_search(left, right, check, checkparams):
    while left < right:
        middle = (left + right) // 2
        if check(middle, checkparams):
            right = middle
        else: left = middle + 1
    return left


def checkboard(xlength, params):
    width, height, number = params
    return (xlength // width) * (xlength // height) >= number


def main():
    w, h, n = list(map(int, input().split()))
    left = 0  # or left = w
    right = max(w * n, h * n)
    print(left_bin_search(left, right, checkboard, (w, h, n)))


def test(algo):
    w, h, n = 2, 3, 10
    right = max(w * n, h * n)
    assert algo(0, right, checkboard, (w, h, n)) == 9, "WA :("
    print("Test 1: Ok")


if __name__ == "__main__":
	main()


# if You want to launch the test,
# replace "main()" by "test(left_bin_search)" in the last line
