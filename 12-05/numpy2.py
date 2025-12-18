import numpy as np
dia_matrix = np.array([
    [5,0,0],
    [0,6,0],
    [0,0,9]
])
daiginal  = np.diag(dia_matrix)
print(daiginal)