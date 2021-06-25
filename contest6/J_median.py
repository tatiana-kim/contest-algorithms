# idea: https://russianblogs.com/article/1097436754/

def binary(a, b, n):
    lefta = leftb = 0
    righta = rightb = n - 1

    if n == 1:
        return min(a[0], b[0])
    if n == 2:
        s = sorted(a + b)
        return s[1]

    while ((righta - lefta) + 1) > 2:
        # find median of a and median of b
        # if length of list is even:
        length = (righta - lefta) + 1
        if length % 2 == 0:
            ma = (lefta + righta) // 2
            mb = (leftb + rightb) // 2 + 1
        # if odd:
        else:
            ma = (lefta + righta) // 2
            mb = (leftb + rightb) // 2
        #
        if a[ma] > b[mb]:
            righta = ma
            leftb = mb
        else:
            lefta = ma
            rightb = mb

    s = sorted(a[lefta: righta+1] + b[leftb: rightb+1])
    return s[1]


def permutate(arr, n, l):
    for i in range(n):
        for j in range(i+1, n):
            print(binary(arr[i], arr[j], l))


def main():
    n, l = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]
    permutate(arr, n, l)


def tests(algo):
    f = open("J/input.txt", "r")
    n, l = [int(i) for i in next(f).strip().split()]
    lines = f.readlines()
    arr = []
    arr = [[int(i) for i in line.strip().split()] for line in lines]
    f.close()
    
    answer = []
    for i in range(n):
        for j in range(i+1, n):
            answer.append(algo(arr[i], arr[j], l))

    assert answer == [7, 10, 9], "WA :("
    print("Test 1: Ok")


if __name__ == "__main__":
    # main()
    tests(binary)

# replace main() by # tests(binary) call in order to start the tests
