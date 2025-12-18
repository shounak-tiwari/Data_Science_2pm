import pandas as pd

df = pd.read_csv(r'C:\Users\DELL\Desktop\Projects\Batches\Data Science - 2pm\12-15\employee.csv')

# how to calculate or check duplicate values
# print(df.duplicated().sum())

df.drop_duplicates(inplace=True)
print(df)
print(df.duplicated())