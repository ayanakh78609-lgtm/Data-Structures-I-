class Node:
    def __init__(self, data): self.data, self.next = data, None
class LinkedQueue:
    def __init__(self): self.front = self.rear = None
    def enqueue(self, value):
        node = Node(value)
        if self.rear is None: self.front = self.rear = node
        else: self.rear.next = node; self.rear = node
        print(value, "enqueued")
    def dequeue(self):
        if self.front is None: print("Queue is empty"); return
        value = self.front.data; self.front = self.front.next
        if self.front is None: self.rear = None
        print("Dequeued:", value)
    def display(self):
        cur, values = self.front, []
        while cur: values.append(str(cur.data)); cur = cur.next
        print("Front ->", " -> ".join(values) if values else "Empty", "<- Rear")
def main():
    q = LinkedQueue()
    while True:
        print("\n1.Enqueue 2.Dequeue 3.Display 4.Exit")
        c = input("Choice: ").strip()
        if c == "1": q.enqueue(input("Value: "))
        elif c == "2": q.dequeue()
        elif c == "3": q.display()
        elif c == "4": break
        else: print("Invalid choice")
if __name__ == "__main__": main()
