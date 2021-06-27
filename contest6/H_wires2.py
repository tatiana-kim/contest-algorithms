def right_bin_search(left, right, arr, n, k):
    while left < right:
        summ = 0
        middle = (left + right + 1) // 2
        for wire in arr:
            summ += wire // middle
        if summ >= k:
            left = middle
        else:
            right = middle - 1
    return left


def main():
    n, k = map(int, input().split())
    a = [int(input()) for i in range(n)]
    l = 1
    r = 10 ** 7  # (макс допустимое значение длины провода)
    print(right_bin_search(l, r, a, n, k))


main()
