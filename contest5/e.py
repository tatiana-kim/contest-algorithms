# O(n^2)
def count_dists(d, k):
    count = 0
    for left in range(len(d)):
        for right in range(left, len(d)):
            if d[right] - d[left] > k:
                count += 1
    return count

# O(n)
def count_dists(d, k):
    count = right = 0
    for left in range(len(d)):
        while right < len(d) and d[right] - d[left] <= k:
            right += 1
        count += len(d) - right
    return count

assert count_dists([1, 3, 5, 8], 4) == 2, "WA :("


def main():
   n, r = map(int, input().split())
   d = list(map(int, input().split()))
   print(count_dists(d, r))  # 2


if __name__ == "__main__":
    main()
