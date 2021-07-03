# n = t-shorts
# m = pents

def find_min_diff_btwn_shortspents(shorts, pents):
    s = p = 0  # s = shorts; p = pents
    n, m = len(shorts), len(pents)
    minshorts = minpents = 0
    minval = 10 ** 7 + 1
    while s < n and p < m:
        if abs(shorts[s] - pents[p]) < minval:
            minval = abs(shorts[s] - pents[p])
            minshorts = shorts[s]
            minpents = pents[p]

        # if minval == 0:
        #     return minshorts, minpents

        if shorts[s] > pents[p]:
            p += 1
        else:
            s += 1
    return minshorts, minpents


def tests(algo):
	shorts = [3, 4]
	pents = [1, 2, 3]
	assert algo(shorts, pents) == (3, 3), "WA :("

	shorts = [4, 5]
	pents = [1, 2, 3]
	assert algo(shorts, pents) == (4, 3), "WA :("

	shorts = [1, 2, 3, 4, 5]
	pents = [1, 2, 3, 4, 5]
	assert algo(shorts, pents) == (1, 1), "WA :("

	shorts = [1, 2, 3, 4, 100000]
	pents = [100, 101, 102, 103, 104, 105, 106, 107, 108, 99949]
	assert algo(shorts, pents) == (100000, 99949), "WA :("


def main():
    n = int(input())
    shorts = [int(i) for i in input().split()]  # 3 4
    m = int(input())
    pents = list(map(int, input().split()))  # 1 2 3
    print(*find_min_diff_btwn_shortspents(shorts, pents))


if __name__ == "__main__":
    main()

"""
About commented lines:
if minval == 0:
    return minshorts, minpents
 Эта проверка в худшем случае замедлит ход программы,
 так как на каждом шаге цикла будет выполнятся проверка.
 Но в среднем это может дать выгоду и единственный способ
 узнать будет ли это полезно или нет - запустить на данных,
 похожих на реальные. в учебных задачах худший случай обязательно
 будет
 """

# to launch tests: tests(find_min_diff_btwn_shortspents)
