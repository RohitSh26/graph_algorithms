def convert_edges_to_graph(edges):
    graph = {}
    for edge in edges:
        x, y = edge
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []

        graph[x].append(y)
        graph[y].append(x)

    return graph


def shortest_path(edges, node_A, node_B):
    graph = convert_edges_to_graph(edges)
    visited = set([node_A])
    queue = [[node_A, 0]]

    while len(queue) > 0:

        # remove and returm front of the queue
        [current, distance] = queue.pop(0)

        if current == node_B:
            return distance

        # for each neighbor of current node add it to the queue
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])

    return -1


edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]

print(shortest_path(edges, 'b', 'g'))  # -> -1
