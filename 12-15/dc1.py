import pandas as pd 

df = pd.read_csv(r'C:\Users\DELL\Desktop\Projects\Batches\Data Science - 2pm\12-15\employee.csv')
print(df)
# option:1 
# Detect missing values 
print(df.isnull().sum()) 

# remove missing values 
df = df.dropna()

# print all values 
print(df)