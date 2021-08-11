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
