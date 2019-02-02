import numpy as np

# Arrays
my_list = [1,2,3]
x = np.array(my_list)
type(x)

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
np.array(my_matrix)

list(range(0,5))
# Numpy version of the code
np.arange(0,5) # Array Range
np.arange(0,11,2) # Even numbers

np.zeros(3) # Array of zeros
np.zeros((3,5)) # 3x5 matrix of zeros
np.ones(3,3)
np.linspace(0,10,51) # Evenly spaced numbers (linearly spaced)

np.eye(4) # Identity matrix

np.random.rand(5,4) # np.random.XXXXXX check with tab+shift
np.random.randn(5,4) # Standard normal distribution
np.random.randint(1,100,10) # 10 random int between 1 and 100

arr = np.arrange(25)
ranarr = np.random.randint(0,50,10)
# Reshape method
arr.reshape(5,5)

arr.shape() # Shape attribute
arr.dtype # Data type

ranarr.max() # Max method
ranarr.argmax() # Index location of the max
ranarr.min()

# Numpy operations
arr =  np.arange(0,10)
arr + arr
arr * arr
arr ** 3
arr + 100
np.sqrt(arr)
np.exp(arr)
np.max(arr)
arr.max()
np.sin(arr)
np.log(arr)

# Numpy indexing
arr = np.arange(0,10)
arr[8]
arr[1:5]
arr[:5]
arr[3:]

arr[0:5] = 100 # Broadcasting
arr = np.arange(0,11)
slice_of_arr = arr[:]
slice_of_arr
arr
arr_copy = arr.copy # Copy (don't just point)

mat = np.array([5,10,15],[20,25,30],[35,40,45])
# Indexing an entire row
mat[2]
mat[1][1]
mat[1,1]

mat[:2,1:] # Grab everything from 0 to 2 from the first line and from 1 to the end from the second line

# Conditional selection
arr = np.arange(1,11)
arr > 4
bool_arr = arr > 4
arr[bool_arr]
# Equivalent :
arr[arr>4]

x = np.array([2,1,5,4,3])
np.sort(x)
