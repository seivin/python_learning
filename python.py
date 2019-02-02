# List
my_list = [1,2,3]
my_list.append(4)
print(my_list)
print(my_list[-1]) # Last element of a list
my_list[0:2] # 1st and 3rd elements
my_list[:2] # Everything from the beginning
my_list[2:] # Everything from the end

nested = [1,2['a','b']]
nested[2][0] # Display the 1st element of the 3rd element

# Dictionary (unordered)
d = {'key1':10,'key2':'seconditem'}
d['key2']

# Tuples (unchangable)
t = (1,2,3)
t[0]

# Set
{1,1,1,2,3,3,3,3,3}
set([1,2,3,3,3,3,3])

import math
# math. + Press "tab"
math.sqrt(10)

(1 == 1) and (1 <= 1)
(1 == 1) or (1 <= 1)
(1 == 1) and not (1 == 2)

if True:
  print('True')
elif (2 == 2)
  print ('Two')
else:
  print('If statement was not true.')

seq = [1,2,3,4,5]
for num in seq:
  print(num**2)

i = 1
while i < 5:
  print('i is currently {}'.format(i))
  i = i + 1

# range() 
for item in range(5):
  print(item)

range(5)
range(1,5) # begins at 1
range(0,20,2) # begins at 0, finishes at 20, step of 2
list(range(1,11)) # list of number from 1 to 10*

# List comprehension
x = [1,2,3,4]
out = []
for num in x:
  out.append(num**2)
print(out)
# Equivalent to the stuff just above
[num**2 for num in x]

def my_func(argument=5):
  """
  Docstring goes here
  """
  print(param)
  return argument*5
x = my_func(5)
print(x)

# Lambda expression (anonymous function)
def times_two(var):
  return var*2
result = times_two(4)
print(result)

lambda var: var*2

seq = [1,2,3,4,5]
list(map(times_two,seq)) # Takes the function "x2" and applies it to "seq"
list(map(lambda var: var*2,seq))

def is_even(num):
  return num%2 == 0
list(filter(is_even,seq))
list(filter(lambda num:num%2 == 0,seq))

tweet = "Go sports! #cool"
tweet.upper
tweet.lower
tweet.split() # Split on whitespace by default
tweet.split('#')[1] # Split at the 1st '#'

my_list = [1,2,3]
my_list.append(4)
my_list.pop() # Remove the last item
my_list.pop(0) # Remove the 1st item
1 in my_list # Return if 1 is in the list
'a' in [1,2,'a']
