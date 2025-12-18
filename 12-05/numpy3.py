# Expand a 1D array into a column vector.
# Scaler : working with one dimentions 
# Vector : working with at least 2D and have direction
import numpy as np
# vector (shape:(n,1))
arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(arr)
# column vector 
col_vec = arr.reshape(-1,1)
print(col_vec)
# Reshape : method of numpy it change the shape of (rowsXcolumns )
#  -1 : numpy to calculate the number of rows based on the daya 
# 1 means 1 column 
# arr = [1,2,3,4,5]
print(arr.reshape(-1,4))