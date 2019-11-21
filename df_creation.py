import pandas as pd

def df_create_and_merge():
    df = pd.read_csv('ENV/out.csv')
    df.drop("b'\\xc2\\xa0'", axis=1, inplace=True)
    df.drop("b'Long Description'", axis=1, inplace=True)
    df.drop("b'Attachments'", axis=1, inplace=True)
    df.rename(columns={"b'Date Submitted'" : 'Date_Submitted', "b'Date/Timeof Event'" : 'Date_Time', "b'Short Description'" : 'Short_Description', "b'Location of Event'" : 'Location'}, inplace=True)
    df.to_csv('ENV/clean_out.csv')
    df2 = pd.read_csv('ENV/mufon.csv')
    df3 = pd.concat([df, df2], sort=True)
    df3.drop(df3.columns.difference(['Date_Submitted','Date_Time','Location','Short_Description']), 1, inplace=True)
    df3.drop_duplicates(keep="last", inplace=True)
    df3.sort_values(by=['Date_Submitted', 'Date_Time'], ascending=False, axis=0, inplace=True)
    df3.to_csv('ENV/mufon.csv')