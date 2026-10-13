import heapq
from itertools import count
class Node:
    def __init__(self, char=None, left=None, right=None): self.char, self.left, self.right = char, left, right

def huffman_codes(freq):
    serial = count()
    heap = [(f, next(serial), Node(char=c)) for c, f in freq.items()]
    heapq.heapify(heap)
    if not heap: return {}
    if len(heap) == 1: return {heap[0][2].char: "0"}
    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap); f2, _, right = heapq.heappop(heap)
        heapq.heappush(heap, (f1 + f2, next(serial), Node(left=left, right=right)))
    result = {}
    def walk(node, code):
        if node.char is not None: result[node.char] = code; return
        walk(node.left, code + "0"); walk(node.right, code + "1")
    walk(heap[0][2], "")
    return result

if __name__ == "__main__":
    frequencies = {"A": 5, "B": 9, "C": 12, "D": 13, "E": 16, "F": 45}
    print("Huffman Codes:")
    for char, code in sorted(huffman_codes(frequencies).items()): print(f"{char}: {code}")
