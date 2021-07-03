# n = number of cars
# k = lucky number
def test(nums, k):
    countpairs = 0
    last = 0
    for first in range(len(nums)-1):
        while last < len(nums) and nums[last] + nums[first] == k:
            last += 1
        countpairs += len(nums) - last
    return countpairs


def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))


if __name__ == "__main__":
    main()
