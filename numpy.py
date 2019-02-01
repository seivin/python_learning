import numpy as np

# Array of zeros (floats)
z = np.zeros(3)
type(a)
z.shape
z.shape = (10, 1)

z = np.ones(10)
z = np.empty(3)
z = np.array([10, 20])

a_list = [1,2,3,4,5,6]
z = np.array([a_list])

np.random.seed(0)
z1 = np.random.randint(10, size=6)
z1

# First element
z1[0]

# Range
z1[0:2]

# Last element
z1[-1]

print(np.sum(p))
# np.prod
# np.mean()
# np.std()
# np.var()
# np.min()
# np.max()
# np.argmin() index value of the min

x = np.array([2,1,5,4,3])
np.sort(x)