import pandas as pd

df1 = pd.read_csv("Names.csv")
df2 = pd.read_csv("Names2.csv")

df1 = pd.concat([df1,df2])
df1.to_csv("PlayerNames.csv", index = False)