import pandas as pd
pd.set_option('display.max_rows', None) 
pd.set_option('display.max_columns', None)  
import os
import re
from tqdm import tqdm


def combine_data(input_dir, output_dir, usecols = 'A:AW', header_row = 14, chunk_size = 50000):

    # Make sure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Initialize a list to store the dataframes
    dataframes = []

    # Initialize a counter for the total number of rows
    total_rows = 0

    # Collect all excel files
    excel_files = [f for f in os.listdir(input_dir) if f.endswith(('.xlsx', '.xls'))]

    # Loop through all files in the directory with progress bar
    for filename in tqdm(excel_files, desc="Processing files"):
        file_path = os.path.join(input_dir, filename)
        # Determine the appropriate engine
        if filename.endswith('.xlsx'):
            engine = 'openpyxl'
        elif filename.endswith('.xls'):
            engine = 'xlrd'  # Note: xlrd now only supports old .xls files
        else:
            continue  # Skip unknown file formats

        # Read each sheet in the Excel file
        try:
            xls = pd.ExcelFile(file_path, engine=engine)
        except ValueError as e:
            print(f"Error reading {filename}: {e}")
            continue

        for sheet_name in xls.sheet_names:
            # Reading specified columns and rows, setting rows 14 and 15 as headers
            df = pd.read_excel(file_path, sheet_name=sheet_name, header=[header_row], usecols=usecols, skipfooter=1, engine=engine)
            rows = df.shape[0]
            print(f"File: {filename}, Sheet: {sheet_name}, Rows: {rows}")
            total_rows += rows
            dataframes.append(df)

    # Print the total number of rows
    print(f"Total number of rows across all sheets and files: {total_rows}")

    # Concatenate all dataframes
    compiled_data = pd.concat(dataframes, ignore_index=True)

    # Split compiled data into chunks of 600,000 rows each and save as individual Excel files
    chunk_size = chunk_size
    chunks = [compiled_data.iloc[i:i + chunk_size] for i in range(0, compiled_data.shape[0], chunk_size)]

    # Save chunks with progress bar
    for i, chunk in enumerate(tqdm(chunks, desc="Saving chunks"), start=1):
        chunk_file = os.path.join(output_dir, f'chunk_{i}.xlsx')
        chunk.to_excel(chunk_file, index=False)
        print(f"Chunk {i} saved to {chunk_file}")

    print("All data has been processed and saved.")