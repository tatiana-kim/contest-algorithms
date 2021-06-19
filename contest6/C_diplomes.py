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


w, h, n = list(map(int, input().split()))
left = 0  # or left = w
right = max(w * n, h * n)
print(left_bin_search(left, right, checkboard, (w, h, n)))
