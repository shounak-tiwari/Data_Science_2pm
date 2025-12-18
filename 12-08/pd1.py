import pandas as pd
# read_csv : methods (it is use for read data of csv file ),in read_csv we pass path of file in parameters 
data_csv = pd.read_csv('C:\\Users\\DELL\\Desktop\\Batches\\Data Science - 2pm\\12-08\\CourseDetails.csv')

df= pd.DataFrame(data_csv)
# print(df.iloc[0,1])
print(data_csv.iloc[0,1])