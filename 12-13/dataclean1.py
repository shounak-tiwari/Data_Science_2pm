# Clean data using pandas

import pandas as pd

ref_variable = pd.read_csv(r'C:\Users\DELL\Desktop\Projects\Batches\Data Science - 11am\Data sets\Experience-Salary.csv')

print(ref_variable.head())

print(ref_variable.tail())

print(ref_variable.info())

ref_variable.dropna(inplace=True)

ref_variable.to_csv(
    r'C:\Users\DELL\Desktop\Projects\Batches\Data Science - 11am\Data sets\Experience-Salary.csv',
    index=False
)
print(ref_variable.info())

print(ref_variable)
# 1000 --- 990 ,10 
# 1000 ---  600 / 400 