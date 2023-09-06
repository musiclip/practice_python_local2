import pandas as pd
import numpy as np

df = pd.read_csv('data\\stock-data.csv')

def newdate(df):
    df['new_Date'] = pd.to_datetime(df['Date'])
    df.set_index('new_Date', inplace = True)
    df.drop(['Date'], axis = 1, inplace = True)
    return df

df1 = df.copy()
result = newdate(df1)

def YMD(df):
    newdate(df)
    df = df.reset_index()
    df['Year'] = df.new_Date.dt.year
    df['Month'] = df.new_Date.dt.month
    df['Day'] = df.new_Date.dt.day
    return df

df2 = df.copy()
result2 = YMD(df2)