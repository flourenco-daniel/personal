import jpype
import asposecells
import os
import pandas as pd

def fix_sheets(sheet_names, output_folder):
    jpype.startJVM()
    from asposecells.api import Workbook
    os.makedirs("db_naturallis", exist_ok=True)

    for sheet_name in sheet_names:
        broken_sheet = sheet_name
        fixed_sheet = os.path.join("db_naturallis", f"{sheet_name.split('.')[0]}_fixed.xls")
        
        workbook = Workbook(broken_sheet)
        workbook.save(fixed_sheet)
    
    jpype.shutdownJVM()

sheet_names = [
    "pedidos_simples_2021.xls",
    "pedidos_simples_2022_1.xls",
    "pedidos_simples_2022_2.xls",
    "pedidos_simples_2022_3.xls",
    "pedidos_simples_2022_4.xls",
    "pedidos_simples_2022-5.xls",
    "pedidos_simples_2023_1.xls",
    "pedidos_simples_2023_2.xls",
    "pedidos_simples_2023_3.xls",
    "pedidos_simples_2023_4.xls",
    "pedidos_simples_2024-1.xls",
    "pedidos_simples_2024-2.xls",
    "pedidos_simples_2024-3.xls"
]

output_folder = "db_naturallis"

fix_sheets(sheet_names, output_folder)


def join_sheets(fixed_sheet_folder):
    all_data = pd.DataFrame() 

    for file_name in os.listdir(fixed_sheet_folder):
        if file_name.endswith('.xls'):
            file_path = os.path.join(fixed_sheet_folder, file_name)
            
            df = pd.read_excel(file_path, header=None if all_data.empty else 'infer')  # Skip header except for the first sheet
            
            all_data = pd.concat([all_data, df], ignore_index=True)

    return all_data

fixed_sheet_folder = "db_naturallis"

joined_data = join_sheets(fixed_sheet_folder)
final_table = joined_data.iloc[1:]
header = final_table.columns.tolist()
new_header = header[41:]
new_header.extend([''] * (len(header) - len(new_header)))
final_table.columns = new_header
final_table = final_table.iloc[:, :-41]
final_table.to_csv("table_ntl_pedido.csv", index=False)
new_df = pd.read_csv("table_ntl_pedido.csv")

print(new_df.head())