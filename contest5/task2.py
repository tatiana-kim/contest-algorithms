"""Дана последовательность чисел длиной N
Найти количество отрезков с нулевой суммой
"""

# O(n):
""" Насчитаем префиксные суммы. Одинаковые префиксные
суммы означают, что сумма на отрезке с началом и концом
в позициях, на которых достигаются одинаковые префиксные
суммы, будет равно нулю
"""

def countprefixsum(nums):
    prefixsumbyvalue = {0: 1}
    nowsum = 0
    for now in nums:
        nowsum += now
        if nowsum not in prefixsumbyvalue:
            prefixsumbyvalue[nowsum] = 1
        prefixsumbyvalue[nowsum] += 1
    return prefixsumbyvalue

def countzerosumranges(prefixsumbyvalue):
    countranges = 0
    for nowsum in prefixsumbyvalue:
        countsum = prefixsumbyvalue[nowsum]
        countranges += countsum * (countsum - 1) // 2
    return countranges
