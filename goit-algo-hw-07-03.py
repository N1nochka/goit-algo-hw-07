class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_sum(root):
    if root is None:
        return 0

    # Рекурсивно обчислюємо суму лівого та правого піддерева,
    # додаємо поточне значення та повертаємо суму
    return root.val + find_sum(root.left) + find_sum(root.right)

# Приклад використання:
# Створюємо AVL-дерево
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# Знаходимо суму всіх значень в дереві
tree_sum = find_sum(root)
print("Сума всіх значень в дереві:", tree_sum)
