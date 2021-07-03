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

        if minval == 0:
        	return minshorts, minpents

        if shorts[s] > pents[p]:
            p += 1
        else:
            s += 1
    return minshorts, minpents


def main():
    n = int(input())
    shorts = [int(i) for i in input().split()]  # 3 4
    m = int(input())
    pents = list(map(int, input().split()))  # 1 2 3
    print(*find_min_diff_btwn_shortspents(shorts, pents))


if __name__ == "__main__":
    main()

