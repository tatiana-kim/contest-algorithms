"""
G. Наибольшее произведение двух чисел
Ограничение времени: 1 секунда
Ограничение памяти: 64Mb
Ввод: стандартный ввод или input.txt
Вывод: стандартный вывод или output.txt
Дан список, заполненный произвольными целыми числами. 
Найдите в этом списке два числа, произведение которых максимально. 
Выведите эти числа в порядке неубывания.

Список содержит не менее двух элементов. 
Числа подобраны так, что ответ однозначен.

Решение должно иметь сложность O(n), где n - размер списка.
"""

def find_product_of2max(a):
    max1 = max2 = min1 = min2 = 0
    if len(a) == 2:
        return sorted(a)

    if len(a) == 3:
        a.sort()
        if a[1] * a[2] > a[0] * a[1]:
            return a[1], a[2]
        elif a[0] * a[2] > a[0] * a[1]:
            return a[0], a[2]
        elif a[0] * a[2] > a[1] * a[2]:
            return a[0], a[2]

    for i in range(len(a)):
        if a[i] > max1:
            max2 = max1
            max1 = a[i]
        elif a[i] > max2:
            max2 = a[i]
        elif a[i] < min1:
            min2 = min1
            min1 = a[i]
        elif a[i] < min2:
            min2 = a[i]
    if max1 * max2 > min1 * min2:
        return sorted([max1, max2])
    return sorted([min1, min2])
    # return (max1, max2) if max1 * max2 > min1 * min2 else (min1, min2)


def main():
    seq = list(map(int, input().split()))
    print(*find_product_of2max(seq))


def tests(algo):
    assert algo([4, 3, 5, 2, 5]) == [5, 5], "WA :("
    assert algo([-4, 3, -5, 2, 5]) == [-5, -4], "WA :("
    assert algo([1, 0]) == [0, 1], "WA :("
    assert algo([-6, -5, 20]) == [-6, -5], "WA :("
    f = open("G/input3.txt", "r")
    seq = [int(i) for i in next(f).strip().split()]
    f.close()
    assert algo(seq) == [29710, 29793], "WA :("


if __name__ == "__main__":
    tests(find_product_of2max)

# to launch the tests replace main() call by
# tests(find_product_of2max) call
