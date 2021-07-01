# A_height_of_tree.py
"""
Реализуйте бинарное дерево поиска для целых чисел. 
Программа получает на вход последовательность целых чисел и строит из них дерево. 
Элементы в деревья добавляются в соответствии с результатом поиска их места. 
Если элемент уже существует в дереве, добавлять его не надо. 
Балансировка дерева не производится.

Формат ввода
На вход программа получает последовательность натуральных чисел. 
Последовательность завершается числом 0, которое означает конец ввода, 
и добавлять его в дерево не надо.

Формат вывода
Выведите единственное число – высоту получившегося дерева.
"""

class Node:

    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


    def get_height(self, root):
        if root is None:
            return 0
        else:
            left = self.get_height(root.left)
            right = self.get_height(root.right)
        return max(left, right) + 1


def insert(root, x):
    # if BTS is empty (root doesn't exist yet)
    # then create an object Node with provided value
    if root is None:
        return Node(x)
    else:
        if root.val == x:
            return root
        elif root.val < x:
            root.right = insert(root.right, x)
        else:
            root.left = insert(root.left, x)
    return root


# докучи
def in_order(root):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


def main_stdin():
    number = int(input())
    root = Node(number)
    while number != 0:
        root = insert(root, number)
        number = int(input())
    print(root.get_height(root))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           


def main():
    f = open("A/input4.txt", "r")
    numbers = f.readline().strip().split()
    root = Node(int(numbers[0]))
    n = len(numbers)
    for i in range(1, n-1):
        root = insert(root, int(numbers[i]))
    print(root.get_height(root))


def test(algo):
    numbers = [7, 3, 2, 1, 9, 5, 4, 6, 8]
    root = Node(numbers[0])
    for i in range(1, len(numbers) - 1):
        root = insert(root, numbers[i])
    assert root.algo(root) == 2, "WA :("
    print("Test1: Ok")


if __name__ == "__main__":
    # main()
    test(Node.get_height)

# 2 1 3 0  # answer: 2

"""
arr = [7, 3, 2, 1, 9, 5, 4, 6, 8]
7 3 2 1 9 5 4 6 8 0  # answer: 4
"""
