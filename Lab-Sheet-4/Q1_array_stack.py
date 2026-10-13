class ArrayStack:
    def __init__(self, capacity=100): self.items, self.capacity = [], capacity
    def push(self, value):
        if len(self.items) == self.capacity: print("Stack overflow")
        else: self.items.append(value); print(value, "pushed")
    def pop(self):
        if not self.items: print("Stack underflow")
        else: print("Popped:", self.items.pop())
    def display(self): print("Stack (bottom to top):", self.items)

def main():
    s = ArrayStack()
    while True:
        print("\n1.Push 2.Pop 3.Display 4.Exit")
        c = input("Choice: ").strip()
        if c == "1": s.push(input("Value: "))
        elif c == "2": s.pop()
        elif c == "3": s.display()
        elif c == "4": break
        else: print("Invalid choice")
if __name__ == "__main__": main()
