import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None) 
pd.set_option('display.max_columns', None)  
import os
import re
from tqdm import tqdm

def load_open_claim_auto(directory, skip_rows=12, lhnv = None):
    # Regular expression to find a four-digit year in the file name
    pattern = re.compile(r'\b(\d{2})-(\d{4})\b')

    # List to keep track of the names of the DataFrames stored as globals
    global_df_names = []

    # Iterate through each file in the specified directory
    for file in sorted(os.listdir(directory)):
        if file.endswith('.xlsx') and not file.startswith('~$'):
            
            # Find the year in the file name
            match = pattern.search(file)
            if match:
                quarter = match.group(0)
                file_path = os.path.join(directory, file)
                try:
                    """ IMPORT DATA"""
                    print(f"\n\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n--------------------------------------------------------------------------\nImporting: {file}")
                    # Load and clean data specifying the engine
                    df = pd.read_excel(file_path, header=None, skiprows=skip_rows, engine='openpyxl')
                    df.drop(df.columns[-1], axis = 1, inplace = True)  # remove na col at the end

                    # Dynamically determine headers based on the first non-empty cell per column
                    headers = []
                    for col in df.columns:
                        if pd.notna(df.iloc[1, col]):
                            headers.append(df.iloc[1, col])
                        elif pd.notna(df.iloc[0, col]) and pd.isna(df.iloc[1, col]):
                            headers.append(df.iloc[0, col])
                        else:
                            print(f'No headers found for {col}')

                    # Set the determined headers as column names
                    df.columns = headers
                    df = df.drop([0, 1])
                    df.reset_index(drop = True, inplace=True)
                    print(f'   Rows = {df.shape[0]}')
                    # print(f'Columns = {df.shape[1]}')
                    
                    if df.empty:
                        print(f"{quarter} data is empty.")
                    elif df.shape[0] == 0:
                        print(f"{quarter} data is empty.")
                    else:
                        
                        """ RENAME COLUMNS"""
                        print("--------------------------------------------------------------------------\nRenaming Columns:")
                        df_clm_dict = {
                            'Tình trạng hiện tại': 'SO_HSBT', 
                            'Ngày mở HSBT': 'NGAY_MO_HSBT',
                            'Ngày thông báo': 'NGAY_THONG_BAO',
                            'Ngày xảy ra': 'NGAY_XAY_RA',
                            'Phòng': 'PHONG_BT',
                            'Cán bộ bồi thường': 'CAN_BO_BT',
                            'Nghiệp vụ': 'MA_LHNV',
                            'Số hợp đồng': 'SO_HD',
                            'Mã khai thác': 'MA_KT',
                            'Mã khách hàng': 'MA_KH',
                            'Tên khách hàng': 'TEN_KH',
                            'Đối tượng bảo hiểm': 'TEN_DTBH',
                            'Ngày cấp': 'NGAY_CAP',
                            'Ngày HL': 'NGAY_HL',
                            'Ngày KT': 'NGAY_KT',
                            'Nhóm': 'NHOM_XE', 
                            'Nguyên nhân': 'NGUYEN_NHAN_BT',
                            'Số tiền tổn thất': 'STTT',
                            'Số tiền bồi thường': 'STBT',
                            'Tình trạng hiện tại': 'TINH_TRANG'
                        }

                        df.rename(columns={col: df_clm_dict[col] for col in df.columns if col in df_clm_dict}, inplace=True)

                                
                        """ REMOVE UNNECESSARY COLUMNS"""
                        print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
                        removed_cols = [
                            'STT',
                            'Cán bộ cấp đơn',
                            'Thu hồi bồi thường',
                            'Phí giám định',
                            'Kiểu ĐBH', 
                            'Tỷ lệ ĐBH', 
                            'Thu đòi đồng BH', 
                            'Tỷ lệ tái CĐ', 
                            'Thu đòi tái bảo hiểm CĐ', 
                            'Tỷ lệ tái TT', 
                            'Thu đòi tái bảo hiểm TT'
                        ]

                        # Removing columns, check if the columns exist
                        for col in removed_cols:
                            if col in df.columns:
                                df.drop(columns=col, inplace=True)
                            else:
                                print(f"   Column {col} not found in DataFrame.")                       


                        """ ADD COLUMN FOR VALUATION QUARTER"""
                        print("--------------------------------------------------------------------------\nAdding Column VALU_QUARTER:")
                        df['VALU_QUARTER'] = quarter


                        """ FILTER FOR LHNV"""
                        if lhnv:
                            print("--------------------------------------------------------------------------\nFiltering for LHNV:")    
                            rows_b4 = df.shape[0]    
                            df = df[df['MA_LHNV'] == lhnv]
                        
                        
                        """ CONVERT DATE COLUMNS"""           
                        print("--------------------------------------------------------------------------\nReformatting Date Cols:")
                        dates_columns = [
                            "NGAY_MO_HSBT",
                            "NGAY_THONG_BAO",
                            "NGAY_XAY_RA",
                            "NGAY_CAP",
                            "NGAY_HL",
                            "NGAY_KT"
                        ]

                        for dates_col in dates_columns:
                            if dates_col in df.columns:  # Ensure column exists before converting
                                original_na_count = df[dates_col].isna().sum()
                                df[dates_col] = pd.to_datetime(df[dates_col], errors='coerce', dayfirst=True)
                                new_na_count = df[dates_col].isna().sum()
                                detected_errors = new_na_count - original_na_count
                                if detected_errors > 0:
                                    print(f"   Detected {detected_errors} Incorrect Dates in {dates_col}")
                            else:
                                print(f"   Column {dates_col} not found in DataFrame.")


                        """ CONVERT NUMERICAL COLUMNS"""
                        print("--------------------------------------------------------------------------\nReformatting Num Cols:")
                        num_columns = [
                            'STTT',
                            'STBT'
                        ]
                        
                        for num_col in num_columns:
                            if num_col in df.columns:  # Ensure column exists before converting
                                original_na_count = df[num_col].isna().sum()
                                df[num_col] = pd.to_numeric(df[num_col], errors='coerce')
                                new_na_count = df[num_col].isna().sum()
                                detected_errors = new_na_count - original_na_count
                                if detected_errors > 0:
                                    print(f"   Detected {detected_errors} Incorrect Values in {num_col}")
                            else:
                                print(f"   Column {num_col} not found in DataFrame.")
                        
                            
                        
                        """ REMOVE ROWs WITH MISSING EFF DATE """
                        print("--------------------------------------------------------------------------\nRemoving Rows Missing NGAY_HL:")    
                        rows_b4 = df.shape[0]    
                        df = df[df['NGAY_HL'].notna()]
                        print(f'   Removed: {(rows_b4 - df.shape[0]):,.0f} Rows, ({((rows_b4 - df.shape[0])/rows_b4*100):.2f}%)')
                            
                            
                        
                        """ SAVE DF TO GLOBAL VARIABLE"""
                        print("--------------------------------------------------------------------------\nSaving DF:")
                        # Assign DataFrame to a global variable dynamically using the year
                        df_name = f'df_clm_{quarter}'
                        globals()[df_name] = df
                        global_df_names.append(df_name)
                        print(f"Summary of CY{quarter}:\n   -NUM CLAIMS = {df.shape[0]:,.0f}\n   -TOTAL CLAIMS = {df['STBT'].sum():,.0f}")
                        print('--------------------------------------------------------------------------\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                        
                except Exception as e:
                    print(f"Failed to process {file}: {e}")
            else:
                print(f"No year found in the file name {file}")

    # Print all global DataFrame names created
    print("\n\n\n==========================================================================\n==========================================================================\nSuccessfully Imported:", ", ".join(global_df_names))
    
    """ CONCAT INTO ONE DF"""
    all_dataframes = [globals()[name] for name in global_df_names if name in globals()]
    df_clm_open = pd.concat(all_dataframes, ignore_index=True)
    print(f"   Total Rows = {df_clm_open.shape[0]:,.0f}\n   Total Claims = {df_clm_open['STBT'].sum():,.0f}")
    
    print("==========================================================================\n==========================================================================")
    for name in global_df_names:
        del globals()[name]
        
    global_df_names.clear()
    
    return df_clm_open

def load_open_claim_marine(directory, skip_rows=12, lhnv = None):
    # Regular expression to find a four-digit year in the file name
    pattern = re.compile(r'\b(\d{2})-(\d{4})\b')

    # List to keep track of the names of the DataFrames stored as globals
    global_df_names = []

    # Iterate through each file in the specified directory
    for file in sorted(os.listdir(directory)):
        if file.endswith('.xlsx') and not file.startswith('~$'):
            
            # Find the year in the file name
            match = pattern.search(file)
            if match:
                quarter = match.group(0)
                file_path = os.path.join(directory, file)
                try:
                    """ IMPORT DATA"""
                    print(f"\n\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n--------------------------------------------------------------------------\nImporting: {file}")
                    # Load and clean data specifying the engine
                    df = pd.read_excel(file_path, header=None, skiprows=skip_rows, engine='openpyxl')
                    df.drop(df.columns[-1], axis = 1, inplace = True)  # remove na col at the end

                    # Dynamically determine headers based on the first non-empty cell per column
                    headers = []
                    for col in df.columns:
                        if pd.notna(df.iloc[1, col]):
                            headers.append(df.iloc[1, col])
                        elif pd.notna(df.iloc[0, col]) and pd.isna(df.iloc[1, col]):
                            headers.append(df.iloc[0, col])
                        else:
                            print(f'No headers found for {col}')

                    # Set the determined headers as column names
                    df.columns = headers
                    df = df.drop([0, 1])
                    df.reset_index(drop = True, inplace=True)
                    print(f'   Rows = {df.shape[0]}')
                    # print(f'Columns = {df.shape[1]}')
                    
                    if df.empty:
                        print(f"{quarter} data is empty.")
                    elif df.shape[0] == 0:
                        print(f"{quarter} data is empty.")
                    else:
                        
                        """ RENAME COLUMNS"""
                        print("--------------------------------------------------------------------------\nRenaming Columns:")
                        df_clm_dict = {
                            'Mã đơn vị quản lý': 'MA_DVI_QL',
                            'Mã đơn vị giải quyết': 'MA_DVI_GQ',
                            'Số hồ sơ': 'SO_HSBT', 
                            'Ngày mở HSBT': 'NGAY_MO_HSBT',
                            'Ngày thông báo': 'NGAY_THONG_BAO',
                            'Số ngày tồn': 'SO_NGAY_TON',
                            'Ngày xảy ra': 'NGAY_XAY_RA',
                            'Phòng': 'PHONG_BT',
                            'Cán bộ bồi thường': 'CAN_BO_BT',
                            'Nghiệp vụ': 'MA_LHNV',
                            'Số hợp đồng': 'SO_HD',
                            'Mã khách hàng': 'MA_KH',
                            'Tên khách hàng': 'TEN_KH',
                            'Đối tượng bảo hiểm': 'LOAI_HH',
                            'Ngày cấp': 'NGAY_CAP',
                            'Ngày HL': 'NGAY_HL',
                            'Ngày KT': 'NGAY_KT',
                            'Mã NT': 'MA_NGUYEN_TE', 
                            'Số tiền bảo hiểm': 'STBH', 
                            'Phí bảo hiểm VNĐ': 'PHI_BH', 
                            'Nguyên nhân': 'NGUYEN_NHAN_BT',
                            'Số tiền tổn thất': 'STTT',
                            'Số tiền bồi thường': 'STBT'
                        }

                        df.rename(columns={col: df_clm_dict[col] for col in df.columns if col in df_clm_dict}, inplace=True)

                                
                        """ REMOVE UNNECESSARY COLUMNS"""
                        print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
                        removed_cols = [
                            'STT',
                            'Số CV KN',
                            'Tình trạng hiện tại',
                            'Danh mục cơ sở',
                            'Cán bộ cấp đơn',
                            'Số GCN',
                            'Biển xe',
                            'Số khung/Số máy',
                            'Nhóm',
                            'Loại xe',
                            'Thu hồi bồi thường',
                            'Phí giám định',
                            'Kiểu ĐBH', 
                            'Tỷ lệ ĐBH', 
                            'Thu đòi đồng BH', 
                            'Tỷ lệ tái CĐ', 
                            'Thu đòi tái bảo hiểm CĐ', 
                            'Tỷ lệ tái TT', 
                            'Thu đòi tái bảo hiểm TT'
                        ]

                        # Removing columns, check if the columns exist
                        for col in removed_cols:
                            if col in df.columns:
                                df.drop(columns=col, inplace=True)
                            else:
                                print(f"   Column {col} not found in DataFrame.")                       


                        """ ADD COLUMN FOR VALUATION QUARTER"""
                        print("--------------------------------------------------------------------------\nAdding Column VALU_QUARTER:")
                        df['VALU_QUARTER'] = quarter


                        """ FILTER FOR LHNV"""
                        if lhnv:
                            print("--------------------------------------------------------------------------\nFiltering for LHNV:")    
                            rows_b4 = df.shape[0]    
                            df = df[df['MA_LHNV'] == lhnv]
                        
                        
                        """ CONVERT DATE COLUMNS"""           
                        print("--------------------------------------------------------------------------\nReformatting Date Cols:")
                        dates_columns = [
                            "NGAY_MO_HSBT",
                            "NGAY_THONG_BAO",
                            "NGAY_XAY_RA",
                            "NGAY_CAP",
                            "NGAY_HL",
                            "NGAY_KT"
                        ]

                        for dates_col in dates_columns:
                            if dates_col in df.columns:  # Ensure column exists before converting
                                original_na_count = df[dates_col].isna().sum()
                                df[dates_col] = pd.to_datetime(df[dates_col], errors='coerce', dayfirst=True)
                                new_na_count = df[dates_col].isna().sum()
                                detected_errors = new_na_count - original_na_count
                                if detected_errors > 0:
                                    print(f"   Detected {detected_errors} Incorrect Dates in {dates_col}")
                            else:
                                print(f"   Column {dates_col} not found in DataFrame.")


                        """ CONVERT NUMERICAL COLUMNS"""
                        print("--------------------------------------------------------------------------\nReformatting Num Cols:")
                        num_columns = [
                            'STTT',
                            'STBT'
                        ]
                        
                        for num_col in num_columns:
                            if num_col in df.columns:  # Ensure column exists before converting
                                original_na_count = df[num_col].isna().sum()
                                df[num_col] = pd.to_numeric(df[num_col], errors='coerce')
                                new_na_count = df[num_col].isna().sum()
                                detected_errors = new_na_count - original_na_count
                                if detected_errors > 0:
                                    print(f"   Detected {detected_errors} Incorrect Values in {num_col}")
                            else:
                                print(f"   Column {num_col} not found in DataFrame.")
                        
                            
                        
                        """ SAVE DF TO GLOBAL VARIABLE"""
                        print("--------------------------------------------------------------------------\nSaving DF:")
                        # Assign DataFrame to a global variable dynamically using the year
                        df_name = f'df_clm_{quarter}'
                        globals()[df_name] = df
                        global_df_names.append(df_name)
                        print(f"Summary of CY{quarter}:\n   -NUM CLAIMS = {df.shape[0]:,.0f}\n   -TOTAL CLAIMS = {df['STBT'].sum():,.0f}")
                        print('--------------------------------------------------------------------------\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                        
                except Exception as e:
                    print(f"Failed to process {file}: {e}")
            else:
                print(f"No year found in the file name {file}")

    # Print all global DataFrame names created
    print("\n\n\n==========================================================================\n==========================================================================\nSuccessfully Imported:", ", ".join(global_df_names))
    
    """ CONCAT INTO ONE DF"""
    all_dataframes = [globals()[name] for name in global_df_names if name in globals()]
    df_clm_open = pd.concat(all_dataframes, ignore_index=True)
    print(f"   Total Rows = {df_clm_open.shape[0]:,.0f}\n   Total Claims = {df_clm_open['STBT'].sum():,.0f}")
    
    print("==========================================================================\n==========================================================================")
    for name in global_df_names:
        del globals()[name]
        
    global_df_names.clear()
    
    return df_clm_open






def load_open_claim_auto_old(directory, skip_rows=12, lhnv = None):
    # Regular expression to find a four-digit year in the file name
    pattern = re.compile(r'\b(\d{2})-(\d{4})\b')

    # List to keep track of the names of the DataFrames stored as globals
    global_df_names = []

    # Iterate through each file in the specified directory
    for file in sorted(os.listdir(directory)):
        if file.endswith('.xlsx') and not file.startswith('~$'):
            
            # Find the year in the file name
            match = pattern.search(file)
            if match:
                quarter = match.group(0)
                file_path = os.path.join(directory, file)
                try:
                    """ IMPORT DATA"""
                    print(f"\n\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n--------------------------------------------------------------------------\nImporting: {file}")
                    # Load and clean data specifying the engine
                    df = pd.read_excel(file_path, header=None, skiprows=skip_rows, engine='openpyxl')
                    df.drop(df.columns[-1], axis = 1, inplace = True)  # remove na col at the end

                    # Dynamically determine headers based on the first non-empty cell per column
                    headers = []
                    for col in df.columns:
                        if pd.notna(df.iloc[1, col]):
                            headers.append(df.iloc[1, col])
                        elif pd.notna(df.iloc[0, col]) and pd.isna(df.iloc[1, col]):
                            headers.append(df.iloc[0, col])
                        else:
                            print(f'No headers found for {col}')

                    # Set the determined headers as column names
                    df.columns = headers
                    df = df.drop([0, 1])
                    df.reset_index(drop = True, inplace=True)
                    print(f'   Rows = {df.shape[0]}')
                    # print(f'Columns = {df.shape[1]}')
                    
                    if df.empty:
                        print(f"{quarter} data is empty.")
                    elif df.shape[0] == 0:
                        print(f"{quarter} data is empty.")
                    else:
                        
                        """ RENAME COLUMNS"""
                        print("--------------------------------------------------------------------------\nRenaming Columns:")
                        df_clm_dict = {
                          #  'Tình trạng hiện tại': 'SO_HSBT', 
                            'Ngày mở HSBT': 'NGAY_MO_HSBT',
                            'Ngày thông báo': 'NGAY_THONG_BAO',
                            'Ngày xảy ra': 'NGAY_XAY_RA',
                            'Phòng': 'PHONG_BT',
                            'Cán bộ bồi thường': 'CAN_BO_BT',
                            'Nghiệp vụ': 'MA_LHNV',
                            'Số hợp đồng': 'SO_HD',
                            'Mã khai thác': 'MA_KT',
                            'Mã khách hàng': 'MA_KH',
                            'Tên khách hàng': 'TEN_KH',
                            'Đối tượng bảo hiểm': 'TEN_DTBH',
                            'Ngày cấp': 'NGAY_CAP',
                            'Ngày HL': 'NGAY_HL',
                            'Ngày KT': 'NGAY_KT',
                            'Nhóm': 'NHOM_XE', 
                            'Nguyên nhân': 'NGUYEN_NHAN_BT',
                            'Số tiền tổn thất': 'STTT',
                            'Số tiền bồi thường': 'STBT',
                           # 'Tình trạng hiện tại': 'TINH_TRANG'
                        }

                        df.rename(columns={col: df_clm_dict[col] for col in df.columns if col in df_clm_dict}, inplace=True)

                                
                        """ REMOVE UNNECESSARY COLUMNS"""
                        print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
                        removed_cols = [
                            'STT',
                            'Cán bộ cấp đơn',
                            'Thu hồi bồi thường',
                            'Phí giám định',
                            'Kiểu ĐBH', 
                            'Tỷ lệ ĐBH', 
                            'Thu đòi đồng BH', 
                            'Tỷ lệ tái CĐ', 
                            'Thu đòi tái bảo hiểm CĐ', 
                            'Tỷ lệ tái TT', 
                            'Thu đòi tái bảo hiểm TT'
                        ]

                        # Removing columns, check if the columns exist
                        for col in removed_cols:
                            if col in df.columns:
                                df.drop(columns=col, inplace=True)
                            else:
                                print(f"   Column {col} not found in DataFrame.")                       


                        """ ADD COLUMN FOR VALUATION QUARTER"""
                        print("--------------------------------------------------------------------------\nAdding Column VALU_QUARTER:")
                        df['VALU_QUARTER'] = quarter


                        """ FILTER FOR LHNV"""
                        if lhnv:
                            print("--------------------------------------------------------------------------\nFiltering for LHNV:")    
                            rows_b4 = df.shape[0]    
                            df = df[df['MA_LHNV'] == lhnv]
                        
                        
                        """ CONVERT DATE COLUMNS"""           
                        print("--------------------------------------------------------------------------\nReformatting Date Cols:")
                        dates_columns = [
                            "NGAY_MO_HSBT",
                            "NGAY_THONG_BAO",
                            "NGAY_XAY_RA",
                            "NGAY_CAP",
                            "NGAY_HL",
                            "NGAY_KT"
                        ]

                        for dates_col in dates_columns:
                            if dates_col in df.columns:  # Ensure column exists before converting
                                original_na_count = df[dates_col].isna().sum()
                                df[dates_col] = pd.to_datetime(df[dates_col], errors='coerce', dayfirst=True)
                                new_na_count = df[dates_col].isna().sum()
                                detected_errors = new_na_count - original_na_count
                                if detected_errors > 0:
                                    print(f"   Detected {detected_errors} Incorrect Dates in {dates_col}")
                            else:
                                print(f"   Column {dates_col} not found in DataFrame.")


                        """ CONVERT NUMERICAL COLUMNS"""
                        print("--------------------------------------------------------------------------\nReformatting Num Cols:")
                        num_columns = [
                            'STTT',
                            'STBT'
                        ]
                        
                        for num_col in num_columns:
                            if num_col in df.columns:  # Ensure column exists before converting
                                original_na_count = df[num_col].isna().sum()
                                df[num_col] = pd.to_numeric(df[num_col], errors='coerce')
                                new_na_count = df[num_col].isna().sum()
                                detected_errors = new_na_count - original_na_count
                                if detected_errors > 0:
                                    print(f"   Detected {detected_errors} Incorrect Values in {num_col}")
                            else:
                                print(f"   Column {num_col} not found in DataFrame.")
                        
                            
                        
                        """ REMOVE ROWs WITH MISSING EFF DATE """
                        print("--------------------------------------------------------------------------\nRemoving Rows Missing NGAY_HL:")    
                        rows_b4 = df.shape[0]    
                        df = df[df['NGAY_HL'].notna()]
                        print(f'   Removed: {(rows_b4 - df.shape[0]):,.0f} Rows, ({((rows_b4 - df.shape[0])/rows_b4*100):.2f}%)')
                            
                            
                        
                        """ SAVE DF TO GLOBAL VARIABLE"""
                        print("--------------------------------------------------------------------------\nSaving DF:")
                        # Assign DataFrame to a global variable dynamically using the year
                        df_name = f'df_clm_{quarter}'
                        globals()[df_name] = df
                        global_df_names.append(df_name)
                        print(f"Summary of CY{quarter}:\n   -NUM CLAIMS = {df.shape[0]:,.0f}\n   -TOTAL CLAIMS = {df['STBT'].sum():,.0f}")
                        print('--------------------------------------------------------------------------\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                        
                except Exception as e:
                    print(f"Failed to process {file}: {e}")
            else:
                print(f"No year found in the file name {file}")

    # Print all global DataFrame names created
    print("\n\n\n==========================================================================\n==========================================================================\nSuccessfully Imported:", ", ".join(global_df_names))
    
    """ CONCAT INTO ONE DF"""
    all_dataframes = [globals()[name] for name in global_df_names if name in globals()]
    df_clm_open = pd.concat(all_dataframes, ignore_index=True)
    print(f"   Total Rows = {df_clm_open.shape[0]:,.0f}\n   Total Claims = {df_clm_open['STBT'].sum():,.0f}")
    
    print("==========================================================================\n==========================================================================")
    for name in global_df_names:
        del globals()[name]
        
    global_df_names.clear()
    
    return df_clm_open