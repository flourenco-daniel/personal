import jpype
import asposecells
import os
import pandas as pd

def fix_sheets (broken_sheet, path_fixed_sheet):
    jpype.startJVM()
    from asposecells.api import Workbook
    workbook = Workbook(broken_sheet)
    workbook.save(path_fixed_sheet)
    jpype.shutdownJVM()

path_fixed = "table_ntl_costumers.xlsx"
sheet_broken = "db_ntl_costumers.xls"

fix_sheets(sheet_broken, path_fixed)

df = pd.read_excel(path_fixed, sheet_name="Sheet1")
csv_file = "table_ntl_costumers.csv"
df.to_csv(csv_file, index=False)
df_columns = df.columns.tolist

print(df_columns)