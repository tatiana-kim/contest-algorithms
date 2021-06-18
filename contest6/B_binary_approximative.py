"""
Приближенный двоичный поиск
Для каждого из чисел второй последовательности найдите ближайшее к нему в первой.

Формат ввода
В первой строке входных данных содержатся числа N и K ().
Во второй строке задаются N чисел первого массива, отсортированного по неубыванию, 
а в третьей строке – K чисел второго массива. 
Каждое число в обоих массивах по модулю не превосходит 2⋅109.

Формат вывода
Для каждого из K чисел выведите в отдельную строку число из первого массива,
наиболее близкое к данному. Если таких несколько, выведите меньшее из них.
"""

# O(logN)
def find_left_bound(arr, key):
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
def find_right_bound(arr, key):
    left = -1
    right = len(arr) - 1
    while right - left > 1:
        middle = (left + right) // 2
        if arr[middle] >= key:
            right = middle
        else:
            left = middle
    return arr[right]


def main():
    n, k = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    for i in arr2:
        left_bound = find_left_bound(arr1, i)
        right_bound = find_right_bound(arr1, i)
        distance_from_left_bound = i - left_bound
        distance_from_right_bound = right_bound - i
        print(left_bound if distance_from_left_bound <= distance_from_right_bound else right_bound)


def test(algoleft, algoright):
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4, 8, 1, 6]
    answer = []
    for i in arr2:
        left_bound = find_left_bound(arr1, i)
        right_bound = find_right_bound(arr1, i)
        distance_from_left_bound = i - left_bound
        distance_from_right_bound = right_bound - i
        a = left_bound if distance_from_left_bound <= distance_from_right_bound else right_bound
        answer.append(a)
    assert answer == [1, 3, 7, 1, 5], "Test1: Wrooong :("
    print("Test1 : Ok")


    arr1 = [1, 1, 4, 4, 8, 120]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 63, 64, 65]
    answer = []
    for i in arr2:
        left_bound = find_left_bound(arr1, i)
        right_bound = find_right_bound(arr1, i)
        distance_from_left_bound = i - left_bound
        distance_from_right_bound = right_bound - i
        a = left_bound if distance_from_left_bound <= distance_from_right_bound else right_bound
        answer.append(a)
    assert answer == [1, 1, 4, 4, 4, 4, 8, 8, 8, 8, 120], "Test2: Wrooong :("
    print("Test2 : Ok")


    arr1 = [-5, 1, 1, 3, 5, 5, 8, 12, 13, 16]
    arr2 = [0, 3, 7, -17, 23, 11, 0, 11, 15, 7]
    answer = []
    for i in arr2:
        left_bound = find_left_bound(arr1, i)
        right_bound = find_right_bound(arr1, i)
        distance_from_left_bound = i - left_bound
        distance_from_right_bound = right_bound - i
        a = left_bound if distance_from_left_bound <= distance_from_right_bound else right_bound
        answer.append(a)
    assert answer == [1, 3, 8, -5, 16, 12, 1, 12, 16, 8], "Test3: Wrooong :("
    print("Test3 : Ok")


if __name__ == "__main__":
    main()
    
# in the last line, replace main() by test(find_left_bound, find_right_bound) in order to start tests
