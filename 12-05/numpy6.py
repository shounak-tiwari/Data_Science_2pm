import numpy as np
arr2d = np.array([
    [1,2,3],[4,5,6]
])



arr3d = arr2d[:,np.newaxis,:]
print(arr3d)