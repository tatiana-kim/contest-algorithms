# I_sapper.py
# n = number of rows
# m = number of columns
# k = number of mines

def sapper(field, n, m):
    devi = (-1, -1, -1,  0, 0,  1, 1, 1)
    devj = (-1,  0,  1, -1, 1, -1, 0, 1)
    for i in range(n):
        for j in range(m):
            for k in range(len(devi)):
                if field[i][j] != "*":
                    di = i + devi[k]
                    dj = j + devj[k]
                    if (0 <= di < n) and (0 <= dj < m) and (field[di][dj] == "*"):
                        field[i][j] += 1

    return field


def main():
    # input and create initial field with mines
    n, m, k = map(int, input().split())
    field = [[0 for _cows in range(m)] for _rows in range(n)]
    for i in range(k):
        mine_row, mine_col = (int(i) - 1 for i in input().split())
        field[mine_row][mine_col] = "*"

    field = sapper(field, n, m)

    # output:
    for i in range(n):
        for j in range(m):
                print(field[i][j], end=" ")
        print()


def tests(algo):
    n, m = 3, 2
    field = [['*', 0], [0, '*'], [0, 0]]
    assert algo(field, n, m) == [['*', 2], [2, '*'], [1, 1]], "WA :("
    print("Test 1: Passed")


if __name__ == "__main__":
    main()

# to start tests: call tests(sapper) function
