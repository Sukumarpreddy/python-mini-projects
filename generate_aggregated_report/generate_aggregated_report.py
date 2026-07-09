import pandas as pd

df = pd.read_csv('cleaned_data.csv')

region_sales = df.groupby('Region')['Sales'].sum().reset_index()

product_avg = df.groupby('Product')['Sales'].mean().reset_index()

summary = df.groupby(['Region', 'Product'])['Sales'].sum().reset_index()

with pd.ExcelWriter('aggregated_report.xlsx',
engine='openpyxl') as writer:
    region_sales.to_excel(writer, index = False, sheet_name = 'By Region')
    product_avg.to_excel(writer, index=False, sheet_name='By Product')
    summary.to_excel(writer, index=False, sheet_name = 'Region_product')