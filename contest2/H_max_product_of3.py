def find_maxproduct_of3(a):
    if len(a) <= 2:
        return "No"

    if len(a) == 3:
        return a

    if len(a) == 4:
        a.sort()
        if a[0] * a[1] * a[3] > a[1] * a[2] * a[3]:
            return a[0], a[1], a[3]
        return a[1], a[2], a[3]


    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for i in range(len(a)):
        if max1 <= a[i]:
            max3 = max2
            max2 = max1
            max1 = a[i]
        elif max2 <= a[i]:
            max3 = max2
            max2 = a[i]
        elif max3 <= a[i]:
            max3 = a[i]
        if min1 >= a[i]:
            min2 = min1
            min1 = a[i]
        elif min2 >= a[i]:
            min2 = a[i]

    if (min1 * min2 * max1) > (max1 * max2 * max3):
        return min1, min2, max1
    return max1, max2, max3


def main():
    seq = list(map(int, input().split()))
    
    print(*find_maxproduct_of3(seq))


if __name__ == "__main__":
    main()
