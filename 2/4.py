import pprint
import heapq

def prim(graph):
    start_node = list(graph.keys())[0]  # Select an arbitrary starting node
    visited = set()
    min_spanning_tree = []
    edges = []

    # Add all edges connected to the starting node
    for neighbor, weight in graph[start_node]:
        heapq.heappush(edges, (weight, start_node, neighbor))

    while edges:
        weight, src, dest = heapq.heappop(edges)

        if dest not in visited:
            visited.add(dest)
            min_spanning_tree.append((src, dest, weight))

            # Add new edges connected to the visited node
            for neighbor, edge_weight in graph[dest]:
                if neighbor not in visited:
                    heapq.heappush(edges, (edge_weight, dest, neighbor))

    return min_spanning_tree

# Example usage:
graph = {
    'A': [('B', 7), ('D', 5)],
    'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
    'C': [('B', 8), ('E', 5)],
    'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
    'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
    'F': [('D', 6), ('E', 8), ('G', 11)],
    'G': [('E', 9), ('F', 11)],
}

pprint.pprint(graph)

print("Edges:")

mst = prim(graph)
print("Minimum Spanning Tree using Prim's Algorithm:")
for edge in mst:
    print(edge)
input()