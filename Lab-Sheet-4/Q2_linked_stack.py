class Node:
    def __init__(self, data): self.data, self.next = data, None
class LinkedStack:
    def __init__(self): self.top = None
    def push(self, value):
        node = Node(value); node.next = self.top; self.top = node; print(value, "pushed")
    def pop(self):
        if not self.top: print("Stack underflow"); return
        value = self.top.data; self.top = self.top.next; print("Popped:", value)
    def display(self):
        cur, values = self.top, []
        while cur: values.append(str(cur.data)); cur = cur.next
        print("Top ->", " -> ".join(values) if values else "Empty")
def main():
    s = LinkedStack()
    while True:
        print("\n1.Push 2.Pop 3.Display 4.Exit")
        c = input("Choice: ").strip()
        if c == "1": s.push(input("Value: "))
        elif c == "2": s.pop()
        elif c == "3": s.display()
        elif c == "4": break
        else: print("Invalid choice")
if __name__ == "__main__": main()
