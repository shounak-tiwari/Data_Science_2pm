import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.expanduser("/Users/kundanrathod1310/Documents/all_rec/Data_Science_2pm/12_18/student_result.csv")
df = pd.read_csv(path)

x = df['Hours']
y = df['Marks']
plt.plot(x , y)
plt.scatter(x , y)
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Result according to Hours of study")
plt.show()