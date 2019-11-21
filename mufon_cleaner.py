import pandas as pd
import datetime as dt

df = pd.read_csv('ENV/mufon.csv')

for i in df["Date_Submitted"]:
    if "b'" in df["Date_Submitted"]:
        dates = df["Date_Submitted"]
        dates = dates[2:-1]

print(df["Date_Submitted"].head())

df.to_csv("ENV/mufontest.csv")
