"""
Дан список чисел. Определите, сколько в этом списке элементов, которые
больше двух своих соседей и выведите количество таких элементов.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.
"""
def greater_than_neighb(seq):
    n = len(seq)
    count = 0
    for i in range(1, n-1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
        # if seq[i-1] < seq[i] > seq[i+1]:
            count += 1
    return count


def tests(algo):
    assert algo([1, 2, 3, 4, 5]) == 0, "WA :("
    assert algo([5, 4, 3, 2, 1]) == 0, "WA :("
    assert algo([1, 5, 1, 5, 1]) == 2, "WA :("


def main():
    seq1 = list(map(int, input().split()))
    print(greater_than_neighb(seq1))


if __name__ == "__main__":
    main()

# to start tests replace main() call by 
# tests(greater_than_neighb) in the last line of code
