#Discussion04
#https://cs61a.org/disc/sol-disc04/#q6
#Q3 

def closest_number(nums, target):
    return min(nums, key=lambda x: abs(target - x))   

"""min(iterable, *[, key, default])
iterable: An object capable of returning its members one at a time. 
Examples of iterables include all sequence types (such as list, str, and tuple) and 
some non-sequence types like dict, file objects, and objects of any classes you define with an __iter__() method or with a __getitem__() method that implements Sequence semantics.
"""

"""Q4
using nonconsecutive elements of the list, means if we include the current number, we cannot use the adjacent number.
base case: s == [ ]

Q5
The keys of a dictionary can be any immutable value, such as numbers, strings, and tuples.[1] Dictionaries themselves are mutable.
Hashable: means that some mutable objects, such as classes, can be used as dictionary keys.
Dictionaries cannot use other mutable data structures as keys.
"""

#Q6
# fn(e) is the same for all elements in that list.
# A list of key-value pairs can be converted into a dictionary by calling the dict constructor function.
# dict([(3, 9), (4, 16), (5, 25)])
# {3: 9, 4: 16, 5: 25}
def group_by(s, fn):
    grouped = {}
    for x in s:
        key = fn(x)
        if key in grouped:
            grouped[key].append(x)
        else:
            grouped[key] = [x]
    return grouped
""" determine if key is in dictionary.
pokemon = {'pikachu': 25, 'dragonair': 148}
'mewtwo' in pokemon
False
"""

"""test: 
group_by([12, 23, 14, 45], lambda p: p // 10)
x = 12
key = fn(12) --> 1
group[1] = 12
x = 14 
key = fn(14) --> 1
1 in grouped --> True
group[1].append(14) 
—> group[1]
—> [12,14]
"""

Q7
#base case: target == 0
##   elif not lst: ??
##       return False ??
""" test: subset_sum(4, [5, -2, 12])
(1) a = subset_sum(-1, [-2, 12])  false or false 
    a’ = subset_sum(-3, [12])  false
       a’’= subset_sum(-15, [ ]) false
       b’’= subset_sum(-3, [ ])  false
       # not [ ] —> true. 
    b’ = subset_sum(-1, [12]) false
       a’’= subset_sum(-13, [ ]) false
       b’’= subset_sum(-1, [ ])  false
       
(2) b = subset_sum(4, [-2, 12])
    a’ = subset_sum(6, [12])  false
       a’’= subset_sum(-6, [ ]) false
       b’’= subset_sum(6, [ ])  false
    b’ = subset_sum(4, [12]) false
       a’’= subset_sum(4-12, [ ]) false
       b’’= subset_sum(4, [ ])  false

a: 4 - lst[0] - lst[1] - lst[2] 
Till target == 0, then true.
All conditions: 
target- lst[0] - lst[1] - lst[2] 
target- lst[0] - lst[1] 

target- lst[0] - lst[2] 
target- lst[0]

target- lst[1] - lst[2] 
target- lst[1]

target- lst[2] 
target
"""

Q8
def intersection(lst_of_lsts):
    elements = []
    for elem in lst_of_lsts[0]:
        condition = elem not in elements # condition initialized as true.
        for lst in lst_of_lsts[1:]:
            if elem not in lst:     # if elem is in lst_of_lsts[1], then determine if elem is in the rest of lists
                condition = False   # —- > @2
        if condition:               # @1 # loop through all lists in lst, and elem in all lists
            elements = elements + [elem]
    return elements                 # @2
    
lsts2 = [[1, 4, 2, 6], [7, 2, 4], [4, 4]]
intersection(lsts2)


# lab notes Lab 04 
# list comprehension:
"""[<expression> for <element> in <sequence> if <conditional>]
"Compute the expression for each element in the sequence if the conditional is true for that element."
"""
# Relying on a data abstraction's underlying implementation is known as violating the abstraction barrier, and we never want to do this!
# The nature of the abstraction barrier guarantees that changing the implementation of an ADT shouldn't affect the functionality of any programs that use that ADT, as long as the constructors and selectors were used properly.

# Q6 
"""TA explanation.
(1) If t is a leaf, Use tree constructor.
Build a new tree in which the lable is the same as the original tree, but nodes values being leaves.
Input as a list, output a list, use list comprehension.

(2) if t is not a leaf, preserve the tree structure —-> call tree(lable(t), ...)
Call sprout_leaves to recurse over its branches. We want the branches to be the result of calling sprout_leaves on each branch.
Changing the current branch list, to a new branch list --> use list comprehension.
"""


# Discussion 05
"""	•	If the step size is left out, the default step size is 1.
	•	If the start index is left out, the default start index is the beginning of the list.
	•	If the end index is left out, the default end index is the end of the list.
	•	If the step size is negative, the default start index becomes the end of the list, and the default end index becomes the beginning of the list.

lst[:] creates a list that is identical to lst (a copy of lst)
lst[::-1] creates a list that has the same elements of lst, but reversed. 
Those rules still apply if more than just the step size is specified e.g. lst[3::-1].
refer to discussion05 for more exercises and examples.
"""

# 2.4.2 sequence objects.
chinese = ['coin', 'string', 'myriad']  # A list literal
suits = chinese                         # Two names refer to the same list
# Lists can be copied using the list constructor function. Changes to one list do not affect another, unless they share structure.
# Changing the list referenced by suits will affect the nested list that is the first element of nest, but not the other elements.





