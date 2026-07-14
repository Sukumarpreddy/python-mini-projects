import pandas  as pd

csv_data = pd.read_csv("data.csv")
print("CSVData:" )
print(csv_data)

csv_data.to_excel("data_output.xlsx",index=False)

excel_data = pd.read_excel("data_output.xlsx")
print("\n Excel Data")
print(excel_data)

