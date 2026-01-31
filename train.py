import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

engine = create_engine("sqlite:///sales.db")
df = pd.read_sql("SELECT * FROM sales_data", con=engine)

X = df.drop('revenue', axis=1)
y = df['revenue']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Shapes:", X_train.shape, X_test.shape, y_train.shape, y_test.shape)

#Linear regression
model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))