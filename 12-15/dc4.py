import pandas as pd

df = pd.read_csv(r'C:\Users\DELL\Desktop\Projects\Batches\Data Science - 2pm\12-15\employee.csv')

print(df.dtypes)

df['salary'].fillna(df['salary'].mean(),inplace=True)

df['salary'] = df['salary'].astype(int)


df['dataofjoining'] = pd.to_datetime(df['dataofjoining'])
print(df.dtypes)


print(df['salary'].duplicated().sum())