# https://cs61a.org/lab/sol-lab06/
# Q2, Q3 subsequences. 
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
"""Using map function.
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
Syntax: map(fun, iter)
Parameters :
  fun : It is a function to which map passes each element of given iterable.
  iter : It is a iterable which is to be mapped.
"""
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

# Q7 hard **
# turn to python tutor for this question.
"""zip function: to map the similar index of multiple containers so that they can be used just using as single entity. 
Syntax: zip(*iterators) 
Parameters: Python iterables or containers (list, string etc) 
Return Value: Returns a single iterator object, having mapped values from all the containers.
"""








# Lab07 https://cs61a.org/lab/sol-lab07/#iterators
""" We define an iterable as an object on which calling the built-in function iter function returns an iterator. 
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
