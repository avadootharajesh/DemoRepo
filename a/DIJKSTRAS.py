
# Dijkstra's Shortest Path Algorithm

import heapq as heap

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heap.heappop(pq)
        if current_distance > distances[current_node]: continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heap.heappush(pq, (distance, neighbor))
    return distances


graph = {
    'a': {'b': 5, 'c': 1},
    'b': {'a': 5, 'c': 2, 'd': 1},
    'c': {'a': 1, 'b': 2, 'd': 4, 'e': 8},
    'd': {'b': 1, 'c': 4, 'e': 3, 'f': 6},
    'e': {'c': 8, 'd': 3},
    'f': {'d': 6}
}

print(dijkstra(graph, 'a'))