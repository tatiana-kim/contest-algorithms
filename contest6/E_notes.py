from decimal import Decimal, getcontext

getcontext().prec = 20


def left_bin_search(left, right, check, checkparams):
    i = 0
    while left < right:
        middle = (left + right) // 2
        if check(middle, checkparams):
            right = middle
        else: 
            left = middle + 1
        i += 1
    return left


# x = how many time you have to obtain "5"
def check_note(x, params):
    a, b, c = params
    note = Decimal(2*a + 3*b + 4*c + 5.0*x) / Decimal(a + b + c + x)
    # note = ceil(note) if note * 10 % 10 >= 5 else round(note)  # ; return note >= 4
    return note >= 3.5


def main():
    a, b, c = [int(input()) for i in range(3)]
    left = 0
    right = (a + b + c) + 1
    print(left_bin_search(left, right, check_note, (a, b, c)))


# for output in file
def main_file():
    a, b, c = [float(input()) for i in range(3)]
    left = 0
    right = (a + b + c) + 1
    answer = left_bin_search(left, right, check_note, (a, b, c))
    f = open("output.txt", "w")
    f.write(str(int(answer)))
    f.close()


def tests(algo):
    a, b, c = 2, 0, 0
    right = (a + b + c) + 1
    assert algo(0, right, check_note, (a, b, c)) == 2, "WA :("
    print("Test 1: Ok")

    a, b, c = 1000000000000000, 1000000000000000, 1000000000000000
    right = (a + b + c) + 1
    assert algo(0, right, check_note, (a, b, c)) == 1000000000000000, "WA :("
    print("Test 2: Ok")

    a, b, c = 1000000000000000, 1000000000000000, 0
    right = (a + b + c) + 1
    assert algo(0, right, check_note, (a, b, c)) == 1333333333333334, "WA :("
    print("Test 3: Ok")


if __name__ == "__main__":
    main()


# if You want to launch the test,
# replace "main()" by "tests(left_bin_search)" in the last line

# right = (a + b + c)  # half of all any notes must be "5" (for worst case)
# in other word the number of "5" must be at least the number of all received notes
