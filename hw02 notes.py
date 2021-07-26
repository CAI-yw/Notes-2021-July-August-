#some notes about 21s 61a.
#hw02 TA notes, just for self-use.
#Q1, version 1: focus on how we maniipulate the numbers; version 2: treat functions as their own thing(use compose1)
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


