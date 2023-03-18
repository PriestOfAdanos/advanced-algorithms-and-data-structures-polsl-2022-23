from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def __repr__(self):
        edges = sum(len(adj) for adj in self.adj_list.values()) // 2
        return f"Graph with {self.V} vertices and {edges} edges:\n{self.adj_list}"
    
    def smallest_last_vertex_coloring(self):
        # Sort vertices by degree in ascending order
        sorted_vertices = sorted(self.adj_list.keys(), key=lambda v: len(self.adj_list[v]))

        # Initialize the result dictionary with vertex-color pairs
        result = {v: -1 for v in sorted_vertices}

        # Color the vertices
        for v in sorted_vertices:
            used_colors = set(result[u] for u in self.adj_list[v] if result[u] != -1)
            for color in range(self.V):
                if color not in used_colors:
                    result[v] = color
                    break

        return result

# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

vertex_colors = g.smallest_last_vertex_coloring()
print("Graph:")
print(g)
print("Vertex colors:")
for vertex, color in vertex_colors.items():
    print(f"Vertex {vertex}: Color {color}")
