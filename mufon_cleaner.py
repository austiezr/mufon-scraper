import pandas as pd
import numpy as np
import calendar
import datetime


def clean_csv(df):
    df['Date_Submitted'] = df['Date_Submitted'].str.replace("b'", '')
    df['Date_Submitted'] = df['Date_Submitted'].str.replace("'", '')
    # df['Date_Submitted'] = pd.to_datetime(df['Date_Submitted'], format='%Y-%m-%d')

    df['Date_Time'] = df['Date_Time'].str.replace("b'", '')
    df['Date_Time'] = df['Date_Time'].str.replace("'", '')
    # df['Date_Time'] = pd.to_datetime(df['Date_Time'], format='%Y-%m-%d%I%M%p', errors='ignore')
    # df['Date_Time'] = df['Date_Time'].replace('12:00AM', df['Date_Submitted'])

    df["Location"] = df["Location"].str.replace("b'", '')
    df["Location"] = df["Location"].str.replace("'", '')

    df["Short_Description"] = df["Short_Description"].str.replace("b'", '')
    df["Short_Description"] = df["Short_Description"].str.replace("'", '')
    df["Short_Description"] = df["Short_Description"].str.replace("{tjd} ", '')
    df["Short_Description"] = df["Short_Description"].str.replace("{rjl} ", '')
    df["Short_Description"] = df["Short_Description"].str.replace("{RJL} ", '')
    df["Short_Description"] = df["Short_Description"].str.replace("\\[rjl} ", '')
    df["Short_Description"] = df["Short_Description"].str.replace("{cak} ", '')

    df["Day_Submitted"] = pd.to_datetime(df['Date_Submitted'], format='%Y-%m-%d')
    df["Day_Submitted"] = df["Day_Submitted"].dt.day_name()

    df.drop_duplicates(keep="last", inplace=True)


def drop_columns(df):
    df.drop(df.columns.difference(['Date_Submitted', 'Day_Submitted', 'Date_Time', 'Location', 'Short_Description']), 1, inplace=True)
