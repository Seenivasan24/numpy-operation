import numpy as np
arr1=np.array([[100,200,300,400,500],[600,700,800,900,100]])
arr2=np.array([[600,700,800,900,100],[100,200,300,400,500]])


print(arr1.shape)
print(arr2.shape)

print(arr1.size)
print(arr2.size)


print(arr1.ndim)
print(arr2.ndim)


print(type(arr1))
print(type(arr2))


print(arr1.dtype)
print(arr2.dtype)


print(np.zeros((2,3)))
print(np.zeros((2,3)))


print(np.zeros((2,3),dtype=int))
print(np.zeros((2,3),dtype=int))


print(np.ones((2,3)))
print(np.ones((2,3)))


print(np.ones((2,3),dtype=int))
print(np.ones((2,3),dtype=int))


print(np.full((2,3),10))
print(np.full((2,3),10))


print(np.empty((2,3)))
print(np.empty((2,3)))
