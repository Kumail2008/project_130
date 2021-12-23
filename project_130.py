import csv
import pandas as pd

df = pd.read_csv("total_stars.csv")

print(df.shape)

del df["Luminosity"]
del df["Star_name1"]
del df["Distance1"]
del df["Mass1"]
del df["Radius1"]
del df["1"]
del df["2"]



print(df.shape)


print(list(df))

df.to_csv("project_130.csv")
