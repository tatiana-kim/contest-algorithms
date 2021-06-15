n_keys = int(input())
capacity = [0] + list(map(int, input().split()))
n_pressings = int(input())
pressings = list(map(int, input().split()))

for i in range(n_pressings):
    capacity[pressings[i]] -= 1

for i in range(1, n_keys + 1):
    if capacity[i] < 0:
        print("YES")
    else:
        print("NO")

# n_keys = 5
# capacity = [1, 50, 3, 4, 3]
# capacity[:] = [0] + capacity
# n_pressings = 16
# pressings = [1, 2, 3, 4, 5, 1, 3, 3, 4, 5, 5, 5, 5, 5, 4, 5]
