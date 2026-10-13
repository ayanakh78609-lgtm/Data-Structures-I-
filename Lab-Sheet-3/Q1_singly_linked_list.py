class Node:
    def __init__(self, data):
        self.data, self.next = data, None

class SinglyLinkedList:
    def __init__(self): self.head = None
    def insert_head(self, data):
        node = Node(data); node.next = self.head; self.head = node
    def insert_tail(self, data):
        node = Node(data)
        if self.head is None: self.head = node; return
        cur = self.head
        while cur.next: cur = cur.next
        cur.next = node
    def insert_at(self, index, data):
        if index < 0: raise IndexError("Invalid index")
        if index == 0: self.insert_head(data); return
        cur = self.head
        for _ in range(index - 1):
            if cur is None: raise IndexError("Index out of range")
            cur = cur.next
        if cur is None: raise IndexError("Index out of range")
        node = Node(data); node.next = cur.next; cur.next = node
    def delete_value(self, target):
        cur, prev = self.head, None
        while cur and cur.data != target: prev, cur = cur, cur.next
        if cur is None: print("Value not found"); return
        if prev is None: self.head = cur.next
        else: prev.next = cur.next
        print("Deleted", target)
    def search(self, target):
        cur, index = self.head, 0
        while cur:
            if cur.data == target: return index
            cur, index = cur.next, index + 1
        return -1
    def display(self):
        cur, values = self.head, []
        while cur: values.append(str(cur.data)); cur = cur.next
        print(" -> ".join(values + ["None"]))

ll = SinglyLinkedList()
for value in [10, 20, 30]: ll.insert_tail(value)
print("Initial list:"); ll.display()
ll.insert_head(5); ll.insert_tail(40); ll.insert_at(2, 15)
print("After insertion at head, tail and index 2:"); ll.display()
ll.delete_value(20); print("After deleting 20:"); ll.display()
print("Index of 30:", ll.search(30))
