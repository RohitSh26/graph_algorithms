from re import S


graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

def connected_components_count(graph):
    count = 0
    visited = set()

    for node in graph:
        if(traverse_graph(graph, node, visited) == True):
            count += 1
    
    return count
        

def traverse_graph(graph, node, visited):

    if(node in visited): return False

    visited.add(node)

    for n in graph[node]:
        traverse_graph(graph, n, visited)

    return True

print(connected_components_count(graph)) # -> 2