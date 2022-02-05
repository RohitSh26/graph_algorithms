graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def breath_first(graph, root):

    # create a queue
    queue = [root]

    # while queue is not empty
    while len(queue) > 0:

        # get the front of queue and set it to current
        current = queue.pop(0)

        # print the current node
        print(current)

        # now add nodes to queue
        for n in graph[current]:
            queue.append(n)

breath_first(graph, 'a')
