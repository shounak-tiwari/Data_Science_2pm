# Reading Data using pandas 
# read_excel
# read_csv
# read_sql
# ..........
import pandas as pd 

# read the csv 
data = pd.read_csv('C:\\Users\\DELL\\Desktop\\Batches\\Data Science - 2pm\\12-06\\student.csv')

# data into dataframe 
data = pd.DataFrame(data)

print(data)
