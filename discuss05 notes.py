
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
