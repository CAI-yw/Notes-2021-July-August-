# replaced Loki! & all the pruning questions& “balanced” questions&hailstone questions

"""
Replacing
"""
# Question 1: Homework 03 Q4:Replace Loki at Leaf. https://cs61a.org/hw/sol-hw03/#q4
# Define replace_loki_at_leaf, which takes a tree t and a value lokis_replacement. replace_loki_at_leaf returns a new tree that's the same as t except that every leaf label equal to "loki" has been replaced with lokis_replacement.  

def replace_loki_at_leaf(t, lokis_replacement):
    """Returns a new tree where every leaf value equal to "loki" has
    been replaced with lokis_replacement.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('loki'),
    ...                         tree('freya')]),
    ...                   tree('frigg',
    ...                        [tree('loki')]),
    ...                   tree('loki',
    ...                        [tree('sif'),
    ...                         tree('loki')]),
    ...                   tree('loki')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_loki_at_leaf(yggdrasil, 'freya'))
    odin
      balder
        freya
        freya
      frigg
        freya
      loki
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    if is_leaf(t) and label(t) == "loki":
        return tree(lokis_replacement)
    else:
        bs = [replace_loki_at_leaf(b, lokis_replacement) for b in branches(t)]
        return tree(label(t), bs)



"""
Pruning
"""
# Question 1: Discussion 06  Q11: Pruning Leaves. https://cs61a.org/disc/sol-disc06/#q11
# Define a function prune_leaves that given a tree t and a tuple of values vals, produces a version of t with all its leaves that are in vals removed. Do not attempt to try to remove non-leaf nodes and do not remove leaves that do not match any of the items in vals. Return None if pruning the tree results in there being no nodes left in the tree.

def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    if is_leaf(t) and (label(t) in vals):
      return None
    new_branches = []
    for b in branches(t):
      new_branch = prune_leaves(b, vals)
      if new_branch:
        new_branches += [new_branch]
    return tree(label(t), new_branches)
  
# Question 2: Discussion 05 Q8: Perfectly Balanced and Pruned https://cs61a.org/disc/sol-disc05/#q8
# Difficulty: ⭐
# IMPORTANT: You may use as many lines as you want for these two parts.
# Challenge: Solve both of these parts with just 1 line of code each.
# Part A: Implement sum_tree, which takes adds together all the labels in a tree.
def sum_tree(t):
    """
    Add all elements in a tree.

    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    total = 0
    for b in branches(t):
        total += sum_tree(b)
    return label(t) + total

    # one line solution
    return label(t) + sum([sum_tree(b) for b in branches(t)])

# Part B: Implement balanced, a function which takes in a tree and returns whether each of the branches have the same total sum, and each branch is balanced.
def balanced(t):
    """
    Checks if each branch has same sum of all elements,
    and each branch is balanced.

    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(t, [t, tree(1)])
    >>> balanced(t)
    False
    """
    if not branches(t):
        return True
    for b in branches(t):
        if sum_tree(branches(t)[0]) != sum_tree(b) or not balanced(b):
            return False
    return True

    # one line solution
    return False not in [sum_tree(branches(t)[0]) == sum_tree(b) and balanced(b) for b in branches(t)]

# Part C: Implement prune_tree, a function which takes in a tree t as well as a function predicate that returns True or False for each label of each tree node. prune_tree returns a new tree where any node for which predicate of the label of that node returns True, then all the branches for that tree are pruned (not included in the new tree).
  def prune_tree(t, predicate):
    """
    Returns a new tree where any branch that has the predicate of the label
    of the branch returns True has its branches pruned.

    >>> prune_tree(tree(1, [tree(2)]), lambda x: x == 1) # prune at root
    [1]
    >>> prune_tree(tree(1, [tree(2)]), lambda x: x == 2) # prune at leaf
    [1, [2]]
    >>> prune_tree(test_tree, lambda x: x >= 3) # prune at 3, 4, and 5
    [1, [2, [4], [5]], [3]]
    >>> sum_tree(prune_tree(test_tree, lambda x: x > 10)) # prune nothing, add 1 to 9
    45
    >>> prune_tree(test_tree, lambda x: x > 10) == test_tree # prune nothing
    True
    """
    if predicate(label(t)) or is_leaf(t):
        return tree(label(t))
    return tree(label(t), [prune_tree(b, predicate) for b in branches(t)])

    # one line solution
    return tree(label(t), [prune_tree(b, predicate) for b in branches(t) if not predicate(label(t))])

test_tree = tree(1,
                [tree(2,
                    [tree(4,
                        [tree(8),
                            tree(9)]),
                    tree(5)]),
                tree(3,
                    [tree(6),
                    tree(7)])])
draw(test_tree)



  
"""
Having path
"""
# Question 1: Homework 03 Q5: Has Path https://cs61a.org/hw/sol-hw03/#q5
# Write a function has_path that takes in a tree t and a string word. It returns True if there is a path that starts from the root where the entries along the path spell out the word, and False otherwise. (This data structure is called a trie, and it has a lot of cool applications!---think autocomplete). You may assume that every node's label is exactly one character.

def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    if label(t) != word[0]:
        return False
    elif len(word) == 1:
        return True
    for b in branches(t):
        if has_path(b, word[1:]):
            return True
    return False

# Question 2: Discussion 05 Q6: Maximum Path Sum. https://cs61a.org/disc/sol-disc05/#q6
# Write a function that takes in a tree and returns the maximum sum of the values along any path in the tree. Recall that a path is from the tree's root to any leaf. 
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
      return label(t)
    else:
      return label(t) + max([max_path_sum(b) for b in branches(t)])
  
# Question 3: Discussion 05 Q7: Find Path  https://cs61a.org/disc/sol-disc05/#q6
# Write a function that takes in a tree and a value x and returns a list containing the nodes along the path required to get from the root of the tree to a node containing x.
# If x is not present in the tree, return None. Assume that the entries of the tree are unique.
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path

# Question 4: Discussion 05 Q11: Forest Path - Fall 2015 Final Q3 (a)(b)(d) https://cs61a.org/disc/sol-disc05/#q10
Difficulty: ⭐⭐⭐
Definition: A path through a tree is a list of adjacent node values that starts with the root value and ends with a leaf value. For example, the paths of tree(1, [tree(2), tree(3, [tree(4), tree(5)])]) are
[1, 2]
[1, 3, 4]
[1, 3, 5]
Part A: Implement bigpath, which takes a tree t and an integer n. It returns the number of paths in t whose sum is at least n. Assume that all node values of t are integers.

Part B: Implement allpath which takes a tree t, a one-argument predicate f, a two-argument reducing function g, and a starting value s. It returns the number of paths p in t for which f(reduce(g, p, s)) returns a truthy value. The reduce function is in the code. Pay close attention to the order of arguments to the f function in reduce. You do not need to call it, though.

Part C: Re-implement bigpath (Part A) using allpath (Part B). Assume allpath is implemented correctly.
def reduce(f, s, initial):
    """Combine elements of s pairwise
    using f, starting with initial.

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(pow, [2, 3, 1], 2)
    64
    """
    for x in s:
        initial = f(initial, x)
    return initial

# The one function defined below is used in the questions below 
# to convert truthy and falsy values into the numbers 1 and 0, respectively.
def one(b):
    if b:
        return 1
    else:
        return 0

def bigpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    3
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    if is_leaf(t):
        return one(label(t) >= n)
    return sum([bigpath(b, n - label(t)) for b in branches(t)])

def allpath(t, f, g, s):
    """ Return the number of paths p in t for which f(reduce(g, p, s)) is truthy.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> even = lambda x: x % 2 == 0
    >>> allpath(t, even, max, 0) # Path maxes are 2, 4, and 5
    2
    >>> allpath(t, even, pow, 2) # E.g., pow(pow(2, 1), 2) is even
    3
    >>> allpath(t, even, pow, 1) # Raising 1 to any power is odd
    0
    """
    if is_leaf(t):
        return one(f(g(s, label(t))))
    return sum([allpath(b, f, g, g(s, label(t))) for b in branches(t)])

from operator import add , mul

def bigpath_allpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath_allpath(t, 3)
    3
    >>> bigpath_allpath(t, 6)
    2
    >>> bigpath_allpath(t, 9)
    1
    """
    return allpath(t, lambda x: x >= n, add, 0)        
          
          
"""
Balanced
"""
# Question 1: Homework 03 Q2: Balanced https://cs61a.org/hw/sol-hw03/#q2
# Implement the balanced function, which returns whether m is a balanced mobile. A mobile is balanced if two conditions are met:  1) The torque applied by its left arm is equal to that applied by its right arm. The torque of the left arm is the length of the left rod multiplied by the total weight hanging from that rod. Likewise for the right. For example, if the left arm has a length of 5, and there is a mobile hanging at the end of the left arm of weight 10, the torque on the left side of our mobile is 50.  2) Each of the mobiles hanging at the end of its arms is balanced.
# Planets themselves are balanced, as there is nothing hanging off of them.

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'balanced', ['Index'])
    True
    """
    if is_planet(m):
        return True
    else:
        left_end, right_end = end(left(m)), end(right(m))
        torque_left = length(left(m)) * total_weight(left_end)
        torque_right = length(right(m)) * total_weight(right_end)
        return balanced(left_end) and balanced(right_end) and torque_left == torque_right
# The fact that planets are balanced is important, since we will be solving this recursively like many other tree problems (even though this is not explicitly a tree).
# Base case: if we are checking a planet, then we know that this is balanced. Why is this an appropriate base case? There are two possible approaches to this:
#   1) Because we know that our data structures so far are trees, planets are the simplest possible tree since we have chosen to implement them as leaves.
#   2) We also know that from an ADT standpoint, planets are the terminal item in a mobile. There can be no further mobile structures under this planet, so it makes sense to stop check here.
# Otherwise: note that it is important to do a recursive call to check if both arms are balanced. However, we also need to do the basic comparison of looking at the total weight of both arms as well as their length. For example if both arms are a planet, trivially, they will both be balanced. However, the torque must be equal in order for the entire mobile to balanced (i.e. it's insufficient to just check if the arms are balanced).


"""
other similar questions.
"""
# Question 1: Discussion05 Q10: Recursion on Tree ADT - Summer 2014 Midterm 1 Q7
# Difficulty: ⭐⭐
# Define a function dejavu, which takes in a tree of numbers t and a number n. It returns True if there is a path from the root to a leaf such that the sum of the numbers along that path is n and False otherwise.
# IMPORTANT: For this problem, the starter code template is just a suggestion. You are welcome to add/delete/modify the starter code template, or even write your own solution that doesn’t use the starter code at all.
def dejavu(t, n):
    """
    >>> my_tree = tree(2, [tree(3, [tree(5), tree(7)]), tree(4)])
    >>> dejavu(my_tree, 12) # 2 -> 3 -> 7
    True
    >>> dejavu(my_tree, 5) # Sums of partial paths like 2 -> 3 don ’t count
    False
    """
    if is_leaf(t):
        return n == label(t)
    for branch in branches(t):
        if dejavu(branch, n - label(t)):
            return True
    return False






