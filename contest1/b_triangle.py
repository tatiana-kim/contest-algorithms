def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "NO"
    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return "NO"
    return "YES"

x, y, z = int(input()), int(input()), int(input())
print(triangle(x, y, z))
