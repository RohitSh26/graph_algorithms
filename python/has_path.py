graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

def has_path(graph, src, dst):
    
    if src == dst: return True

    for n in graph[src]:
        if has_path(graph, n, dst) == True: return True
    
    return False

result = has_path(graph, 'f', 'k') # True
print(result)