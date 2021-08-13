# Lab06. https://cs61a.org/lab/sol-lab06/
# Q2, Q3 subsequences. [find these difficult]
# You can mutate a slice of a list using slice assignment. The slice and the given list need not be the same length.
>>> a = [1, 2, 3, 4, 5, 6]
>>> a[2:5] = [10, 11, 12, 13]
>>> a
[1, 2, 10, 11, 12, 13, 6]
# Q2 subsequence
def insert_into_all(item, nested_list):
    """Return a new list consisting of all the lists in nested_list, but with item added to the front of each. You can assuming that nested_list is a list of lists.
    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    return [[item] + lst for lst in nested_list]

def subseqs(s):
    """Return a nested list (a list of lists) of all subsequences of S.
    The subsequences can appear in any order. You can assume S is a list.

    >>> subseqs([])
    [[]]
    """
    if not s:
        return [[]]
    else:
        subset = subseqs(s[1:])
        return insert_into_all(s[0], subset) + subset
"""
test: seqs = subseqs([1, 2, 3])
>>> sorted(seqs)
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

[1, 2, 3] != []
subset = subseqs([2, 3])
return insert_into_all(1, subseqs([2, 3])) + subseqs([2, 3])
--> return insert_into_all(1, [[2, 3], [2], [3], []]) + [[2, 3], [2], [3], []]
--> [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]

subseqs([2, 3])
[2, 3] != []
subset = subseqs([3])
return insert_into_all(2, subseqs([3])) + subseqs([3])
--> return insert_into_all(2, [[3], []]) + [[3], []]
--> [[2, 3], [2], [3], []]

subseqs([3])
[3] != []
subset = subseqs([])
return insert_into_all(3, subseqs([])) + subseqs([]) 
--> return insert_into_all(3, [[]]) + [[]]
--> [[3], []]

subseqs([])
[[]]
"""

# Q3 Non-Decreasing Subsequences
def non_decrease_subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences of S (a list of lists) for which the elements of the subsequence are strictly nondecreasing. The subsequences can appear in any order.
    
    >>> non_decrease_subseqs([])
    [[]]
    >>> seqs2 = non_decrease_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
    def subseq_helper(s, prev):
        if not s:
            return [[]] 
        elif s[0] < prev:
            return subseq_helper(s[1:], prev) 
        # prev is the bigger number, then hold prev, and compare prev with the rest numbers in s
        else:
            a = subseq_helper(s[1:], s[0]) # s[0] is the larger number, then use s[0] to compare with the rest numbers
            b = subseq_helper(s[1:], prev) # leave s[0] behind
            return insert_into_all(s[0], a) + b
    return subseq_helper(s, 0)

"""test 
>>> seqs = non_decrease_subseqs([1, 3, 2])
>>> sorted(seqs)
[[], [1], [1, 2], [1, 3], [2], [3]]

s = [1, 3, 2]
prev initialized to 0
subseq_helper([1, 3, 2], 0)
s[0] = 1 
s[0] > prev
a = subseq_helper([3, 2], 1)
b = subseq_helper([3, 2], 0)
return insert_into_all(1, a) + b
[[1, 3], [1, 2], [1]] + [[3], [2], []]
--> [[1, 3], [1, 2], [1], [3], [2], []]

a:
subseq_helper([3, 2], 1)
s[0] = 3, prev = 1 
s[0] > prev
a' = subseq_helper([2], 3)
b' = subseq_helper([2], 1)
return insert_into_all(3, a') + b'
--> return insert_into_all(3, [[]]) + [[2], []] 
-->  [[3], [2], []] 

a':
subseq_helper([2], 3)
s[0] = 2, prev = 3
s[0] < prev
return subseq_helper([], 3)
subseq_helper([], 3)
return [[]]

b':
subseq_helper([2], 1)
s[0] = 2, prev = 1
s[0] > prev
a'' = subseq_helper([], 2) --> [[]]
b'' = subseq_helper([], 1) --> [[]]
return insert_into_all(2, a'') + b''
--> insert_into_all(2, [[]]) + [[]]
--> [[2], []] 

b:
subseq_helper([3, 2], 0)
s[0] = 3, prev = 0
s[0] > prev
a''' = subseq_helper([2], 3) 
       s[0] = 2, prev = 3
       s[0] < prev
       return subseq_helper([], 3) --> [[]]
b''' = subseq_helper([2], 0)
       s[0] = 2, prev = 0
       s[0] > prev
       a'''' = subseq_helper([], 2) --> [[]]
       b'''' = subseq_helper([], 0) --> [[]]
       return insert_into_all(2, [[]]) + [[]] --> [[2], []]
return insert_into_all(3, [[]]) + [[2], []] --> [[3], [2], []]

"""

# Q5 shuffle
def card(n):
    """Return the playing card numeral as a string for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

suits = ['♡', '♢', '♤', '♧'] # str
cards = [card(n) + suit for n in range(1,14) for suit in suits] # list
cards[:12]
['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']

# Q6 same_shape
"""map function.
>> map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
Syntax: map(fun, iter)
Parameters :
  fun : It is a function to which map passes each element of given iterable.
  iter : It is a iterable which is to be mapped.

# example 1: 
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# example 2 List of strings, map() can listify the list of strings individually
l = ['sat', 'bat', 'cat', 'mat']
test = list(map(list, l))
print(test)
# --> [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]
"""

# Q7 hard **
# turn to python tutor for this question.
"""zip function: to map the similar index of multiple containers so that they can be used just using as single entity. 
Syntax: zip(*iterators) 
Parameters: Python iterables or containers (list, string etc) 
Return Value: Returns a single iterator object, having mapped values from all the containers.
"""
---------------------------------------------------




# Lab07 https://cs61a.org/lab/sol-lab07/#iterators
""" [some notes and concepts]
We define an iterable as an object on which calling the built-in function iter function returns an iterator. 
1) An iterable is any object that can be iterated through, or gone through one element at a time.
2) An iterator is another type of object that allows us to iterate through an iterable by keeping track of which element is next in the sequence.

iterator = iter(iterable)
next(iterator) ✨ 

3) next(iter(list_iter)) # Calling iter on an iterator returns itself
4) you cannot call next directly on an iterable.
>>> lst = [1, 2, 3, 4]
>>> next(lst)           # Calling next on an iterable
TypeError: 'list' object is not an iterator
5) all iterators are iterables, not all iterables are iterators. 

6) Great explanation.
Analogy: An iterable is like a book (one can flip through the pages) and an iterator for a book would be a bookmark (saves the position and can locate the next page). Calling iter on a book gives you a new bookmark independent of other bookmarks, but calling iter on a bookmark gives you the bookmark itself, without changing its position at all. Calling next on the bookmark moves it to the next page, but does not change the pages in the book. Calling next on the book wouldn't make sense semantically. We can also have multiple bookmarks, all independent of each other.
"""

---------------------------------------------------




# Discussion07 https://cs61a.org/disc/sol-disc07/#inheritance
# Normally when defining an __init__ method in a subclass, we take some additional action to calling super().__init__. For example, we could add a new instance variable like the following:
def __init__(self, name, owner, has_floppy_ears):
    super().__init__(name, owner)
    self.has_floppy_ears = has_floppy_ears

super().__init__()
Butterfly.__init__(self)

# Q8
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives
    def talk(self):
        print(self.name + ' says meow!')

class NoisyCat(Cat):
    super().talk()
    super().talk()
     # alternatively, you can use Cat.talk(self) here
""" NoisyCat('Magic', 'James').talk()
    Magic says meow!
    Magic says meow!
"""        

# Q10 Fibonacci Generator https://cs61a.org/disc/sol-disc07/#q10
"""Difficulty: ⭐⭐
Construct the generator function fib_gen, which when called returns a generator that yields elements of the Fibonacci sequence in order. Hint: consider using the zip function.

Try solving this problem iteratively, then try to find a recursive solution using the template.
"""
def fib_gen(): # ?? ❓
    """
    >>> fg = fib_gen()
    >>> for _ in range(7):
    ...     print(next(fg))
    0
    1
    1
    2
    3
    5
    8
    """
    yield from [0, 1]
    a = fib_gen()
    next(a)
    for x, y in zip(a, fib_gen()):
        yield x + y
        
# Q11 Cucumber - Fall 2015 Final Q7 https://cs61a.org/disc/sol-disc07/#q11
"""Difficulty: ⭐⭐

Cucumber is a card game. Cards are positive integers (no suits). Players are numbered from 0 up to players (0, 1, 2, 3 in a 4-player game).
In each Round, the players each play one card, starting with the starter and in ascending order (player 0 follows player 3 in a 4-player game). If the card played is as high or higher than the highest card played so far, that player takes control. The winner is the last player who took control after every player has played once.
Implement Round so that Game behaves as described in the doctests below.
"""

# Q12 Partition Generator
"""Difficulty: ⭐⭐⭐
Construct the generator function partition_gen, which takes in a number n and returns an n-partition iterator. An n-partition iterator yields partitions of n, where a partition of n is a list of integers whose sum is n. The iterator should only return unique partitions; the order of numbers within a partition and the order in which partitions are returned does not matter.
"""
def partition_gen(n):
    """
    >>> for partition in partition_gen(4): # note: order doesn't matter
    ...     print(partition)
    [4]
    [3, 1]
    [2, 2]
    [2, 1, 1]
    [1, 1, 1, 1]
    """
    def yield_helper(j, k):
        if j == 0:
            yield []
        elif k > 0 and j > 0:
            for small_part in yield_helper(j-k, k):
                yield [k] + small_part
            yield from yield_helper(j, k - 1)
    yield from yield_helper(n, n)
    
---------------------------------------------

        
    
    
    
    
# hw4 https://cs61a.org/hw/sol-hw04/#q2
def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a list of the elements in SEQ in a different order. The permutations may be yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    if not seq:
        yield []
    else:
        for perm in permutations(seq[1:]):
            for i in range(len(seq)):
                yield perm[:i] + [seq[0]] + perm[i:]

"""
permutations([1, 2, 3])
[1, 2, 3], [1, 3, 2]
[2, 1, 3], [2, 3, 1]
[3, 1, 2], [3, 2, 1]
"""

# Q3: Generators generator
def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g."""    
    def gener(x):
        for e in g():
            yield e
            if e == x:
                return
    for e in g():
        yield gener(e)
""">>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while (i <= n):
    ...         yield i
    ...         i += m
    ...
    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9 
    """

        
        
        
        
        
# lab8 https://cs61a.org/lab/sol-lab08/
"""
>> To check if a linked list is empty, compare it against the class attribute Link.empty. 
>> The rest attribute of any Link instance must be either Link.empty or another Link instance! 
"""
# Q6
def add_d_leaves(t, v):
    """Add d leaves containing v to each node at every depth d.

    >>> t_one_to_four = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> print(t_one_to_four)
    1
      2
      3
        4
    >>> add_d_leaves(t_one_to_four, 5)
    >>> print(t_one_to_four)
    1
      2
        5
      3
        4
          5
          5
        5
        """
    def add_leaves(t, d):
        
        """Adds a number of leaves to each node in t equivalent to the depth of
        the node, assuming that the root node is at depth d, the children of
        the root node are at depth d + 1, and so on."""
        
        for b in t.branches:
            add_leaves(b, d + 1) 
        t.branches.extend([Tree(v) for _ in range(d)])
    add_leaves(t, 0)

"""
each recursive call should've successfully added the correct number of leaves at each node in each branch. 
That means that the only step left is to add the correct number of leaves to the current node!
Do we need an explicitly base case? Let's take a look at what happens when t is a leaf. In that case, t.branches would be an empty list, so we would not enter the for loop. Then, the function will extend t.branches, which is an empty list, by a list containing the new leaves. This is exactly the desired result, so no base case is needed!
"""






# discussion 8 https://cs61a.org/disc/sol-disc08/#exam-prep

# Question5: flip twoCompare the recursive solution and the iterative approach

# examprep, difficult Question9 - question 11
"""Q9: Node Printer
Difficulty: ⭐⭐_

Your friend wants to print out all of the values in some trees. 
(a function that takes in a tree and returns a node-printing function.) 
When you call a node-printing function, it prints out the label of one node in the tree. Each time you call the function it will print the label of a different node. You may assume that your friend is polite and will not call your function after printing out all of the tree's node labels. You may print the labels in any order, so long as you print the label of each node exactly once.
"""
def node_printer(t):
    """
    >>> t1 = Tree(1, [Tree(2,
    ...                   [Tree(5),
    ...                    Tree(6, [Tree(8)])]),
    ...               Tree(3),
    ...               Tree(4, [Tree(7)])])
    >>> printer = node_printer(t1)
    >>> for _ in range(8): # NOTE: it's okay to fail this test if all 8 are printed once
    ...     printer()
    1
    2
    3
    4
    5
    6
    7
    8
    """
    to_explore = [t]
    def step():
        node = to_explore.pop(0) 
        print(node.label) # the label of tree t
        to_explore.extend(node.branches) # add tree t's branches back to it
    return step

"""Q10: Iterator Tree Link Tree Iterator
Difficulty: ⭐⭐
Part A: Fill out the function funcs, which is a generator that takes in a linked list link and yields functions.
The linked list link defines a path from the root of the tree to one of its nodes, with each element of link specifying which branch to take by index. Applying all functions sequentially to a Tree instance will evaluate to the label of the node at the end of the specified path.

For example, using the Tree t defined in the code, funcs(Link(2)) yields 2 functions. The first gets the third branch from t -- the branch at index 2 -- and the second function gets the label of this branch.
>>> func_generator = funcs(Link(2)) # get label of third branch
>>> f1 = next(func_generator)
>>> f2 = next(func_generator)
>>> f2(f1(t))
4
"""

def funcs(link):
    """
    >>> t = Tree(1, [Tree(2,
    ...                   [Tree(5),
    ...                    Tree(6, [Tree(8)])]),
    ...               Tree(3),
    ...               Tree(4, [Tree(7)])])
    >>> print_tree(t)
    1
      2
        5
        6
          8
      3
      4
        7
    >>> func_generator = funcs(Link.empty) # get root label
    >>> f1 = next(func_generator) 
    >>> f1(t)
    1
    >>> func_generator = funcs(Link(2)) # get label of third branch
    >>> f1 = next(func_generator)
    >>> f2 = next(func_generator)
    >>> f2(f1(t))
    4
    >>> # This just puts the 4 values from the iterable into f1, f2, f3, f4
    >>> f1, f2, f3, f4 = funcs(Link(0, Link(1, Link(0))))
    >>> f4(f3(f2(f1(t))))     ❓# what does this test means?
    8
    """
    if link is Link.empty:
        yield lambda t: t.label
    else:
        yield lambda t: t.branches[link.first]
        yield from funcs(link.rest)


"""Part B: Using funcs from above, fill out the definition for apply, which applies g to the element in t who's position is at the end of the path defined by link."""
def apply(g, t, link):
    """
    >>> t = Tree(1, [Tree(2,
    ...                   [Tree(5),
    ...                    Tree(6, [Tree(8)])]),
    ...               Tree(3),
    ...               Tree(4, [Tree(7)])])
    >>> print_tree(t)
    1
      2
        5
        6
          8
      3
      4
        7
    >>> apply(lambda x: x, t, Link.empty) # root label
    1
    >>> apply(lambda x: x, t, Link(0))    # label at first branch
    2
    >>> apply(lambda x: x * x, t, Link(0, Link(1, Link(0))))
    64
    """
    for f in funcs(link):
        t = f(t)
    return g(t)

t = Tree(1, [Tree(2,
                [Tree(5),
                 Tree(6, [Tree(8)])]),
             Tree(3),
             Tree(4, [Tree(7)])])

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.
    """
    print('  ' * indent + str(t.label))
    for b in t.branches:
        print_tree(b, indent + 1)




# homework05 


