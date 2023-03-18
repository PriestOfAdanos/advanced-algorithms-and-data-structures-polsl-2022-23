def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal(graph):
    result = []
    edges = []

    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((weight, node, neighbor))
            
    edges.sort()
    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}

    for edge in edges:
        weight, u, v = edge
        u_root = find(parent, u)
        v_root = find(parent, v)

        if u_root != v_root:
            result.append(edge)
            union(parent, rank, u_root, v_root)
            
            if len(result) == len(graph) - 1:
                break

    return result

graph = {
    'A': [('B', 7), ('D', 5)],
    'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
    'C': [('B', 8), ('E', 5)],
    'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
    'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
    'F': [('D', 6), ('E', 8), ('G', 11)],
    'G': [('E', 9), ('F', 11)],
}

print("Minimum Spanning Tree using Kruskal's Algorithm:")
for edge in kruskal(graph):
    print(edge)