class MinHeap:
    def __init__(self): self.a = []
    def push(self, x):
        self.a.append(x); i = len(self.a) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.a[p] <= self.a[i]: break
            self.a[p], self.a[i] = self.a[i], self.a[p]; i = p
    def pop(self):
        if not self.a: raise IndexError("empty heap")
        root = self.a[0]; last = self.a.pop()
        if self.a:
            self.a[0] = last; i = 0
            while True:
                left, right = 2*i+1, 2*i+2; smallest = i
                if left < len(self.a) and self.a[left] < self.a[smallest]: smallest = left
                if right < len(self.a) and self.a[right] < self.a[smallest]: smallest = right
                if smallest == i: break
                self.a[i], self.a[smallest] = self.a[smallest], self.a[i]; i = smallest
        return root
class MaxHeap:
    def __init__(self): self.a = []
    def push(self, x):
        self.a.append(x); i = len(self.a)-1
        while i > 0:
            p = (i-1)//2
            if self.a[p] >= self.a[i]: break
            self.a[p], self.a[i] = self.a[i], self.a[p]; i = p
    def pop(self):
        if not self.a: raise IndexError("empty heap")
        root = self.a[0]; last = self.a.pop()
        if self.a:
            self.a[0] = last; i = 0
            while True:
                left, right = 2*i+1, 2*i+2; largest = i
                if left < len(self.a) and self.a[left] > self.a[largest]: largest = left
                if right < len(self.a) and self.a[right] > self.a[largest]: largest = right
                if largest == i: break
                self.a[i], self.a[largest] = self.a[largest], self.a[i]; i = largest
        return root
if __name__ == "__main__":
    values = [40, 10, 30, 50, 20]
    mn, mx = MinHeap(), MaxHeap()
    for x in values: mn.push(x); mx.push(x)
    print("Min heap array:", mn.a); print("Min root removed:", mn.pop()); print("After removal:", mn.a)
    print("Max heap array:", mx.a); print("Max root removed:", mx.pop()); print("After removal:", mx.a)
