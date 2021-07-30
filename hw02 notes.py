"""some notes about 21s 61a.
hw02 TA notes, just for self-use.
Q1, version 1: focus on how we maniipulate the numbers; version 2: treat functions as their own thing(use compose1)
"""
def make_repeater(func, n): 
  def inner_func(x): #helper function
    k = 0 #tracker initialized as a number
    while k < n:
      x,k = func(x), k + 1 #loop through n times, apply func to x (keep track)
    return x 
  return inner_func

def make_repeater(func, n): 
  g = identity #tracker initialized as a func (identity)
  while n > 0: #loop through n times
    g = compose1(func, g) #when n = 1, func(identity(x)), tracker is updated to func(identity(x))...
    n = n - 1
  return g

def compose1(func1, func2):
  def f(x):
    return func1(func2(x))
  return f

#Q2 
def num_eights(pos): #iterative version
  k = 0
  while pos > 0:
    if pos % 10 == 8:
      k = k + 1
    pos = pos // 10
  return k 
  
def num_eights(pos): #recursive version
  if pos % 10 == 8: #check if the last digit of pos is 8
    return 1 + num_eights(pos // 10)
  elif pos < 10: #base case, check if we have reached the end of pos.(6 // 10 --> 0)
    return 0
  else:
    return num_eights(pos // 10)

#Q3
def helper(total, i, direction): #helper function, i:count, direction: 1 or -1
  if i == n: #base case
    return total #no else
  if i % 8 == 0 or num_eights(i) > 0:
    return helper(total - direction, i + 1, direction * -1) #since direction becomces -1 in the next term
  # pingpong(14)-->2, pingpong(15)-->1, pingpong(16)-->2, pigpong(17)-->3
  return helper(total + direction, i + 1, direction)
return helper(1, 1, 1) #total, count and direction initialized to 1
   
#iterative version
def next_dir(direction, i): #not so sure
    if i % 8 == 0 or num_eights(i) > 0:
        return direction * -1
    return direction
  
def pingpong(n): 
  i = 1 # count/index
  ppv = 1
  direction = 1
  while i < n:
    direction = next_dir(direction, i)
    ppv += direction # direction == (1 or -1)
    i += 1 # count increment by 1
  return ppv

#Q4
def missing_digits(n):
  if n < 10:
    return 0 # base case, missing_digits(4) --> 0, no missing number
  last, rest = n % 10, n // 10
  return max(last - rest % 10 - 1, 0) + missing_digits(rest)
"""A tricky case for this problem was handling adjacent numbers that are the same(last - rest % 10 - 1 = -1
that's why we wrap the digit difference each recursive call with a max comparison call to 0.
"""
#solution 2, with herlper fucntion
def missing_digits_alt(n):
    def helper(n, digit):
        if n == 0:
            return 0  # base case, when the input number n < 10, n // 10 --> 0
        last, rest = n % 10, n // 10
        if last == digit or last + 1 == digit:
            return helper(rest, last)
        return 1 + helper(n, digit - 1) # if adjacent numbers are neither the same nor continuous, add 1 missing number 
    return helper(n // 10, n % 10) # diigt initialized to the last number of n
""" missing_digits_alt(4)
helper(0, 4) # 4 // 10 --> 0
return 0
"""

#Q5
""" Partitions 
The number of ways to partition n using integers up to m equals:
  the number of ways to partition n-m using integers up to m, and
  the number of ways to partition n using integers up to m-1.
To complete the implementation, we need to specify the following base cases:
  There is one way to partition 0: include no parts.
  There are 0 ways to partition a negative n.
  There are 0 ways to partition any n greater than 0 using parts of size 0 or less.

>>> def count_partitions(n, m): # how to count the ways to sum up to a final value with smaller parts
        """Count the ways to partition n using parts up to m."""
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 0
        else:
            return count_partitions(n-m, m) + count_partitions(n, m-1)
>>> count_partitions(6, 4)
9
>>> count_partitions(5, 5)
7
"""
def get_next_coin(coin): 
   if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
# >>> get_next_coin(2) # Other values return None
      
#takes a positive integer change and returns the number of ways to make change for change using coins
def count_coins(change): 
    def constrained_count(change, smallest_coin):
        if change == 0:
            return 1
        if change < 0:
            return 0
        if smallest_coin == None:
            return 0
        without_coin = constrained_count(change, get_next_coin(smallest_coin))
        with_coin = constrained_count(change - smallest_coin, smallest_coin)
        return without_coin + with_coin
    return constrained_count(change, 1)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
