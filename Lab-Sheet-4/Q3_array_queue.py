class ArrayQueue:
    def __init__(self, capacity=100): self.items, self.capacity = [], capacity
    def enqueue(self, value):
        if len(self.items) == self.capacity: print("Queue is full")
        else: self.items.append(value); print(value, "enqueued")
    def dequeue(self):
        if not self.items: print("Queue is empty")
        else: print("Dequeued:", self.items.pop(0))
    def display(self): print("Front ->", " -> ".join(map(str, self.items)), "<- Rear")
def main():
    q = ArrayQueue()
    while True:
        print("\n1.Enqueue 2.Dequeue 3.Display 4.Exit")
        c = input("Choice: ").strip()
        if c == "1": q.enqueue(input("Value: "))
        elif c == "2": q.dequeue()
        elif c == "3": q.display()
        elif c == "4": break
        else: print("Invalid choice")
if __name__ == "__main__": main()
