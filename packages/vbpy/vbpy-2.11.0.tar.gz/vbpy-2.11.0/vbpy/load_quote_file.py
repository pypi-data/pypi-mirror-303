import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None) 
pd.set_option('display.max_columns', None)  

import os
import re
from tqdm import tqdm


def load_quote_marine(directory, skip_rows=4, lhnv = None, dup_year = False, diagnostics = True):
    # Regular expression to find a four-digit year in the file name
    year_pattern = re.compile(r'\b(\d{4})\b')

    # List to keep track of the names of the DataFrames stored as globals
    global_df_names = []

    # Iterate through each file in the specified directory
    starting_file = True
    for file in sorted(os.listdir(directory)):
        if file.endswith('.xlsx') and not file.startswith('~$'):
            
            # Find the year in the file name
            match = year_pattern.search(file)
            if match:
                year = match.group(1)
                file_path = os.path.join(directory, file)
                try:
                    """ IMPORT DATA"""
                    if diagnostics:
                        if starting_file:
                            print(f"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n--------------------------------------------------------------------------\nImporting: {file}")
                            starting_file = False 
                        else:
                            print(f"\n\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n--------------------------------------------------------------------------\nImporting: {file}")
                    # Load and clean data specifying the engine
                    df = pd.read_excel(file_path, header=None, skiprows=skip_rows, engine='openpyxl')
                    df.drop(df.columns[-1], axis = 1, inplace = True)  # remove na col at the end
                    
                    df.iloc[0,17] = 'Phương tiện vận chuyển TRUE'
                    
                    # Dynamically determine headers based on the first non-empty cell per column
                    headers = []
                    for col in df.columns:
                        if pd.notna(df.iloc[1, col]):
                            headers.append(df.iloc[1, col])
                        elif pd.notna(df.iloc[0, col]) and pd.isna(df.iloc[1, col]):
                            headers.append(df.iloc[0, col])
                        elif diagnostics:
                            print(f'No headers found for {col}')

                    # Set the determined headers as column names
                    df.columns = headers
                    df = df.drop([0, 1])
                    df.reset_index(drop = True, inplace=True)
                    if diagnostics:
                        print(f'   Rows = {df.shape[0]}')
                    # print(f'Columns = {df.shape[1]}')
            
            
                    """ RENAME COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRenaming Columns:")
                    
                    df_quo_dict = {
                        'Đơn vị': 'MA_DVI_QL',
                        'Kiểu HĐ': 'KIEU_HD',
                        'Số GCN': 'SO_GCN',
                        'SĐBS': 'SDBS',
                        'Ngày cấp': 'NGAY_CAP',
                        'Quy tắc áp dụng': 'QUY_TAC_AP_DUNG',
                        'Điều kiện quy đổi': 'DIEU_KIEN_QUY_DOI',
                        'Người  được  BH': 'NGUOI_DUOC_BH',
                        'MST':'MST',
                        'Nhóm' : 'MA_LHNV',
                        'Nhóm hàng' : 'NHOM HANG',
                        'Phương  tiện  vận  chuyển TRUE' : 'PHUONG_TIEN_VC',
                        'Hàng hóa  được BH' : 'HH_DUOC_BH',
                        'Số lượng/Trọng lượng' : 'TRONG_LUONG',
                        'Phương thức đóng gói' : 'PHUONG_THUC_DONG GOI',
                        'Ngày  khởi hành': 'NGAY_KHOI_HANH',
                        'Ngày hiệu lực' : 'NGAY_HL',
                        'Ngày kết thúc' : 'NGAY_KT',
                        'Từ' : 'FROM',
                        'Chuyển  tải': 'CHUYEN_TAI',
                        'Đến' : 'TO',
                        'Nguyên tệ': 'NGUYEN_TE',
                        'Số tiền': 'STBH',
                        'Quy đổi VNĐ' : 'QUY_DOI_VND',
                        'Nguyên tệ': 'NGUYEN_TE',
                        'Tỷ lệ phí  chính' : 'TY_LE_PHI_CHINH',
                        'Phí chính': 'PHI_BH',
                        'Tỷ lệ phụ phí' : 'TY_LE_PHU_PHI',
                        'Phụ  phí' : 'PHU PHI',
                        'Tổng phí': 'TONG_PHI',
                        'Phí Quy đổi': 'PHI_QUY_DOI',
                        'Ngày nộp phí': 'NGAY_NOP_PHI',
                        'Kiểu đồng BH' : 'KIEU_DBH',
                        'Tỷ lệ VBI' : 'TY_LE_VBI',
                        'Treaty': 'TREATY',
                        'Fax':'FAX',
                        'Cán bộ quản lý': 'CAN_BO_QUAN_LY',
                        'Đại lý khai thác': 'DAI_LY_KT',
                        'Nguồn khai thác': 'NGUON_KT',
                        'Nhóm khách hàng': 'NHOM_KH',
                        'Tình trạng đơn':'TINH TRANG DON'
                   
                    }

                    df.rename(columns={col: df_quo_dict[col] for col in df.columns if col in df_quo_dict}, inplace=True)


                    """ REMOVE UNNECESSARY COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
                    removed_cols = [
                        'Phương  tiện  vận  chuyển',
                        'STT'
                        'Mã đối tượng',
                        'Loại xe',
                        'Tuổi xe',
                        'Nhóm KH',
                        'Người thụ hưởng'
                    ]

                    # Removing columns, check if the columns exist
                    columns_to_remove = [col for col in removed_cols if col in df.columns]
                    df.drop(columns=columns_to_remove, inplace=True)
                    
                    # Remove Reins Columns
                    try:
                        phi_bh_index = df.columns.get_loc("PHI_BH")
                    except KeyError:
                        if diagnostics:
                            print("Column 'PHI_BH' not found in DataFrame")
                        raise

                    # Step 2: Drop from the next column after "PHI_BH" onwards
                    df.drop(df.columns[phi_bh_index + 1:], axis=1, inplace=True)


                    """ ADD COLUMN FOR DATA YEAR"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nAdding Column NAM_DATA:")
                    if dup_year:
                        df['NAM_DATA'] = file
                    else:
                        df['NAM_DATA'] = year
                    
                    
                    """ FILTER FOR LHNV"""
                    if lhnv:
                        if diagnostics:
                            print("--------------------------------------------------------------------------\nFiltering for LHNV:")    
                        rows_b4 = df.shape[0]    
                        df = df[df['MA_LHNV'].str.startswith(lhnv)]
                        if diagnostics:
                            print(f'   Removed: {(rows_b4 - df.shape[0]):,.0f} Rows, ({((rows_b4 - df.shape[0])/rows_b4*100):.2f}%)')


                    """ CONVERT DATE COLUMNS""" 
                    if diagnostics:          
                        print("--------------------------------------------------------------------------\nReformatting Date Cols:")
                    dates_columns = [
                        "NGAY_CAP",
                        "NGAY_KHOI_HANH",
                        "NGAY_HL",
                        "NGAY_KT",
                        "NGAY_NOP_PHI"
                    ]

                    for dates_col in dates_columns:
                        if dates_col in df.columns:  # Ensure column exists before converting
                            original_na_count = df[dates_col].isna().sum()
                            df[dates_col] = pd.to_datetime(df[dates_col], errors='coerce', dayfirst=True)
                            new_na_count = df[dates_col].isna().sum()
                            detected_errors = new_na_count - original_na_count
                            if (detected_errors > 0) & diagnostics:
                                print(f"   Detected {detected_errors} Incorrect Dates in {dates_col}")
                        elif diagnostics:
                            print(f"   Column {dates_col} not found in DataFrame.")


                    """ CONVERT NUMERICAL COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nReformatting Num Cols:")
                    num_columns = [
                        'STBH',
                        'PHI_BH',
                    ]
                    
                    for num_col in num_columns:
                        if num_col in df.columns:  # Ensure column exists before converting
                            original_na_count = df[num_col].isna().sum()
                            df[num_col] = pd.to_numeric(df[num_col], errors='coerce')
                            new_na_count = df[num_col].isna().sum()
                            detected_errors = new_na_count - original_na_count
                            if (detected_errors > 0) & diagnostics:
                                print(f"   Detected {detected_errors} Incorrect Values in {num_col}")
                        elif diagnostics:
                            print(f"   Column {num_col} not found in DataFrame.")
                        
                    
                    
                    """ REPLACE BLANKS WITH NAs """
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nReplacing Blanks:")
                    def replace_blanks(x):
                        if isinstance(x, str) and x.strip() == '':
                            return np.nan
                        else:
                            return x
                        
                    for col in df.columns:
                        col_copy = df[col].copy()
                        df[col] = df[col].apply(replace_blanks)
                        # replaced = (col_copy != df[col]).sum()
                        # if (replaced > 0) and diagnostics:
                        #     print(f"   Converted {replaced} values in {col}")
                    
                    del col_copy
                    
                    
                    """ SAVE DF TO GLOBAL VARIABLE"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nSaving DF:")
                    # Assign DataFrame to a global variable dynamically using the year
                    if dup_year:
                        df_name = f'{file}'
                    else:    
                        df_name = f'df_quo_{year}'
                    globals()[df_name] = df
                    global_df_names.append(df_name)
                    if dup_year & diagnostics:
                        print(f"Summary of {file}:\n   -NUM POLS = {df.shape[0]:,.0f}\n   -TOTAL QUOTED = {df['PHI_BH'].sum():,.0f}")
                    elif diagnostics:    
                        print(f"Summary of CY{year}:\n   -NUM POLS = {df.shape[0]:,.0f}\n   -TOTAL QUOTED = {df['PHI_BH'].sum():,.0f}")
                        print('--------------------------------------------------------------------------\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                except Exception as e:
                    if diagnostics:
                        print(f"Failed to process {file}: {e}")
            else:
                if diagnostics:
                    print(f"No year found in the file name {file}")

    # Print all global DataFrame names created
    print("\n\n\n==========================================================================\n==========================================================================\nSuccessfully Imported:", ", ".join(global_df_names))
    
    """ CONCAT INTO ONE DF"""
    all_dataframes = [globals()[name] for name in global_df_names if name in globals()]
    df_quo = pd.concat(all_dataframes, ignore_index=True)
    print(f"   -NUM POLS = {df_quo.shape[0]:,.0f}\n   -TOTAL QUOTED = {df_quo['PHI_BH'].sum():,.0f}")
    
    print("==========================================================================\n==========================================================================")
    for name in global_df_names:
        del globals()[name]
        
    global_df_names.clear()
    
    return df_quo




## NGHIEN CUU THEM


# def load_quote_credit(directory, skip_rows=4, lhnv = None, dup_year = False, diagnostics = True):  
#     # Regular expression to find a four-digit year in the file name
#     year_pattern = re.compile(r'\b(\d{4})\b')

#     # List to keep track of the names of the DataFrames stored as globals
#     global_df_names = []

#     # Iterate through each file in the specified directory
#     starting_file = True
#     for file in sorted(os.listdir(directory)):
#         if file.endswith('.xlsx') and not file.startswith('~$'):
            
#             # Find the year in the file name
#             match = year_pattern.search(file)
#             if match:
#                 year = match.group(1)
#                 file_path = os.path.join(directory, file)
#                 try:
#                     """ IMPORT DATA"""
#                     if diagnostics:
#                         if starting_file:
#                             print(f"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n--------------------------------------------------------------------------\nImporting: {file}")
#                             starting_file = False 
#                         else:
#                             print(f"\n\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n--------------------------------------------------------------------------\nImporting: {file}")
#                     # Load and clean data specifying the engine
#                     df = pd.read_excel(file_path, header=None, skiprows=skip_rows, engine='openpyxl')
#                     df.drop(df.columns[-1], axis = 1, inplace = True)  # remove na col at the end
                    
#                     df.iloc[0,17] = 'Phương tiện vận chuyển TRUE'
                    
#                     # Dynamically determine headers based on the first non-empty cell per column
#                     headers = []
#                     for col in df.columns:
#                         if pd.notna(df.iloc[1, col]):
#                             headers.append(df.iloc[1, col])
#                         elif pd.notna(df.iloc[0, col]) and pd.isna(df.iloc[1, col]):
#                             headers.append(df.iloc[0, col])
#                         elif diagnostics:
#                             print(f'No headers found for {col}')

#                     # Set the determined headers as column names
#                     df.columns = headers
#                     df = df.drop([0, 1])
#                     df.reset_index(drop = True, inplace=True)
#                     if diagnostics:
#                         print(f'   Rows = {df.shape[0]}')
#                     # print(f'Columns = {df.shape[1]}')
            
            
#                     """ RENAME COLUMNS"""
#                     if diagnostics:
#                         print("--------------------------------------------------------------------------\nRenaming Columns:")
                    
#                     df_quo_dict = {
#                         'Đơn vị': 'MA_DVI_QL',
#                         'Kiểu HĐ': 'KIEU_HD',
#                         'Số GCN': 'SO_GCN',
#                         'SĐBS': 'SDBS',
#                         'Ngày cấp': 'NGAY_CAP',
#                         'Quy tắc áp dụng': 'QUY_TAC_AP_DUNG',
#                         'Điều kiện quy đổi': 'DIEU_KIEN_QUY_DOI',
#                         'Người  được  BH': 'NGUOI_DUOC_BH',
#                         'MST':'MST',
#                         'Nhóm' : 'MA_LHNV',
#                         'Nhóm hàng' : 'NHOM HANG',
#                         'Phương  tiện  vận  chuyển TRUE' : 'PHUONG_TIEN_VC',
#                         'Hàng hóa  được BH' : 'HH_DUOC_BH',
#                         'Số lượng/Trọng lượng' : 'TRONG_LUONG',
#                         'Phương thức đóng gói' : 'PHUONG_THUC_DONG GOI',
#                         'Ngày  khởi hành': 'NGAY_KHOI_HANH',
#                         'Ngày hiệu lực' : 'NGAY_HL',
#                         'Ngày kết thúc' : 'NGAY_KT',
#                         'Từ' : 'FROM',
#                         'Chuyển  tải': 'CHUYEN_TAI',
#                         'Đến' : 'TO',
#                         'Nguyên tệ': 'NGUYEN_TE',
#                         'Số tiền': 'STBH',
#                         'Quy đổi VNĐ' : 'QUY_DOI_VND',
#                         'Nguyên tệ': 'NGUYEN_TE',
#                         'Tỷ lệ phí  chính' : 'TY_LE_PHI_CHINH',
#                         'Phí chính': 'PHI_BH',
#                         'Tỷ lệ phụ phí' : 'TY_LE_PHU_PHI',
#                         'Phụ  phí' : 'PHU PHI',
#                         'Tổng phí': 'TONG_PHI',
#                         'Phí Quy đổi': 'PHI_QUY_DOI',
#                         'Ngày nộp phí': 'NGAY_NOP_PHI',
#                         'Kiểu đồng BH' : 'KIEU_DBH',
#                         'Tỷ lệ VBI' : 'TY_LE_VBI',
#                         'Treaty': 'TREATY',
#                         'Fax':'FAX',
#                         'Cán bộ quản lý': 'CAN_BO_QUAN_LY',
#                         'Đại lý khai thác': 'DAI_LY_KT',
#                         'Nguồn khai thác': 'NGUON_KT',
#                         'Nhóm khách hàng': 'NHOM_KH',
#                         'Tình trạng đơn':'TINH TRANG DON'
                   
#                     }

#                     df.rename(columns={col: df_quo_dict[col] for col in df.columns if col in df_quo_dict}, inplace=True)


#                     """ REMOVE UNNECESSARY COLUMNS"""
#                     if diagnostics:
#                         print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
#                     removed_cols = [
#                         'Phương  tiện  vận  chuyển',
#                         'STT'
#                         'Mã đối tượng',
#                         'Loại xe',
#                         'Tuổi xe',
#                         'Nhóm KH',
#                         'Người thụ hưởng'
#                     ]

#                     # Removing columns, check if the columns exist
#                     columns_to_remove = [col for col in removed_cols if col in df.columns]
#                     df.drop(columns=columns_to_remove, inplace=True)
                    
#                     # Remove Reins Columns
#                     try:
#                         phi_bh_index = df.columns.get_loc("PHI_BH")
#                     except KeyError:
#                         if diagnostics:
#                             print("Column 'PHI_BH' not found in DataFrame")
#                         raise

#                     # Step 2: Drop from the next column after "PHI_BH" onwards
#                     df.drop(df.columns[phi_bh_index + 1:], axis=1, inplace=True)


#                     """ ADD COLUMN FOR DATA YEAR"""
#                     if diagnostics:
#                         print("--------------------------------------------------------------------------\nAdding Column NAM_DATA:")
#                     if dup_year:
#                         df['NAM_DATA'] = file
#                     else:
#                         df['NAM_DATA'] = year
                    
                    
#                     """ FILTER FOR LHNV"""
#                     if lhnv:
#                         if diagnostics:
#                             print("--------------------------------------------------------------------------\nFiltering for LHNV:")    
#                         rows_b4 = df.shape[0]    
#                         df = df[df['MA_LHNV'].str.startswith(lhnv)]
#                         if diagnostics:
#                             print(f'   Removed: {(rows_b4 - df.shape[0]):,.0f} Rows, ({((rows_b4 - df.shape[0])/rows_b4*100):.2f}%)')


#                     """ CONVERT DATE COLUMNS""" 
#                     if diagnostics:          
#                         print("--------------------------------------------------------------------------\nReformatting Date Cols:")
#                     dates_columns = [
#                         "NGAY_CAP",
#                         "NGAY_KHOI_HANH",
#                         "NGAY_HL",
#                         "NGAY_KT",
#                         "NGAY_NOP_PHI"
#                     ]

#                     for dates_col in dates_columns:
#                         if dates_col in df.columns:  # Ensure column exists before converting
#                             original_na_count = df[dates_col].isna().sum()
#                             df[dates_col] = pd.to_datetime(df[dates_col], errors='coerce', dayfirst=True)
#                             new_na_count = df[dates_col].isna().sum()
#                             detected_errors = new_na_count - original_na_count
#                             if (detected_errors > 0) & diagnostics:
#                                 print(f"   Detected {detected_errors} Incorrect Dates in {dates_col}")
#                         elif diagnostics:
#                             print(f"   Column {dates_col} not found in DataFrame.")


#                     """ CONVERT NUMERICAL COLUMNS"""
#                     if diagnostics:
#                         print("--------------------------------------------------------------------------\nReformatting Num Cols:")
#                     num_columns = [
#                         'STBH',
#                         'PHI_BH',
#                     ]
                    
#                     for num_col in num_columns:
#                         if num_col in df.columns:  # Ensure column exists before converting
#                             original_na_count = df[num_col].isna().sum()
#                             df[num_col] = pd.to_numeric(df[num_col], errors='coerce')
#                             new_na_count = df[num_col].isna().sum()
#                             detected_errors = new_na_count - original_na_count
#                             if (detected_errors > 0) & diagnostics:
#                                 print(f"   Detected {detected_errors} Incorrect Values in {num_col}")
#                         elif diagnostics:
#                             print(f"   Column {num_col} not found in DataFrame.")
                        
                    
                    
#                     """ REPLACE BLANKS WITH NAs """
#                     if diagnostics:
#                         print("--------------------------------------------------------------------------\nReplacing Blanks:")
#                     def replace_blanks(x):
#                         if isinstance(x, str) and x.strip() == '':
#                             return np.nan
#                         else:
#                             return x
                        
#                     for col in df.columns:
#                         col_copy = df[col].copy()
#                         df[col] = df[col].apply(replace_blanks)
#                         # replaced = (col_copy != df[col]).sum()
#                         # if (replaced > 0) and diagnostics:
#                         #     print(f"   Converted {replaced} values in {col}")
                    
#                     del col_copy
                    
                    
#                     """ SAVE DF TO GLOBAL VARIABLE"""
#                     if diagnostics:
#                         print("--------------------------------------------------------------------------\nSaving DF:")
#                     # Assign DataFrame to a global variable dynamically using the year
#                     if dup_year:
#                         df_name = f'{file}'
#                     else:    
#                         df_name = f'df_quo_{year}'
#                     globals()[df_name] = df
#                     global_df_names.append(df_name)
#                     if dup_year & diagnostics:
#                         print(f"Summary of {file}:\n   -NUM POLS = {df.shape[0]:,.0f}\n   -TOTAL QUOTED = {df['PHI_BH'].sum():,.0f}")
#                     elif diagnostics:    
#                         print(f"Summary of CY{year}:\n   -NUM POLS = {df.shape[0]:,.0f}\n   -TOTAL QUOTED = {df['PHI_BH'].sum():,.0f}")
#                         print('--------------------------------------------------------------------------\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#                 except Exception as e:
#                     if diagnostics:
#                         print(f"Failed to process {file}: {e}")
#             else:
#                 if diagnostics:
#                     print(f"No year found in the file name {file}")

#     # Print all global DataFrame names created
#     print("\n\n\n==========================================================================\n==========================================================================\nSuccessfully Imported:", ", ".join(global_df_names))
    
#     """ CONCAT INTO ONE DF"""
#     all_dataframes = [globals()[name] for name in global_df_names if name in globals()]
#     df_quo = pd.concat(all_dataframes, ignore_index=True)
#     print(f"   -NUM POLS = {df_quo.shape[0]:,.0f}\n   -TOTAL QUOTED = {df_quo['PHI_BH'].sum():,.0f}")
    
#     print("==========================================================================\n==========================================================================")
#     for name in global_df_names:
#         del globals()[name]
        
#     global_df_names.clear()
    
#     return df_quo

