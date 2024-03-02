class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_max_value(root):
    if root is None:
        return None

    while root.right is not None:
        root = root.right

    return root.val

# Приклад використання:
# Створюємо AVL-дерево
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# Знаходимо найбільше значення в дереві
max_value = find_max_value(root)
print("Найбільше значення у дереві:", max_value)
