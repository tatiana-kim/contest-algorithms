def right_bin_search(left, right, check, checkparams):
    while left < right:
        middle = (left + right + 1) // 2
        if check(middle, checkparams):
            left = middle
        else:
            right = middle - 1
    return left


# how many wires with given length from 1 to 10**7 cm
def checklength(x, params):
    arr, k = params
    summ = 0
    for wire in arr:
        summ += wire // x
    return summ >= k


def main():
    n, k = map(int, input().split())
    arr = [int(input()) for i in range(n)]
    l = 0
    r = 10 ** 7  # (макс допустимое значение длины провода)
    print(right_bin_search(l, r, checklength, (arr, k)))

main()
