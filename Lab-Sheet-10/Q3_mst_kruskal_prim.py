import heapq

def kruskal(vertices, edges):
    parent={v:v for v in vertices}; rank={v:0 for v in vertices}
    def find(x):
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra==rb:return False
        if rank[ra]<rank[rb]: parent[ra]=rb
        elif rank[ra]>rank[rb]: parent[rb]=ra
        else: parent[rb]=ra; rank[ra]+=1
        return True
    result=[]; cost=0
    for u,v,w in sorted(edges,key=lambda e:e[2]):
        if union(u,v): result.append((u,v,w)); cost+=w
    return result,cost

def prim(graph, start):
    visited={start}; heap=[]; result=[]; cost=0
    for v,w in graph[start]: heapq.heappush(heap,(w,start,v))
    while heap and len(visited)<len(graph):
        w,u,v=heapq.heappop(heap)
        if v in visited: continue
        visited.add(v); result.append((u,v,w)); cost+=w
        for nxt,weight in graph[v]:
            if nxt not in visited: heapq.heappush(heap,(weight,v,nxt))
    return result,cost

if __name__ == "__main__":
    vertices=["A","B","C","D","E"]
    edges=[("A","B",1),("A","C",3),("B","C",2),("B","D",4),("C","D",5),("C","E",6),("D","E",2)]
    graph={v:[] for v in vertices}
    for u,v,w in edges: graph[u].append((v,w)); graph[v].append((u,w))
    e1,c1=kruskal(vertices,edges); e2,c2=prim(graph,"A")
    print("Kruskal MST edges:",e1,"Total cost:",c1)
    print("Prim MST edges:",e2,"Total cost:",c2)
