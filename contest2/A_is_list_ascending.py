def is_list_ascending(lst):
    n = len(lst)
    for i in range(1, n):
        if lst[i - 1] >= lst[i]:
            return "NO"
    return "YES"


lst1 = list(map(int, input().split()))
print(is_list_ascending(lst1))
