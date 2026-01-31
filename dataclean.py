import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///sales.db")

df = pd.read_sql("SELECT * FROM sales_data", con=engine)

# Step 3: Clean the data

# 3a Check for missing values
print("Missing values before cleaning:\n", df.isnull().sum())

# 3b Fill missing numerical values with 0 (or mean)
df.fillna(0, inplace=True)

# 3c Make sure categorical columns are strings
if 'region' in df.columns:
    df['region'] = df['region'].astype(str)
if 'product' in df.columns:
    df['product'] = df['product'].astype(str)

# 3d: Optional – drop duplicates
df.drop_duplicates(inplace=True)

# 3e: Quick check
print("Data after cleaning:")
print(df.head())
print(df.info())

#  categorical columns to numbers 
df = pd.get_dummies(df, columns=['region', 'product'], drop_first=True)

print(df.head())

if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['month'] = df['Order Date'].dt.month
    df['year'] = df['Order Date'].dt.year

numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
df_model = df[numeric_cols].fillna(0)
