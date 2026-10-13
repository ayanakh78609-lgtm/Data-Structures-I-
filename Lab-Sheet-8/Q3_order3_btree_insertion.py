# B-tree of order 3: at most 3 children (therefore at most 2 keys per node).
class Node:
    def __init__(self, leaf=True): self.keys, self.children, self.leaf = [], [], leaf
class BTreeOrder3:
    def __init__(self): self.root = Node()
    def insert(self, key):
        root = self.root
        if len(root.keys) == 2:
            new = Node(False); new.children.append(root); self._split_child(new, 0); self.root = new
            self._insert_nonfull(new, key)
        else: self._insert_nonfull(root, key)
    def _split_child(self, parent, i):
        child = parent.children[i]
        median = child.keys[1]
        right = Node(child.leaf); right.keys = child.keys[2:]
        child.keys = child.keys[:1]
        if not child.leaf: right.children = child.children[2:]; child.children = child.children[:2]
        parent.keys.insert(i, median); parent.children.insert(i + 1, right)
    def _insert_nonfull(self, node, key):
        if node.leaf:
            node.keys.append(key); node.keys.sort(); return
        i = 0
        while i < len(node.keys) and key > node.keys[i]: i += 1
        if len(node.children[i].keys) == 2:
            self._split_child(node, i)
            if key > node.keys[i]: i += 1
        self._insert_nonfull(node.children[i], key)
    def print_levels(self):
        level, depth = [self.root], 0
        while level:
            print(f"Level {depth}:", [n.keys for n in level])
            level = [child for node in level for child in node.children]; depth += 1
if __name__ == "__main__":
    tree = BTreeOrder3()
    for x in [10, 20, 5, 6, 12, 30, 7, 17]: tree.insert(x)
    tree.print_levels()
