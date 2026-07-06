import pandas as pd

df = pd.read_csv('raw_data.csv')

df = df.drop_duplicates()

df['Sales'] = df['Sales'].fillna(0)

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df = df.dropna(subset=['Region', 'Product'])

df.to_csv('cleaned_data.csv', index=False)