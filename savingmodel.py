import joblib
from sklearn.ensemble import RandomForestRegressor  
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('dataset.csv')
X = df[['Quantity', 'Discount', 'Profit']] 
y = df['Sales']          

X = X.fillna(0)
y = y.fillna(0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'sales_model.pkl')
print(f"R² Score on test set: {model.score(X_test, y_test):.3f}")