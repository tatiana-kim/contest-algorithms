"""
Напишите программу, которая находит в массиве элемент, самый близкий по величине к  данному числу.

Формат ввода
В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива. 
Во второй строке содержатся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000). 
В третьей строке вводится одно целое число x, не превосходящее по модулю 1000.

Формат вывода
Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько, выведите любое из них.
"""

def mostfrequent(n, seq, x):
    diff = abs(seq[0] - x)
    answer = seq[0]
    for i in range(1, n):
        if abs(seq[i] - x) < diff:
            diff = abs(seq[i] - x)
            answer = seq[i]
    return answer


def main():
    n = int(input())
    seq = list(map(int, input().split()))
    x = int(input())
    # input from file
    # f = open("input.txt", "r")
    # n = int(next(f))
    # seq = [int(i) for i in next(f).strip().split()]
    # x = int(next(f))
    print(mostfrequent(n, seq, x))


def tests(algo):
	n, x = 5, 6
	seq = [1, 2, 3, 4, 5]
	assert algo(n, seq, x) == 5, "WA :("
	print("Test 1: Ok")

	n, x = 5, 3
	seq = [5, 4, 3, 2, 1]
	assert algo(n, seq, x) == 3, "WA :("
	print("Test 2: Ok")

	n, x = 6, 2
	seq = [1, 3, 1, 3, 1, 3] == 1, "WA :("
	print("Test 3: Ok")

if __name__ == "__main__":
    # main()
    tests(mostfrequent)
