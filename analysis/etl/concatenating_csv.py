import os
import pandas as pd

def concatenate_csv_files(folder_path, output_file):
    files = os.listdir(folder_path)
    csv_files = [f for f in files if f.endswith('.csv')]
    data_frames = []
    
    for csv_file in csv_files:
        try:
            file_path = os.path.join(folder_path, csv_file)
            df = pd.read_csv(file_path)
            data_frames.append(df)
            
            print(f"Read {csv_file}")
        except Exception as e:
            print(f"Failed to read {csv_file}: {e}")
    
    combined_df = pd.concat(data_frames, ignore_index=True)
    
    combined_df.to_csv(output_file, index=False)
    
    print(f"Combined {len(csv_files)} files into {output_file}")

if __name__ == '__main__':
    folder_path = 'C:\\Users\\danie\\Documents\\Python Scripts\\db_naturallis'  
    output_file = 'C:\\Users\\danie\\Documents\\Python Scripts\\db_naturallis\\combined_file.csv'  
    concatenate_csv_files(folder_path, output_file)
