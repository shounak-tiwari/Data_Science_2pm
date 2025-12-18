# Add a new axis to make a 3D array from a 2D array.

import numpy as np 

arr2d = np.array([
    [1,2,3],[4,5,6]
])
print(arr2d.ndim)
print(arr2d.size)
print(arr2d.shape)

arr3d = arr2d[np.newaxis,:,:]
print(arr3d)