import pandas

# variable_data  = pandas.read_csv(r'C:\Users\DELL\Desktop\Batches\Data Science - 2pm\12-08\CourseDetails.csv')
varriable_data = pandas.read_json(r'C:\Users\DELL\Desktop\Batches\Data Science - 2pm\12-08\CourseDetails.json')

print(varriable_data)
# dataframe of pandas 
print(type(varriable_data))