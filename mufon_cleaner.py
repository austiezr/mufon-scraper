import pandas as pd

mufon = pd.read_csv('ENV/mufon.csv')


def clean_csv(df):
    df['Date_Submitted'] = df['Date_Submitted'].str.replace("b'", '')
    df['Date_Submitted'] = df['Date_Submitted'].str.replace("'", '')

    df['Date_Time'] = df['Date_Time'].str.replace("b'", '')
    df['Date_Time'] = df['Date_Time'].str.replace("'", '')

    df["Location"] = df["Location"].str.replace("b'", '')
    df["Location"] = df["Location"].str.replace("'", '')

    df["Short_Description"] = df["Short_Description"].str.replace("b'", '')
    df["Short_Description"] = df["Short_Description"].str.replace("'", '')
    df["Short_Description"] = df["Short_Description"].str.replace("{tjd} ", '')
    df["Short_Description"] = df["Short_Description"].str.replace("{rjl} ", '')
    df["Short_Description"] = df["Short_Description"].str.replace("{RJL} ", '')
    df["Short_Description"] = df["Short_Description"].str.replace("\[rjl} ", '')
    df["Short_Description"] = df["Short_Description"].str.replace("{cak} ", '')

    df.drop_duplicates(keep="last", inplace=True)


def drop_columns(df):
    df.drop(df.columns.difference(['Date_Submitted', 'Date_Time', 'Location', 'Short_Description']), 1, inplace=True)
