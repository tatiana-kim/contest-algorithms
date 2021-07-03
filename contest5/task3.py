"""
Дана отсортированная последовательность чисел длиной N и число K
Найти количество пар чисел A, B таких, что B - A > K
"""
n = [1, 3, 7, 8]
k = 3

# O(n**2)
# перебираем все пары чисел и для каждой проверим условие
def countpairswithdiff_greater_than_k(sortednums, k):
    countpairs = 0
    for first in range(len(sortednums)):
        for last in range(first, len(sortednums)):
            if sortednums[last] - sortednums[first] > k:
                countpairs += 1
    return countpairs

# O(n):
""" Возьмем наименьшее число и найдем для него первое подходящее
большее. Все еще большие числа точно подходят. Возьмем в качестве
меньшего числа следующее, а указатель первого подходящего большего
будем двигать начиная с той позиции, где он находится сейчас.
"""
def countpairswithdiff_greater_than_k(sortednums, k):
    countpairs = 0
    last = 0
    for first in range(len(sortednums)-1):
        while last < len(sortednums) and sortednums[last] - sortednums[first] <= k:
            last += 1
        countpairs += len(sortednums) - last
    return countpairs


        while (i < n && j < m) {
            if (Math.abs(a[i] - b[j]) < min) {
                min = Math.abs(a[i] - b[j]);
                mini = a[i];
                minj = b[j];
            }

            if (a[i] > b[j]) {
                j++;
            } else {
                i++;
            }
        }
