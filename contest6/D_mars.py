def right_bin_search(left, right, check, checkparams):
    while left < right:
        middle = (left + right + 1) // 2
        if check(middle, checkparams):
            left = middle
        else: 
            right = middle - 1
    return left


def check_defense(d, params):
    n, a, b, w, h = params
    return max((w//(a+2*d)) * (h//(b+2*d)), (w//(b+2*d)) * (h//(a+2*d))) >= n


def main():
    n, a, b, w, h = list(map(int, input().split()))
    left = 0
    right = min(w, h)
    print(right_bin_search(0, right, check_defense, (n, a, b, w, h)))


def tests(algo):
    left = 0

    n, a, b, w, h = 1, 1, 1, 1, 1
    right = min(w, h)
    assert algo(left, right, check_defense, (n, a, b, w, h)) == 0, "Test 1: Something get wrong :("
    print("Test 1: Ok :)")

    n, a, b, w, h = 1, 1, 1, 3, 3
    right = min(w, h)
    assert algo(left, right, check_defense, (n, a, b, w, h)) == 1, "Test 2: Something get wrong :("
    print("Test 2: Ok :)")

    n, a, b, w, h = 11, 3, 2, 21, 25
    right = min(w, h)
    assert algo(left, right, check_defense, (n, a, b, w, h)) == 2, "Test 3: Something get wrong :("
    print("Test 3: Ok :)")

    n, a, b, w, h = 1, 1, 1, 1000, 1
    right = min(w, h)
    assert algo(left, right, check_defense, (n, a, b, w, h)) == 0, "Test 4: Something get wrong :("
    print("Test 4: Ok :)")


if __name__ == "__main__":
    main()

# if You want to launch the test,
# replace "main()" by "tests(left_bin_search)" in the last line
