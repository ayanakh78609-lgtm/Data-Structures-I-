class Node:
    def __init__(self, key): self.key, self.left, self.right = key, None, None
def insert(root, key):
    if root is None: return Node(key)
    if key < root.key: root.left = insert(root.left, key)
    elif key > root.key: root.right = insert(root.right, key)
    return root
def inorder(root): return inorder(root.left) + [root.key] + inorder(root.right) if root else []
def delete(root, key):
    if root is None: return None
    if key < root.key: root.left = delete(root.left, key)
    elif key > root.key: root.right = delete(root.right, key)
    else:
        if root.left is None: return root.right
        if root.right is None: return root.left
        successor = root.right
        while successor.left: successor = successor.left
        root.key = successor.key; root.right = delete(root.right, successor.key)
    return root
root = None
for x in [50, 30, 70, 20, 40, 60, 80]: root = insert(root, x)
print("BST before deletion:", inorder(root)); root = delete(root, 30); print("BST after deleting 30:", inorder(root))
