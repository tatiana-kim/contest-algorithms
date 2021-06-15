# A_dict_of_synonims.py
n = int(input())
dict_syn = {}
for i in range(n):
    word, syn = input().split()
    dict_syn[word] = syn
    dict_syn[syn] = word

find_syn_for = input()
print(dict_syn[find_syn_for])

"""
> Input:
2
Ololo Ololo
Numbers 1234567890
Numbers
> Output:
1234567890
"""

"""
3
Hello Hi
Bye Goodbye
List Array
Goodbye

> Bye
"""