
graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


def largest_component(graph):
    visited = set()
    max = 0
    for node in graph:
        ret = traverse_graph(graph, node, visited)
        if(ret == True):
            if len(visited) > max:
                max = len(visited)
            visited = set()

    return max


def traverse_graph(graph, node, visited):

    if(node in visited):
        return False

    visited.add(node)
    for n in graph[node]:
        traverse_graph(graph, n, visited)

    return True


print(largest_component(graph))  # -> 2
