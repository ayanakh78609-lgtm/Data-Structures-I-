class Node:
    def __init__(self, key): self.key, self.left, self.right, self.height = key, None, None, 1
def height(n): return n.height if n else 0
def update(n): n.height = 1 + max(height(n.left), height(n.right))
def balance(n): return height(n.left) - height(n.right) if n else 0
def rotate_right(y):
    x, t2 = y.left, y.left.right; x.right, y.left = y, t2; update(y); update(x); return x
def rotate_left(x):
    y, t2 = x.right, x.right.left; y.left, x.right = x, t2; update(x); update(y); return y
def insert(root, key):
    if not root: return Node(key)
    if key < root.key: root.left = insert(root.left, key)
    elif key > root.key: root.right = insert(root.right, key)
    else: return root
    update(root); b = balance(root)
    if b > 1 and key < root.left.key: return rotate_right(root)       # LL
    if b < -1 and key > root.right.key: return rotate_left(root)      # RR
    if b > 1 and key > root.left.key: root.left = rotate_left(root.left); return rotate_right(root) # LR
    if b < -1 and key < root.right.key: root.right = rotate_right(root.right); return rotate_left(root) # RL
    return root
def inorder(root): return inorder(root.left) + [root.key] + inorder(root.right) if root else []
root = None
for value in [30, 20, 40, 10, 25, 28, 50]: root = insert(root, value)
print("AVL inorder:", inorder(root)); print("Root balance factor:", balance(root))
