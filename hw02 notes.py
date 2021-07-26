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
  i = 1 #count/index
  ppv = 1
  direction = 1
  while i < n:
    direction = next_dir(direction, i)
    ppv += direction #direction == (1 or -1)
    i += 1 #count increment by 1
  return ppv

  
   
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
