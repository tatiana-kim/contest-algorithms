"""
Последовательность чисел назовем симметричной, если она одинаково читается как слева направо, 
так и справа налево. Например, следующие последовательности являются симметричными: 
1 2 3 4 5 4 3 2 1 1 2 1 2 2 1 2 1 Вашей программе будет дана последовательность чисел. 
Требуется определить, какое минимальное количество и каких чисел надо приписать 
в конец этой последовательности, чтобы она стала симметричной.

Формат ввода
Сначала вводится число N — количество элементов исходной последовательности (1 ≤ N ≤ 100). 
Далее идут N чисел — элементы этой последовательности, натуральные числа от 1 до 9.

Формат вывода
Выведите сначала число M — минимальное количество элементов, которое надо дописать 
к последовательности, а потом M чисел (каждое — от 1 до 9) — числа, которые надо 
дописать к последовательности.

"""
def symmetric_seq(a):
    count = 0
    for i in range(len(a)):
        if a[i:] != a[i:][::-1]:
            count += 1
        else:
            return count, a[:count][::-1]


def main():
    n = int(input())
    seq1 = list(map(int, input().split()))
    a, b = symmetric_seq(seq1)
    print(a)
    if a != 0:
    	print(*b)


if __name__ == "__main__":
    main()


"""
def main_file_input():
    f = open("F/input8.txt", "r")
    next(f)
    seq1 = [int(i) for i in next(f).strip().split()]  # 32 ... 
    f.close()
    a, b = symmetric_seq(seq1)
    print(a)
    if a != 0:
        print(*b)

"""