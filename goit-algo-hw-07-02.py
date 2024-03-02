class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_min_value(root):
    if root is None:
        return None

    # Йдемо у лівого сина, поки він існує
    while root.left is not None:
        root = root.left

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

# Знаходимо найменше значення в дереві
min_value = find_min_value(root)
print("Найменше значення у дереві:", min_value)
