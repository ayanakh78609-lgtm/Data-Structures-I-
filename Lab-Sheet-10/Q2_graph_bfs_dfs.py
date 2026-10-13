from collections import deque

graph = {"A":["B","C"], "B":["A","D","E"], "C":["A","F"], "D":["B"], "E":["B","F"], "F":["C","E"]}
nodes=list(graph)
print("Adjacency list:",graph)
print("Adjacency matrix:")
print("  ",*nodes)
for node in nodes: print(node, *[1 if neighbour in graph[node] else 0 for neighbour in nodes])
def bfs(start):
    visited={start}; queue=deque([start]); order=[]
    while queue:
        node=queue.popleft(); order.append(node)
        for nxt in graph[node]:
            if nxt not in visited: visited.add(nxt); queue.append(nxt)
    return order
def dfs(start):
    visited=set(); order=[]
    def visit(node):
        visited.add(node); order.append(node)
        for nxt in graph[node]:
            if nxt not in visited: visit(nxt)
    visit(start); return order
print("BFS from A:", bfs("A")); print("DFS from A:", dfs("A"))
