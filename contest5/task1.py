"""
Task. Дана последовательность чисел длиной N и M зпросов.
Solution. Для каждого префикса посчитаем количество нулей на нем
(prefixzeroes). Тогда ответ на запрос на полуинтервале [L, R):
prefixzeroes[R] - prefixzeroes[L]
"""

def makeprefixzeroes(nums):
    prefixzeroes = [0] + (len(nums) + 1)
    for i in range(1, len(nums) - 1):
        if nums[i - 1] == 0:
            prefixzeroes[i] = prefixzeroes[i - 1] + 1
        else:
            prefixzeroes[i] = prefixzeroes[i - 1]
    return prefixzeroes

def countzeroes(prefixzeroes, l, r):
    return prefixzeroes[r] - prefixzeroes[l]
