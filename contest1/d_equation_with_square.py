# sqrt(a * x + b) = c
a, b, c = [int(input) for i in range(3)]
# input sample: a, b, c = 1, 2, 3

if a == 0:
	print("There's two cases")
elif b == c*c:
	print("MANY SOLUTIONS")
elif b == c*c:
    print("NO SOLUTION")
else:
	x = (c*c - b) / a
	print(x)
