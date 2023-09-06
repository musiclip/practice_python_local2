import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data\\auto-mpg.csv', header = None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
def hp_float(df):
    df.horsepower.replace('?', np.nan, inplace = True)
    df.dropna(subset = ['horsepower'], axis = 0, inplace = True)
    df.horsepower = df.horsepower.astype('float') 
    return df.horsepower

def horsepower_bin(df):
    df.horsepower = hp_float(df)
    count, bin_dividers = np.histogram(df.horsepower, bins = 3)
    bin_names = ['저출력','보통출력','고출력']
    df['hp_bin'] = pd.cut(x = df['horsepower'], bins = bin_dividers,
                          labels = bin_names, include_lowest = True)
    return (df[['horsepower','hp_bin']].head(15))

df1 = df.copy()
result = horsepower_bin(df1)

horsepower_dummies = pd.get_dummies(df1['hp_bin'])

df2 = df.copy()

def horsepower_MinMax(df):
    df.horsepower = hp_float(df)
    df.horsepower = df.horsepower / abs(df.horsepower.max())
    return (df.horsepower.head(15))

result2 = horsepower_MinMax(df)