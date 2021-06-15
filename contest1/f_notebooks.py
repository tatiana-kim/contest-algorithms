# f_notebooks.py
# a1, b1, a2, b2 = 10, 2, 2, 10
# a1, b1, a2, b2 = 5, 7, 3, 2
# area1 = {(a1 + a2) * max(b1, b2): [a1 + a2, max(b1, b2)]}
# area2 = {(a1 + b2) * max(a2, b1): [a1 + b2, max(a2, b1)]}
# area3 = {(b1 + a2) * max(b2, a1): [b1 + a2, max(b2, a1)]}
# area4 = {(b1 + b2) * max(a1, a2): [b1 + b2, max(a1, a2)]}

a1, b1, a2, b2 = map(int, input().split())

area_vars = {(a1 + a2) * max(b1, b2): [a1 + a2, max(b1, b2)],
             (a1 + b2) * max(a2, b1): [a1 + b2, max(a2, b1)],
             (b1 + a2) * max(b2, a1): [b1 + a2, max(b2, a1)],
             (b1 + b2) * max(a1, a2): [b1 + b2, max(a1, a2)]}

min_area_var = min([i for (i, j) in area_vars.items()])
print(*area_vars[min_area_var])
