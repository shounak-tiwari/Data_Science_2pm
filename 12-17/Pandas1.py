import pandas as pd 

df = pd.DataFrame({
    "Name":['Akash','Arun','Kundan'],
    'Age':[25,30,28]
})

df.drop('Age',axis=1,inplace=True)
print(df)