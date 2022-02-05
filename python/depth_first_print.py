
from lib2to3.pgen2.token import RPAR
from locale import currency


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def depth_first(graph, root):
    # initialize stack with root
    stack = [root]

    # while there are nodes in stack
    while len(stack) > 0:
        # get the current node out from stack
        current = stack.pop()

        # print the current node
        print(current)

        # now push every neighbor of current node into stack
        for n in graph[current]:
            stack.append(n)

def depth_first_recursice(grapth, root):

    # initialize stack with root
    stack = [root]

    # get the current node out from stack
    current = stack.pop()

    # print the current node
    print(current)

    # now push every neighbor of current node into stack
    for n in graph[current]:
        depth_first_recursice(graph, n)


depth_first(graph, 'a')

depth_first_recursice(graph, 'a')