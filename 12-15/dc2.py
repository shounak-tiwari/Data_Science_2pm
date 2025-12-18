import pandas as pd

df = pd.read_csv(r'C:\Users\DELL\Desktop\Projects\Batches\Data Science - 2pm\12-15\employee.csv')

print(df)
df['salary'].fillna(df['salary'].mean(),inplace=True)

print(df)