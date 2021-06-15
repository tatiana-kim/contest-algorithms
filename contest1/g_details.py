# using recursion

# g_details.py
# n: kg of alloy we have in total in the begining
# k: kg for one piece of blank
# m: kg for one piece of product

def main(n, k, m, products, rest):
    if n < k or k < m:
        return products

    blanks = n // k
    n %= k  # n = n - blanks

    for i in range(blanks):
        products += k // m
        rest.append(k % m)

    n += sum(rest)
    rest = []
    return main(n, k, m, products, rest)


def tests(algo):
    assert algo(10, 5, 2, 0, []) == 4
    assert algo(13, 5, 3, 0, []) == 3
    assert algo(14, 5, 3, 0, []) == 4


if __name__ == "__main__":
    # tests(main)
    n, k, m = map(int, input().split())
    products = 0
    rest = []
    print(main(n, k, m, products, rest))
