import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///sales.db")

df = pd.read_sql("SELECT * FROM sales_data", con=engine)

print(df.head())
print(df.info())
print(df.describe())
