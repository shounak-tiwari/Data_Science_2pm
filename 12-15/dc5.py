import pandas as pd

df = pd.read_csv(r'C:\Users\DELL\Desktop\Projects\Batches\Data Science - 2pm\12-15\employee.csv')

df['name'] = df['name'].str.strip()
df['name'] = df['name'].str.replace(r'\s+',' ',regex=True)

print(df)