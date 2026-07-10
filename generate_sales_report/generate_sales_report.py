import pandas as pd 

df = pd.read_csv("sales_data.csv")

summary = df.groupby('Region')['Sales'].sum().reset_index()

with pd.ExcelWriter('sales_report.xlsx',engine = 'openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Raw Data')
    summary.to_excel(writer, index=False, sheet_name='Summary')