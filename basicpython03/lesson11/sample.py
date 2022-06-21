import numpy as np

# #1D array
# arr = np.array([1, 2, 3, 4, 5,6])
# print(arr)

# #2D array
# arr = np.array([[1, 2, 3, 4, 5,6],
#                 [1, 2, 3, 4, 5,6]],dtype= int)
# print(arr)

# #3D array
# arr = np.array(([(1, 2, 3, 4, 5,6),(1, 2, 3, 4, 5,6)],
#                 [(1, 2, 3, 4, 5,6),(1, 2, 3, 4, 5,6)],
#                 [(1, 2, 3, 4, 5,6),(1, 2, 3, 4, 5,6)]),dtype= int)
# print(arr)


# arr = np.zeros((3,4),dtype = int)
# print(arr)

# arr = np.ones((2,3,4),dtype = int)
# print(arr)

# arr = np.full((2,3),5)
# print(arr)

# arr = np.eye(4,dtype = int)
# print(arr)

arr = np.random.random((2,3))
print(arr)

print(arr.dtype) #kiểu dữ liệu
print(arr.shape) #kích thước ma trận
print(arr.size) #só lượng phần tử trong ma trận
print(arr.ndim) #số chiều của ma trận