import pandas as pd

df1 = pd.read_csv("FullData.csv")
df2 = pd.read_csv("FullData(Edit2).csv")

df1 = pd.concat([df1,df2])
df1.to_csv("FullData.csv", index = False)