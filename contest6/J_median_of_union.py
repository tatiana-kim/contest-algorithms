from math import ceil

# O(logN)
def left_bin_search(arr, key):
    left = 0
    right = len(arr)
    while right - left > 1:
        middle = (left + right) // 2
        if arr[middle] <= key:
            left = middle
        else:
            right = middle
    return arr[left]


# O(logN)
def right_bin_search(arr, key):
    left = -1
    right = len(arr) - 1
    while right - left > 1:
        middle = (left + right) // 2
        if arr[middle] >= key:
            right = middle
        else:
            left = middle
    return arr[right]


def permutate(arr, n, l):  # find_median_of_union
    # l -= 1
    for i in range(n):
        for j in range(i+1, n):
            median = ceil((arr[i][-1] + arr[j][0]) / 2)
            #print(median)

            left_bound_med_arr1 = left_bin_search(arr[i], median)
            right_bound_med_arr1 = right_bin_search(arr[i], median)
            #print("left_bound_med_arr1:", left_bound_med_arr1, "right_bound_med_arr1:", right_bound_med_arr1)
            # arr1: left_bound_med_from_med
            dist_from_left_bound_arr1 = median - left_bound_med_arr1
            dist_from_right_bound_arr1 = right_bound_med_arr1 - median
            median_arr1 = left_bound_med_arr1 if dist_from_left_bound_arr1 <= dist_from_right_bound_arr1 else right_bound_med_arr1
            #print("median_arr1:", median_arr1)

            left_bound_med_arr2 = left_bin_search(arr[j], median)
            right_bound_med_arr2 = right_bin_search(arr[j], median)
            #print("left_bound_med_arr2:", left_bound_med_arr2, "right_bound_med_arr2:", right_bound_med_arr2)
            dist_from_left_bound_arr2 = median - left_bound_med_arr2
            dist_from_right_bound_arr2 = right_bound_med_arr2 - median
            median_arr2 = left_bound_med_arr2 if dist_from_left_bound_arr2 <= dist_from_right_bound_arr2 else right_bound_med_arr2
            #print("median_arr2:", median_arr2)
            
            dist_med_arr1 = abs(median - median_arr1)
            dist_med_arr2 = abs(median - median_arr2)
            print(median_arr1 if dist_med_arr1 <= dist_med_arr2 else median_arr2)


def main():
    # n, l = list(map(int, input().split()))
    # a = []
    # for i in range(n):
    #     a.append(list(map(int, input().split())))

    n, l = 3, 6
    a = [[1, 4, 7, 10, 13, 16], [0, 2, 5, 9, 14, 20], [1, 7, 16, 16, 21, 22]]

    # n, l = 4, 20
    # a = [[-1128, -869, -492, -103, 119, 250, 291, 592, 980, 1249, 1553, 1800, 1947, 2030, 2342, 2610, 2961, 2984, 3337, 3663],
    #      [-1492, -1414, -1408 -1238, -1103, -996, -856, -745, -491, -455, -261, 4, 215, 272, 372, 451, 624, 706, 826, 921],
    #      [67, 105, 115, 142, 216, 250, 293, 342, 395, 415, 520, 539, 572, 650, 651, 672, 742, 809, 874, 902],
    #      [-1434, -1357, -1217, -1163, -983, -975, -715, -528, -379, -376, -178, -1, 24, 278, 499, 636, 707, 881, 923, 1171]
    #     ]


    n. l = 2, 20
    a = [[-1062 -896 -536 -138 103 250 484 520 922 1168 1219 1333 1628 1638 1803 1855 1868 2139 2528 2860],
         [-1393 -1327 -1206 -995 -983 -977 -821 -606 -401 -239 -174 -28 144 252 495 586 668 682 931 1165]
        ]


    permutate(a, n, l)

main()
