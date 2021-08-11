
# https://cs61a.org/disc/sol-disc05/#trees-implementation 
#Q5
def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    t = tree(3,
          [tree(5,
             [tree(1)]),
           tree(2)])
    """
    if is_leaf(t):
        return 0
    return 1 + max([height(branch) for branch in branches(t)])
# is_leaf(t3) --> False, return 1 + max(height(t5), height(t2))
# height(t5) --> return 1 + max(height(t1)) --> 1 + max(0) --> 1
# height(t2) --> return 0

# Q6
"""if is_leaf(t):
      return label(t)
"""
# Q7
#Leaf: A node that has no branches. (leaf is also a node)
def find_path(tree, x):
    if label(tree) == x:
        return [label(tree)]
    paths = [find_path(b, x) for b in branches(tree)] 
# find the path from my branch to the same value.
# the variable path is gonna has a list of different paths, only one of the paths will return a valid path, else -> empty list.
# if we don't find the path, it will not return to us a list.
    for path in paths: 
        if path: # if this path exist
            return [label(tree)] + path
""" test: 
t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
find_path(t, 5)
>>> 
label(t2) == 5 --> False
find_path(t7, 5) --> find_path(t3, 5) None
                     find_path(t6, 5) --> find_path(t5, 5) --> return label(t7) --> 7
                                          find_path(t11, 5) None
find_path(t15, 5) None
"""
    
    
    
