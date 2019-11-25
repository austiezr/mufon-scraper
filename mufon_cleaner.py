import pandas as pd
import datetime as dt

df = pd.read_csv('ENV/mufon.csv')

df['Date_Submitted'] = df['Date_Submitted'].str.replace("b'", '')
df['Date_Submitted'] = df['Date_Submitted'].str.replace("'", '')

df['Date_Time'] = df['Date_Time'].str.replace("b'", '')
df['Date_Time'] = df['Date_Time'].str.replace("'", '')

df.drop(df.columns.difference(['Date_Submitted','Date_Time','Location','Short_Description']), 1, inplace=True)

df.to_csv("ENV/mufon.csv")
