import pandas as pd

# read_csv 
data_csv = pd.read_csv(r'C:\Users\DELL\Desktop\Batches\Data Science - 2pm\12-08\CourseDetails.csv')
print(data_csv)

print(type(data_csv))

df = pd.DataFrame(data_csv)
print(df)
print(type(df))