import pandas as pd
from sqlalchemy import create_engine

import pandas as pd
from sqlalchemy import create_engine

def get_sales_data():
    df = pd.read_csv('dataset.csv')  
    engine = create_engine("sqlite:///sales.db", echo=True)
    df.to_sql("sales_data", con=engine, if_exists="replace", index=False)
    print("CSV data loaded into SQLite database successfully!")
    return df
