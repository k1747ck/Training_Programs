import  numpy as np

from numpy import linalg as LA

a = np.array([1,2,3,4])

b = np.arange(1,10,2)

c = np.linspace(0,1,5)

# print(c)

arr = np.array([[1,2,3],[4,5,6]])

# print(arr.shape) # shape
# print(arr.ndim) #dimension
# print(arr.size) # size
# print(arr.dtype) #data type

reshaped = arr.reshape(3,2)

x = np.array([1,2,3])
y = np.array([4,5,6])

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(np.sqrt(x))
# print(np.exp(x))

data = np.array([[1,2,3],[4,5,6]])

# print(np.sum(data))
# print(np.mean(data))
# print(np.std(data))
# print(np.max(data))
# print(np.min(data))
# print(np.sum(data, axis=0))


A = np.array([[1,2,3],[4,5,6]])

# print(np.sum(A, axis=1))

X = np.array([[1,2,3],[4,5,6]])
Y = np.array([7,8,9])

# print (X+Y) # broadcasting - adding multidimentional array into single one


# linalg

M = np.array([[1,2],[3,4]])
# print ("Transpose : ", M.T)

rand_arr = np.random.rand(3,3)

rand_ints = np.random.randint(0,10,(2,3))

normal_dist = np.random.normal(0,1,5)

# print(rand_arr)
# print(rand_ints)
# print(normal_dist)

data_one = np.random.randint(0,255,(3,3))
# print(data_one)

normalized = data_one/255.0
# print(normalized)