import numpy as np
arr2d = np.array([
    [1,2,3],
    [4,5,6]
])
# print(arr2d)
# print(arr2d.shape)
# Add new axis ---> 3D 
arr3d = arr2d[np.newaxis,:,:]
print(arr3d)
print(arr3d.shape)
new_layer  = np.array([[7,8,9],[10,11,12]])
# add new lay to the 3D arrays 
arr3d = np.vstack([arr3d,new_layer[np.newaxis,:,:]])
print(arr3d)
print(arr3d.shape)