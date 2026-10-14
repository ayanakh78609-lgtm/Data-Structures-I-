# ==================================================
# Name: Ayan
# College ID: CU25250038
# University: COER University, Roorkee
# Course: B.Tech Computer Science and Engineering
# Subject: Data Structures-I
# Experiment: Binary Tree Traversals(MTE Practicle)
# ==================================================
# Lab Sheet 6: Binary Tree Traversals

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Recursive Inorder Traversal
def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.data, end=" ")
        inorder_recursive(root.right)


# Recursive Preorder Traversal
def preorder_recursive(root):
    if root:
        print(root.data, end=" ")
        preorder_recursive(root.left)
        preorder_recursive(root.right)


# Recursive Postorder Traversal
def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.data, end=" ")


# Iterative Inorder Traversal
def inorder_iterative(root):
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")
        current = current.right


# Iterative Preorder Traversal
def preorder_iterative(root):
    if not root:
        return

    stack = [root]

    while stack:
        current = stack.pop()
        print(current.data, end=" ")

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)


# Iterative Postorder Traversal
def postorder_iterative(root):
    if not root:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        current = stack1.pop()
        stack2.append(current)

        if current.left:
            stack1.append(current.left)

        if current.right:
            stack1.append(current.right)

    while stack2:
        print(stack2.pop().data, end=" ")


# Construct the binary tree
#
#           1
#          / \
#         2   3
#        / \
#       4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# Display traversal results
print("Recursive Inorder Traversal:")
inorder_recursive(root)

print("\nRecursive Preorder Traversal:")
preorder_recursive(root)

print("\nRecursive Postorder Traversal:")
postorder_recursive(root)

print("\n\nIterative Inorder Traversal:")
inorder_iterative(root)

print("\nIterative Preorder Traversal:")
preorder_iterative(root)

print("\nIterative Postorder Traversal:")
postorder_iterative(root)

print()