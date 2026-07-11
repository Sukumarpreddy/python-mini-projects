"""import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_squared_error  

# Load dataset  
df = pd.read_csv('house_data.csv')  # Example CSV with columns: area, bedrooms, location, price  

# Convert categorical data  
df = pd.get_dummies(df, columns=['Location'], drop_first=True)

# Features & Target  
X = df.drop('Price', axis=1)  
y = df['Price']  

# Split data  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model  
model = LinearRegression()  
model.fit(X_train, y_train)

# Predict  
predictions = model.predict(X_test)  
print("MSE:", mean_squared_error(y_test, predictions))



"""

import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_squared_error  

# Load dataset  
df = pd.read_csv('house_data.csv')

# Clean column names (strip whitespace)
df.columns = df.columns.str.strip()

# Print actual column names to verify
print("Columns in dataset:", df.columns.tolist())

# Rename 'Price ($)' to 'Price'
df.rename(columns={'Price ($)': 'Price'}, inplace=True)

# Drop unnecessary columns
columns_to_drop = ['ID']
df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

# One-hot encode Location
if 'Location' in df.columns:
    df = pd.get_dummies(df, columns=['Location'], drop_first=True)
else:
    print("Warning: 'Location' column not found. Skipping one-hot encoding.")

# Check if 'Price' column now exists
if 'Price' not in df.columns:
    raise KeyError("The column 'Price' was not found in the dataset even after renaming.")

# Drop rows with missing values
df = df.dropna()

# Separate features and target
X = df.drop('Price', axis=1)  
y = df['Price']  

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()  
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error (MSE):", mse)

