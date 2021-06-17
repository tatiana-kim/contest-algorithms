def binary(arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == k:
            return "YES"
        elif arr[middle] > k:
            right = middle - 1
        else:  # arr[middle] < k
            left = middle + 1
    return "NO"


def main():
    n, k = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    answer = "\n".join([binary(arr1, i) for i in arr2])
    print(answer)


def test(algo):
    n, k = 10, 10
    arr1 = [1, 61, 126, 217, 2876, 6127, 39162, 98126, 712687, 1000000000]
    arr2 = [100, 6127, 1, 61, 200, -10000, 1, 217, 10000, 1000000000]
    assert [algo(arr1, i) for i in arr2] == ["NO", "YES", "YES", "YES", "NO", "NO", "YES", "YES", "NO", "YES"],\
        "Test1: Something get wrong :("
    print("Test1: Ok")

    n, k = 10, 10
    arr1 = [-8, -6, -4, -4, -2, -1, 0, 2, 3, 3]
    arr2 = [8, 3, -3, -2, 2, -1, 2, 9, -8, 0]
    assert [algo(arr1, i) for i in arr2] == ["NO", "YES", "NO", "YES", "YES", "YES", "YES", "NO", "YES", "YES"],\
        "Test2: Something get wrong :("
    print("Test2: Ok")

    n, k = 10, 5
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [-2, 0, 4, 9, 12]
    assert [algo(arr1, i) for i in arr2] == ["NO", "NO", "YES", "YES", "NO"],\
        "Test2: Something get wrong :("
    print("Test3: Ok")


if __name__ == "__main__":
    main()

# in the last line, replace main() by test(binary) in order to start tests
