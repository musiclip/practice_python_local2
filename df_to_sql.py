import pymysql
import pandas as pd
from sqlalchemy import create_engine

data=[{ 'id': 154, 'name': 'Chocolate Heaven' },
{ 'id': 155, 'name': 'Tasty Lemons' },
{ 'id': 156, 'name': 'Vanilla Dreams' }]

df = pd.DataFrame(data)

print(df)

engine = create_engine("mysql+pymysql://pmth"+"@localhost:3306/mydatabase?charset=utf8")

df.to_sql(name='products', con=engine, if_exists='append', index=False)

#engine = create_engine("mysql+pymysql://pmth"+"@localhost:3306/mydatabase?charset=utf8")

#df.to_sql(name='products', con=engine, if_exists='append', index=False)

data2 = [{ 'id': 1, 'name': 'John', 'fav': 154},
{ 'id': 2, 'name': 'Peter', 'fav': 154},
{ 'id': 3, 'name': 'Amy', 'fav': 155},
{ 'id': 4, 'name': 'Hannah', 'fav':0},
{ 'id': 5, 'name': 'Michael', 'fav':0}]

df2 = pd.DataFrame(data2)

df2.to_sql(name='users', con=engine, if_exists='append', index=False)
