def only_letters(nums):
    num, nums2 = [], []
    for i in nums:
        for j in i:
            if j.isnumeric():
                num.append(j)
        nums2.append("".join(num))
        num = []

    return nums2


def main(num):
	number = only_letters(num)
	if len(number) > 7:
		return with_code(number)
	else:
		return without_code(number)


def with_code(numbers):
	for i in numbers:
		if "495" in i:



# nums = [input() for i in range(3)]
# nums = ["8(495)430-23-97", "+7-4-9-5-43-023-97", "4-3-0-2-3-9-7"]
n = "8(495)430-23-97"
nums = ["+7-4-9-5-43-023-97", "4-3-0-2-3-9-7", "8-495-430"]
print(only_letters(nums))
