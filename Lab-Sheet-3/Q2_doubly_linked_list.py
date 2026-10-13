class Node:
    def __init__(self, data):
        self.data, self.prev, self.next = data, None, None

class DoublyLinkedList:
    def __init__(self): self.head = None
    def insert_head(self, data):
        node = Node(data); node.next = self.head
        if self.head: self.head.prev = node
        self.head = node
    def insert_tail(self, data):
        node = Node(data)
        if not self.head: self.head = node; return
        cur = self.head
        while cur.next: cur = cur.next
        cur.next = node; node.prev = cur
    def delete_value(self, value):
        cur = self.head
        while cur and cur.data != value: cur = cur.next
        if not cur: print("Value not found"); return
        if cur.prev: cur.prev.next = cur.next
        else: self.head = cur.next
        if cur.next: cur.next.prev = cur.prev
    def forward(self):
        cur, out = self.head, []
        while cur: out.append(str(cur.data)); cur = cur.next
        print(" <-> ".join(out) if out else "Empty")
    def backward(self):
        cur = self.head
        if not cur: print("Empty"); return
        while cur.next: cur = cur.next
        out = []
        while cur: out.append(str(cur.data)); cur = cur.prev
        print(" <-> ".join(out))

dll = DoublyLinkedList()
for value in [10, 20, 30]: dll.insert_tail(value)
dll.insert_head(5); dll.insert_tail(40)
print("Forward traversal:"); dll.forward()
print("Backward traversal:"); dll.backward()
dll.delete_value(20); print("After deleting 20:"); dll.forward()
