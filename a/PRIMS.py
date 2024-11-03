
# Prim's Algorithm

import heapq as heap

def prims(graph, start=0):
    
    n = len(graph)
    mincost = 0
    minedges = []
    
    visited = set()
    minheap = [(0, start, -1)]
    
    while minheap and len(visited) < n:
        
        cost, node, parent = heap.heappop(minheap)
        
        if node in visited: continue
        
        mincost += cost
        visited.add(node)
        
        if parent != -1: minedges.append((parent, node))
        
        for vertex, weight in graph[node]:
            if vertex not in visited:
                heap.heappush(minheap, (weight, vertex, node))
    
    return mincost, minedges

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (4, 8)],
    2: [(1, 3), (4, 5)],
    3: [(0, 6), (2, 5), (4, 9)],
    4: [(1, 8), (2, 5), (3, 9)]
}

mincost, minedges = prims(graph)
print(f'Minimum cost: {mincost}')
print(f'Minimum edges: {minedges}')

for u, v, w in minedges:
    print(f'{u} -> {v} ({w})')