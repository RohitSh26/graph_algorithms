class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
def depth_first_values(root):
    result = []
    if root == None: return result

    stack = [root]
    
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)

        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
        
    return result
print(depth_first_values(a))

#   -> ['a', 'b', 'd', 'e', 'c', 'f']