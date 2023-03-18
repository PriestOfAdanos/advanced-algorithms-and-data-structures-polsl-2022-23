import heapq
import pprint 

def bellman_ford(graph, source):
    distance = {node: float('inf') for node in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                new_distance = distance[node] + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance

    for node in graph:
        for neighbor, weight in graph[node]:
            if distance[node] + weight < distance[neighbor]:
                raise ValueError("Graf zawiera cykl o ujemnej wadze")

    return distance

def dijkstra(graph, source):
    distance = {node: float('inf') for node in graph}
    distance[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        dist, node = heapq.heappop(priority_queue)
        if dist > distance[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = distance[node] + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distance

def johnson(graph):
    new_node = "NEW_NODE"
    new_graph = {**graph, new_node: [(node, 0) for node in graph]}

    weight_adjustments = bellman_ford(new_graph, new_node)
    del new_graph[new_node]

    adjusted_graph = {}
    for node, edges in graph.items():
        adjusted_graph[node] = [(neighbor, weight + weight_adjustments[node] - weight_adjustments[neighbor]) for neighbor, weight in edges]

    all_pairs_shortest_paths = {}
    for node in graph:
        shortest_paths = dijkstra(adjusted_graph, node)
        all_pairs_shortest_paths[node] = {neighbor: dist + weight_adjustments[neighbor] - weight_adjustments[node] for neighbor, dist in shortest_paths.items()}

    return all_pairs_shortest_paths

# Przykład użycia
graph = {
    'A': [('B', 3), ('C', 8), ('D', 4)],
    'B': [('E', 1), ('D', 7)],
    'C': [('B', 4)],
    'D': [('C', 6), ('E', 6)],
    'E': [('A', 2), ('B', -1)],
}



shortest_paths = johnson(graph)
print("graph: ")
pprint.pprint(graph, indent=2)
print("shortest_paths: ")
pprint.pprint(shortest_paths)
input()