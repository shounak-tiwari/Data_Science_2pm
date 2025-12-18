import matplotlib.pyplot as plt
import pandas as pd

#Data of plotting 
df = pd.read_csv(r'C:\Users\DELL\Desktop\Projects\Batches\Data Science - 2pm\12-17\StudyResullt.csv')

x = df['Hours']
y = df['Marks']

plt.plot(x,y)
plt.xlabel('Hours')
plt.ylabel('Marks')
plt.title('Result according to marks')
plt.show()