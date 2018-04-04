def try_coloring(graph, num_colors):
    assert num_colors >= 0, "Invalid number of colors: %s" % num_colors
    colors = {}

    def neighbors_have_different_colors(nodes, color):
        return all(color != colors.get(n) for n in nodes)

    for node, adjacents in graph.items():

        found_color = False

        for color in range(num_colors):
            if neighbors_have_different_colors(adjacents, color):
                found_color = True
                colors[node] = color
                break

        if not found_color:
            return None

    return colors


def find_graph_colors(graph):
    for num_colors in range(1, len(graph)):
        colors = try_coloring(graph, num_colors)
        if colors:
            return colors


grafo = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
    }
print(try_coloring(grafo, 1))
print(try_coloring(grafo, 2))
