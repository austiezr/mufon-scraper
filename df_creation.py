import pandas as pd
import mufon_cleaner as cleaner

def df_create_and_merge():
    df = pd.read_csv('ENV/out.csv')
    df.rename(columns={"b'Date Submitted'" : 'Date_Submitted', "b'Date/Timeof Event'" : 'Date_Time', "b'Short Description'" : 'Short_Description', "b'Location of Event'" : 'Location'}, inplace=True)
    cleaner.drop_columns(df)
    cleaner.clean_csv(df)
    df.to_csv('ENV/clean_out.csv')
    df2 = pd.read_csv('ENV/mufon.csv')
    df3 = pd.concat([df, df2], sort=True)
    cleaner.drop_columns(df3)
    cleaner.clean_csv(df3)
    df3.sort_values(by=['Date_Submitted', 'Date_Time'], ascending=False, axis=0, inplace=True)
    df3.to_csv('ENV/mufon.csv')
