# Dataframe in pandas 
import pandas as pd
data = {
    "Name" : ["Amit","Rahul","Neha","Suneha"],
    "Marks" : [98,99,97,96]
}
df = pd.DataFrame(data)
print(df)