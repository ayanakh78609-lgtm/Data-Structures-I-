class Node:
    def __init__(self, data): self.data, self.left, self.right = data, None, None

def inorder(root): return inorder(root.left) + [root.data] + inorder(root.right) if root else []
def preorder(root): return [root.data] + preorder(root.left) + preorder(root.right) if root else []
def postorder(root): return postorder(root.left) + postorder(root.right) + [root.data] if root else []
def inorder_iterative(root):
    result, stack, cur = [], [], root
    while cur or stack:
        while cur: stack.append(cur); cur = cur.left
        cur = stack.pop(); result.append(cur.data); cur = cur.right
    return result
def preorder_iterative(root):
    if not root: return []
    result, stack = [], [root]
    while stack:
        cur = stack.pop(); result.append(cur.data)
        if cur.right: stack.append(cur.right)
        if cur.left: stack.append(cur.left)
    return result
def postorder_iterative(root):
    if not root: return []
    result, stack = [], [root]
    while stack:
        cur = stack.pop(); result.append(cur.data)
        if cur.left: stack.append(cur.left)
        if cur.right: stack.append(cur.right)
    return result[::-1]

# Sample tree:       1
#                   / \
#                  2   3
#                 / \
#                4   5
root = Node(1); root.left, root.right = Node(2), Node(3)
root.left.left, root.left.right = Node(4), Node(5)
for name, fn in [("Inorder", inorder), ("Preorder", preorder), ("Postorder", postorder), ("Iterative inorder", inorder_iterative), ("Iterative preorder", preorder_iterative), ("Iterative postorder", postorder_iterative)]:
    print(f"{name}: {fn(root)}")
