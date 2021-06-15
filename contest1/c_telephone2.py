# new = input()
# nums = [input() for i in range(3)]

new = "835-5-18-5"
nums = ["8-3-55-1-85", "7-355185", "835-518-5"]

new2 = []
for i in new:
    if i.isnumeric():
        new2.append(i)

new2 = "".join(new2)

num, nums2 = [], []
for i in nums:
    for j in i:
        if j.isnumeric():
            num.append(j)
    nums2.append("".join(num))
    num = []

for i in nums2:
    if len(i) > 7 and len(new2) > 7:
        if i[1:] == new2[1:]:
            print("YES")
        else:
            print("NO")
    elif len(i) == 7 and len(new2) > 7:
        if new2[1:4] == "495" and new2[4:] == i:
            print("YES")
        else:
            print("NO")
    elif len(i) > 7 and len(new2) == 7:
        if i[1:4] == "495" and i[4:] == new2:
            print("YES")
        else:
            print("NO")
    else:  # len(i) == 7 and len(n) == 7:
        if i == new2:
            print("YES")
        else:
            print("NO")


# ----------------------------------------
# new = "8(495)430-23-97"
# nums = ["+7-4-9-5-43-023-97", "4-3-0-2-3-9-7", "8-495-430"]

# new = "86406361642"
# nums = ["83341994118", "86406361642", "83341994118"]

# new = "+78047952807"
# nums = ["+78047952807", "+76147514928", "88047952807"]
