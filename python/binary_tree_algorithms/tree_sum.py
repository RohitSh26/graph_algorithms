class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1


def tree_sum(root):
    if root is None: return 0

    total = 0
    stack = [root]
    
    while len(stack) > 0:
        current = stack.pop()
        total += current.val

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return total

print(tree_sum(a))  # -> 21
