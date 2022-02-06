import re


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

"""
Finds if there a path between two nodes A and B
"""
def undirected_path(edges, node_A, node_B):
  
  # convert edges into graph
  graph = convert_edges_into_adjency_list(edges)

  # call a method that would return if there is a path or not
  return has_path(graph, node_A, node_B, set())

def has_path(graph, src, dst, visited_nodes):

    if src == dst: return True

    if src in visited_nodes: return
    
    visited_nodes.add(src)

    for n in graph[src]:
        if has_path(graph, n, dst, visited_nodes): return True

    return False

"""
Converts edges in to adjency list graph
"""
def convert_edges_into_adjency_list(edges):

    graph = {}
    
    for x, y in edges:

        if(x not in graph): graph[x] = []
        if(y not in graph): graph[y] = []

        graph[x].append(y)
        graph[y].append(x)

    return graph

print(convert_edges_into_adjency_list(edges))

print(undirected_path(edges, 'm', 'j') )# -> True