# Expand a 1D array into a row vector.
import numpy as np
OneD = np.array([1,2,3,4,5])
# print(OneD)
row_vec = OneD.reshape(1,-1)
print(row_vec)