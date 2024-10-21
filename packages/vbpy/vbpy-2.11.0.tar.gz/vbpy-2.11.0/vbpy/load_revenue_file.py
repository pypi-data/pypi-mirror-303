import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None) 
pd.set_option('display.max_columns', None)  

import os
import re
from tqdm import tqdm

def load_revenue_auto(directory, skip_rows=13, lhnv = None, dup_year = False, diagnostics = True):
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
                    df_rev_dict = {
                        'Mã đơn vị': 'MA_DVI',
                        'Mã đơn vị quản lý hợp đồng': 'MA_DVI_QL',
                        'Số hợp đồng': 'SO_HD',
                        'Đối tượng bảo hiểm': 'SO_BIEN_XE',
                        'Giấy chứng nhận': 'SO_GCN',
                        'Giấy chứng nhận gốc': 'SO_GCN_GOC',
                        'Tuổi xe': 'TUOI_XE',
                        'Phòng': 'PHONG_BT',
                        'Ngày cấp': 'NGAY_CAP',
                        'Ngày bán hàng': 'NGAY_PSINH_PHI',
                        'Ngày HL': 'NGAY_HL',
                        'Ngày kết thúc': 'NGAY_KT',
                        'Mã khách hàng': 'MA_KH',
                        'Tên khách hàng': 'TEN_KH',
                        'Nguồn KT': 'NGUON_KT',
                        'LHNV': 'MA_LHNV',
                        'Tên LHNV': 'TEN_LHNV',
                        'Nguyên tệ số tiền BH': 'NGUYEN_TE',
                        'Số tiền bảo hiểm': 'STBH',
                        'Phí doanh thu': 'PHI_BH',
                        'Mã đối tượng': 'NHOM_XE',
                        'Loại': 'NHOM_XE_2',
                        'Nhóm': 'LOAI_XE',
                        'Loại KH': 'LOAI_KH',
                        'Phân khúc': 'PHAN_KHUC_KH',
                        'Số CMT/MST': 'SO_CMT/MST',
                        'Đại lý': 'DAI_LY',
                        'CBQL': 'CAN_BO_QL',
                        'Giá trị xe': 'GIA_TRI_XE'
                    }

                    df.rename(columns={col: df_rev_dict[col] for col in df.columns if col in df_rev_dict}, inplace=True)


                    """ REMOVE UNNECESSARY COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
                    removed_cols = [
                        'Nhóm KH',
                        'Người thụ hưởng',
                        'Ngày kỳ thanh toán',
                        'Kiểu ĐBH', 
                        'TL của VBI',
                        'STT'
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
                        "NGAY_PSINH_PHI",
                        "NGAY_HL",
                        "NGAY_KT"
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
                        'TUOI_XE',
                        'STBH',
                        'PHI_BH',
                        'GIA_TRI_XE'
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
                    
                    
                    """ PROCESS DUPLICATED/COINSURED ROWS """
                    if year != '2020':  #SO_GCN was not recorded before 2021.
                        if diagnostics:
                            print("--------------------------------------------------------------------------\nProcessing Dup/Coins Rows:")

                        """ Step 1 - Remove Duplicated Policies """  # Result - Removed Policies with multiple Premium Transactions
                        _nrows_bf1 = df.shape[0]
                        _rev_bf1 = df['PHI_BH'].sum()
                        df = df[~df.duplicated(subset = ['MA_DVI', 'SO_HD', 'SO_GCN', 'SO_BIEN_XE', 'STBH'])] # Policies with the same Pol ID, Department ID, GCN, and SI amount are duplicates
                        
                        if diagnostics:
                            print(f"Step 1 - Remove Duplicates\n   -Removed {(_nrows_bf1 - df.shape[0]):,.0f} Rows\n   -Change in Tot Revenue = {(_rev_bf1 - df['PHI_BH'].sum()):,.0f} ({((_rev_bf1 - df['PHI_BH'].sum())/_rev_bf1*100):,.0f}%)")

                        """ Step 2 - Aggregate Claims with Multiple Department IDs """  # Poclies with same Claim ID, different Department ID
                        _nrows_bf2 = df.shape[0]
                        _rev_bf2 = df['PHI_BH'].sum()
                        df["IS_MAIN"] = df.apply(lambda x: x["SO_HD"][:3] == x["MA_DVI"], axis=1)
                        df = df[df["IS_MAIN"]]
                        df.drop('IS_MAIN', axis = 1, inplace = True)

                        if diagnostics:
                            print(f"Step 2 - Adjust for Internal Coinsurance\n   -Removed {(_nrows_bf2 - df.shape[0]):,.0f} Rows\n   -Change in Tot Revenue = {(_rev_bf2 - df['PHI_BH'].sum()):,.0f} ({((_rev_bf2 - df['PHI_BH'].sum())/_rev_bf2*100):,.0f}%)")

                        """ Step 3 - Remove the rest of the Dups """ 
                        _nrows_bf3 = df.shape[0] 
                        _rev_bf3 = df['PHI_BH'].sum()
                        df = df[~df.duplicated(subset = ['NGAY_HL', 'SO_GCN', 'SO_BIEN_XE', 'SO_HD', 'STBH'])]
        
                        if diagnostics:
                            print(f"Step 3 - Remove Rest of Duplicates\n   -Removed {(_nrows_bf3 - df.shape[0]):,.0f} Rows\n   -Change in Tot Revenue = {(_rev_bf3 - df['PHI_BH'].sum()):,.0f} ({((_rev_bf3 - df['PHI_BH'].sum())/_rev_bf3*100):,.0f}%)")
                        
                    
                    
                    """ REGROUP VEHICLE TYPE """
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nAdding LOAI_XE_MOI and NHOM_XE_MOI:")    
                    df.loc[:, "LOAI_XE_MOI"] = df["LOAI_XE"]

                    df.loc[(df['LOAI_XE'] == "Xe vừa chở người vừa chở hàng") &
                                (df['NHOM_XE'] != "NHOM.02"), 'LOAI_XE_MOI'] = "Xe vừa chở người vừa chở hàng không kinh doanh"

                    df.loc[(df['LOAI_XE'] == "Xe vừa chở người vừa chở hàng") &
                                (df['NHOM_XE'] == "NHOM.02"), 'LOAI_XE_MOI'] = "Xe vừa chở người vừa chở hàng kinh doanh"

                    df.loc[(df['LOAI_XE'] == "Xe gắn cẩu") &
                                (df['NHOM_XE'] == "NHOM.04"), 'LOAI_XE_MOI'] = "Xe đầu kéo, container"

                    new_type_to_group = {
                        "Xe Bus": "NHOM.1A",
                        "Xe Bus": "NHOM.1A",
                        "Xe vận tải hành khách (nội tỉnh, liên tỉnh)": "NHOM.1A",
                        
                        "Xe vừa chở người vừa chở hàng kinh doanh": "NHOM.1A",
                        "Xe chở khách du lịch theo hợp đồng": "NHOM.1A",
                        "Xe kinh doanh chở người": "NHOM.1A",
                        
                        "Xe chở người không kinh doanh": "NHOM.1B",
                        "Xe vừa chở người vừa chở hàng không kinh doanh": "NHOM.1B",

                        "Xe đầu kéo, container": "NHOM.2A",
                        "Xe Ro mooc": "NHOM.2A",
                        "Xe tải bảo ôn": "NHOM.2A",
                        "Xe tải thùng dưới 9 tấn": "NHOM.2A",
                        "Xe tải thùng từ 9 tấn trở lên": "NHOM.2A",
                        "Xe gắn cẩu": "NHOM.2A",
                        "Xe đông lạnh": "NHOM.2A",
                        "Xe trộn bê tông, xe tải ben": "NHOM.2A",
                        
                        "Xe téc chở xi măng": "NHOM.2A",
                        
                        "Xe bơm bê tông": "NHOM.2B",
                        "Xe chở xăng dầu, nhựa đường": "NHOM.2B",
                        "Xe máy chuyên dùng": "NHOM.2B",
                        "Xe hoạt động trong vùng khai thác khoáng sản": "NHOM.2B",
                        "Xe tải ben": "NHOM.2B",
                        "Xe trộn bê tông": "NHOM.2B",

                        "Xe chở tiền chuyên dụng": "NHOM.2C",
                        "Xe téc chở nước": "NHOM.2C",
                        "Xe vệ sinh, quét đường": "NHOM.2C",
                        "Xe chuyên dụng khác": "NHOM.2C",
                        "Xe cứu hộ": "NHOM.2C",
                        "Xe cứu thương": "NHOM.2C",

                        "Xe taxi, cho thuê tự lái": "NHOM.3A",
                        "Xe kinh doanh taxi công nghệ": "NHOM.3A",

                        "Xe tập lái - Bán tải (Pick-up)": "NHOM.3B",
                        "Xe tập lái - Xe tải": "NHOM.3B",
                        "Xe tập lái (xe chở người)": "NHOM.3B"
                    }

                    df.loc[:,'NHOM_XE_MOI'] = df['LOAI_XE_MOI'].map(new_type_to_group)  
                    
                    rows_b4 = df.shape[0]    
                    df = df[df['NHOM_XE_MOI'].notna()]
                    if diagnostics:
                        print(f'   Removed: {(rows_b4 - df.shape[0]):,.0f} Rows Missing NHOM_XE_MOI ({((rows_b4 - df.shape[0])/rows_b4*100):.2f}%)')
                    
                    
                    """ REMOVE ROWs WITH MISSING EFF DATE """
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemove Rows Missing NGAY_HL:")    
                    rows_b4 = df.shape[0]    
                    df = df[df['NGAY_HL'].notna()]
                    if diagnostics:
                        print(f'   Removed: {(rows_b4 - df.shape[0]):,.0f} Rows, ({((rows_b4 - df.shape[0])/rows_b4*100):.2f}%)')
                    
                    
                    " STANDARDIZE PLATE IDs"
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nStandardizing SO_BIEN_XE:")    
                    pattern = r'^\d{2}[A-Za-z]\d{4,5}$' 
                    try:
                        _copy = df['SO_BIEN_XE'].copy()
                        df.loc[:,'SO_BIEN_XE'] = df['SO_BIEN_XE'].str.replace('[^a-zA-Z0-9]', '', regex=True)
                        df.loc[:,'SO_BIEN_XE'] = df['SO_BIEN_XE'].str.strip().str.upper()
                        df.loc[df['SO_BIEN_XE'] == '', 'SO_BIEN_XE'] = pd.NA
                        df.loc[~df['SO_BIEN_XE'].str.match(pattern, na = False), 'SO_BIEN_XE'] = pd.NA
                        
                        if diagnostics:
                            print(f"   Changed: {sum(df['SO_BIEN_XE'] == _copy)} values")
                            print(f"   Converted: {df['SO_BIEN_XE'].isna().sum() - _copy.isna().sum()} to NAs")
                        del _copy
                        
                        if diagnostics:
                            print(f'   Standardization Successful')
                    except Exception as e:
                        if diagnostics:
                            print(f'   Standardization Failed')
                    
                    
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
                        replaced = (col_copy != df[col]).sum()
                        if (replaced > 0) & diagnostics:
                            print(f"   Converted {replaced} values in {col}")
                    
                    del col_copy
                    
                    
                    """ PRINT EFF_YEAR COUNTS IN EACH DF"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nEff Year Count:")
                    df['NAM_HL'] = df['NGAY_HL'].dt.year 
                    if dup_year & diagnostics:
                        print(f"Effective Year Count in {file}: {df['NAM_HL'].value_counts()}")
                    elif diagnostics:
                        print(f"Effective Year Count in CY{year}: {df['NAM_HL'].value_counts()}")
                    
                    
                    """ SAVE DF TO GLOBAL VARIABLE"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nSaving DF:")
                    # Assign DataFrame to a global variable dynamically using the year
                    if dup_year:
                        df_name = f'{file}'
                    else:    
                        df_name = f'df_rev_{year}'
                    globals()[df_name] = df
                    global_df_names.append(df_name)
                    if dup_year & diagnostics:
                        print(f"Summary of {file}:\n   -NUM POLS = {df.shape[0]:,.0f}\n   -TOTAL REVENUE = {df['PHI_BH'].sum():,.0f}")
                    elif diagnostics:    
                        print(f"Summary of CY{year}:\n   -NUM POLS = {df.shape[0]:,.0f}\n   -TOTAL REVENUE = {df['PHI_BH'].sum():,.0f}")
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
    df_rev = pd.concat(all_dataframes, ignore_index=True)
    print(f"   -NUM POLS = {df_rev.shape[0]:,.0f}\n   -TOTAL REVENUE = {df_rev['PHI_BH'].sum():,.0f}")
    
    print("==========================================================================\n==========================================================================")
    for name in global_df_names:
        del globals()[name]
        
    global_df_names.clear()
    
    return df_rev




def load_revenue_property(directory, skip_rows=13, lhnv = None, dup_year = False, diagnostics = True):
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
                    df_rev_dict = {
                        'Mã đơn vị': 'MA_DVI',
                        'Mã đơn vị quản lý hợp đồng': 'MA_DVI_QL',
                        'Số hợp đồng': 'SO_HD',
                        'Đối tượng bảo hiểm': 'DOI_TUONG_BH',
                        'Loại': 'LOAI_TS',
                        'Mã đối tượng': 'NHOM_TS',
                        'Phòng': 'PHONG_BT',
                        'Ngày cấp': 'NGAY_CAP',
                        'Ngày HL': 'NGAY_HL',
                        'Ngày kết thúc': 'NGAY_KT',
                        'Loại KH': 'LOAI_KH',
                        'Phân khúc': 'PHAN_KHUC_KH',
                        'Mã khách hàng': 'MA_KH',
                        'Tên khách hàng': 'TEN_KH',
                        'Số CMT/MST': 'SO_CMT/MST',
                        'Đại lý': 'DAI_LY',
                        'CBQL': 'CAN_BO_QL',
                        'Nguồn KT': 'NGUON_KT',
                        'Ngày bán hàng': 'NGAY_PSINH_PHI',
                        'LHNV': 'MA_LHNV',
                        'Tên LHNV': 'TEN_LHNV',
                        'Nguyên tệ số tiền BH': 'NGUYEN_TE',
                        'Số tiền bảo hiểm': 'STBH',
                        'Phí doanh thu': 'PHI_BH'
                    }

                    df.rename(columns={col: df_rev_dict[col] for col in df.columns if col in df_rev_dict}, inplace=True)


                    """ REMOVE UNNECESSARY COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
                    removed_cols = [
                        'Nhóm',
                        'Giấy chứng nhận',
                        'Giấy chứng nhận gốc',
                        'Tuổi xe',
                        'Giá trị xe',
                        'Nhóm KH',
                        'Người thụ hưởng',
                        'Ngày kỳ thanh toán',
                        'Kiểu ĐBH', 
                        'TL của VBI',
                        'STT'
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
                        "NGAY_BAN",
                        "NGAY_HL",
                        "NGAY_KT"
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
                        
                    
                    
                    """ REMOVE ROWs WITH MISSING EFF DATE """
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemove Rows Missing NGAY_HL:")    
                    rows_b4 = df.shape[0]    
                    df = df[df['NGAY_HL'].notna()]
                    if diagnostics:
                        print(f'   Removed: {(rows_b4 - df.shape[0]):,.0f} Rows, ({((rows_b4 - df.shape[0])/rows_b4*100):.2f}%)')
                    
                    
                    
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
                        replaced = (col_copy != df[col]).sum()
                        if (replaced > 0) & diagnostics:
                            print(f"   Converted {replaced} values in {col}")
                    
                    del col_copy
                    
                    
                    """ PRINT EFF_YEAR COUNTS IN EACH DF"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nEff Year Count:")
                    df['NAM_HL'] = df['NGAY_HL'].dt.year 
                    if dup_year & diagnostics:
                        print(f"Effective Year Count in {file}: {df['NAM_HL'].value_counts()}")
                    elif diagnostics:
                        print(f"Effective Year Count in CY{year}: {df['NAM_HL'].value_counts()}")
                    
                    
                    """ SAVE DF TO GLOBAL VARIABLE"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nSaving DF:")
                    # Assign DataFrame to a global variable dynamically using the year
                    if dup_year:
                        df_name = f'{file}'
                    else:    
                        df_name = f'df_rev_{year}'
                    globals()[df_name] = df
                    global_df_names.append(df_name)
                    if dup_year & diagnostics:
                        print(f"Summary of {file}:\n   -NUM POLS = {df.shape[0]:,.0f}\n   -TOTAL REVENUE = {df['PHI_BH'].sum():,.0f}")
                    elif diagnostics:    
                        print(f"Summary of CY{year}:\n   -NUM POLS = {df.shape[0]:,.0f}\n   -TOTAL REVENUE = {df['PHI_BH'].sum():,.0f}")
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
    df_rev = pd.concat(all_dataframes, ignore_index=True)
    print(f"   -NUM POLS = {df_rev.shape[0]:,.0f}\n   -TOTAL REVENUE = {df_rev['PHI_BH'].sum():,.0f}")
    
    print("==========================================================================\n==========================================================================")
    for name in global_df_names:
        del globals()[name]
        
    global_df_names.clear()
    
    return df_rev




def load_revenue_marine(directory, skip_rows=13, lhnv = None, dup_year = False, diagnostics = True):
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
                        
                    def dynamically_rename_columns(df, name_mapping):
                        from collections import Counter
                        name_count = Counter()
                        new_names = []

                        for col in df.columns:
                            if col in name_mapping:
                                name_count[col] += 1
                                # Apply a new name based on the mapping and occurrence count
                                new_name = f"{name_mapping[col]}_{name_count[col]}"
                                new_names.append(new_name)
                            else:
                                new_names.append(col)

                        df.columns = new_names
                        return df

                    # Define renaming dictionary
                    name_mapping = {
                        'Tỷ lệ': 'TL',
                        'Phí tái': 'PHI'
                    }    
                    
                    df = dynamically_rename_columns(df, name_mapping)
                    
                    df_rev_dict = {
                        'Mã đơn vị quản lý hợp đồng': 'MA_DVI_QL',
                        'Số hợp đồng': 'SO_HD',
                        'Đối tượng bảo hiểm': 'LOAI_HH',
                        'Phương thức đóng gói': 'PT_DONG_GOI',
                        'Phòng': 'PHONG_BT',
                        'Ngày cấp': 'NGAY_CAP',
                        'Ngày HL': 'NGAY_HL',
                        'Ngày kết thúc': 'NGAY_KT',
                        'Loại KH': 'LOAI_KH',
                        'Phân khúc': 'PHAN_KHUC_KH',
                        'Mã khách hàng': 'MA_KH',
                        'Tên khách hàng': 'TEN_KH',
                        'Đại lý': 'DAI_LY',
                        'CBQL': 'CAN_BO_QL',
                        'Nguồn KT': 'NGUON_KT',
                        'Ngày phát sinh phí': 'NGAY_PSINH_PHI',
                        'LHNV': 'MA_LHNV',
                        'Tên LHNV': 'TEN_LHNV',
                        'Điều kiện': 'DIEU_KIEN',
                        'Nguyên tệ số tiền BH': 'NGUYEN_TE',
                        'Số tiền bảo hiểm': 'STBH',
                        'Tỷ lệ phí': 'TLP',
                        'Phí doanh thu': 'PHI_BH',
                        'Kiểu ĐBH': 'KIEU_DBH', 
                        'TL của VBI': 'TL_DBH',
                        'TL_1': 'TL_TTT', # first column named Tỷ lệ
                        'PHI_1': 'PHI_TTT', # first column named Phí tái
                        'TL_2': 'TL_PTL', # second column named Tỷ lệ
                        'PHI_2': 'PHI_PTL' # second column named Phí tái
                    }

                    df.rename(columns={col: df_rev_dict[col] for col in df.columns if col in df_rev_dict}, inplace=True)


                    """ REMOVE UNNECESSARY COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
                    removed_cols = [
                        'STT'
                        'Mã đối tượng',
                        'Loại xe',
                        'Tuổi xe',
                        'Nhóm KH',
                        'Người thụ hưởng',
                        
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
                        "NGAY_PSINH_PHI",
                        "NGAY_HL",
                        "NGAY_KT"
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
                        replaced = (col_copy != df[col]).sum()
                        if (replaced > 0) & diagnostics:
                            print(f"   Converted {replaced} values in {col}")
                    
                    del col_copy
                    
                    
                    """ SAVE DF TO GLOBAL VARIABLE"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nSaving DF:")
                    # Assign DataFrame to a global variable dynamically using the year
                    if dup_year:
                        df_name = f'{file}'
                    else:    
                        df_name = f'df_rev_{year}'
                    globals()[df_name] = df
                    global_df_names.append(df_name)
                    if dup_year & diagnostics:
                        print(f"Summary of {file}:\n   -NUM POLS = {df.shape[0]:,.0f}\n   -TOTAL REVENUE = {df['PHI_BH'].sum():,.0f}")
                    elif diagnostics:    
                        print(f"Summary of CY{year}:\n   -NUM POLS = {df.shape[0]:,.0f}\n   -TOTAL REVENUE = {df['PHI_BH'].sum():,.0f}")
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
    df_rev = pd.concat(all_dataframes, ignore_index=True)
    print(f"   -NUM POLS = {df_rev.shape[0]:,.0f}\n   -TOTAL REVENUE = {df_rev['PHI_BH'].sum():,.0f}")
    
    print("==========================================================================\n==========================================================================")
    for name in global_df_names:
        del globals()[name]
        
    global_df_names.clear()
    
    return df_rev


def load_revenue_credit(directory, skip_rows=13, lhnv = None, dup_year = False, diagnostics = True):
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
                    df_rev_dict = {
                        'Mã đơn vị': 'MA_DVI',
                        'Mã đơn vị quản lý hợp đồng': 'MA_DVI_QL',
                        'Số hợp đồng': 'SO_HD',
                        'Đối tượng bảo hiểm': 'DOI_TUONG_BH',
                        'Giấy chứng nhận': 'SO_GCN',
                        'Giấy chứng nhận gốc': 'SO_GCN_GOC',
                        'Mã đối tượng': 'MA_DOI_TUONG',
                        'Loại' : 'LOAI',
                        'Nhóm': 'NHOM',
                        'Tuổi xe': 'TUOI_XE',
                        'Phòng': 'PHONG_BT',
                        'Ngày cấp': 'NGAY_CAP',
                        'Ngày HL': 'NGAY_HL',
                        'Ngày kết thúc': 'NGAY_KT',
                        'Nhóm KH': 'NHOM_KH',
                        'Loại KH': 'LOAI_KH',
                        'Phân khúc' : 'PHAN_KHUC',
                        'Mã khách hàng': 'MA_KH',
                        'Tên khách hàng': 'TEN_KH',
                        'Số CMT/MST': 'SO_CMT/MST',
                        'Đại lý': 'DAI_LY', ##
                        'CBQL': 'CAN_BO_QL',
                        'Nguồn KT': 'NGUON_KT',
                        'Ngày bán hàng': 'NGAY_BAN_HANG', ##
                        'Ngày kỳ thanh toán': 'NGAY_KI_TT',##
                        'LHNV': 'MA_LHNV',
                        'Tên LHNV': 'TEN_LHNV',
                        'Nguyên tệ số tiền BH': 'NGUYEN_TE',
                        'Số tiền bảo hiểm': 'STBH',
                        'Phí doanh thu': 'PHI_BH',
                        'Kiểu đồng BH': 'KIEU_DONG_BH'
                    }

                    df.rename(columns={col: df_rev_dict[col] for col in df.columns if col in df_rev_dict}, inplace=True)


                    """ REMOVE UNNECESSARY COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
                    removed_cols = [
                        'Nhóm KH',
                        'Người thụ hưởng',
                        'Ngày kỳ thanh toán',
                        'Kiểu đồng BH', 
                        'TL của VBI',
                        'STT',
                        'Tỷ lệ tái',
                        'Phí tái'
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
                        "NGAY_PSINH_PHI",
                        "NGAY_HL",
                        "NGAY_KT"
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
                        'PHI_BH'
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
                    
                    
                    # """ PROCESS DUPLICATED/COINSURED ROWS """
                    # if year != '2020':  #SO_GCN was not recorded before 2021.
                    #     if diagnostics:
                    #         print("--------------------------------------------------------------------------\nProcessing Dup/Coins Rows:")

                    #     """ Step 1 - Remove Duplicated Policies """  # Result - Removed Policies with multiple Premium Transactions
                    #     _nrows_bf1 = df.shape[0]
                    #     _rev_bf1 = df['PHI_BH'].sum()
                    #     df = df[~df.duplicated(subset = ['MA_DVI', 'SO_HD', 'SO_GCN', 'STBH'])] # Policies with the same Pol ID, Department ID, GCN, and SI amount are duplicates
                        
                    #     if diagnostics:
                    #         print(f"Step 1 - Remove Duplicates\n   -Removed {(_nrows_bf1 - df.shape[0]):,.0f} Rows\n   -Change in Tot Revenue = {(_rev_bf1 - df['PHI_BH'].sum()):,.0f} ({((_rev_bf1 - df['PHI_BH'].sum())/_rev_bf1*100):,.0f}%)")

                    #     """ Step 2 - Aggregate Claims with Multiple Department IDs """  # Poclies with same Claim ID, different Department ID
                    #     _nrows_bf2 = df.shape[0]
                    #     _rev_bf2 = df['PHI_BH'].sum()
                    #     df["IS_MAIN"] = df.apply(lambda x: x["SO_HD"][:3] == x["MA_DVI"], axis=1)
                    #     df = df[df["IS_MAIN"]]
                    #     df.drop('IS_MAIN', axis = 1, inplace = True)

                    #     if diagnostics:
                    #         print(f"Step 2 - Adjust for Internal Coinsurance\n   -Removed {(_nrows_bf2 - df.shape[0]):,.0f} Rows\n   -Change in Tot Revenue = {(_rev_bf2 - df['PHI_BH'].sum()):,.0f} ({((_rev_bf2 - df['PHI_BH'].sum())/_rev_bf2*100):,.0f}%)")

                    #     """ Step 3 - Remove the rest of the Dups """ 
                    #     _nrows_bf3 = df.shape[0] 
                    #     _rev_bf3 = df['PHI_BH'].sum()
                    #     df = df[~df.duplicated(subset = ['NGAY_HL', 'SO_GCN', 'SO_HD', 'STBH'])]
        
                    #     if diagnostics:
                    #         print(f"Step 3 - Remove Rest of Duplicates\n   -Removed {(_nrows_bf3 - df.shape[0]):,.0f} Rows\n   -Change in Tot Revenue = {(_rev_bf3 - df['PHI_BH'].sum()):,.0f} ({((_rev_bf3 - df['PHI_BH'].sum())/_rev_bf3*100):,.0f}%)")
                        
                    
                    
                    
                    
                    """ REMOVE ROWs WITH MISSING EFF DATE """
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemove Rows Missing NGAY_HL:")    
                    rows_b4 = df.shape[0]    
                    df = df[df['NGAY_HL'].notna()]
                    if diagnostics:
                        print(f'   Removed: {(rows_b4 - df.shape[0]):,.0f} Rows, ({((rows_b4 - df.shape[0])/rows_b4*100):.2f}%)')
                    
                    
                    
                    
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
                        replaced = (col_copy != df[col]).sum()
                        if (replaced > 0) & diagnostics:
                            print(f"   Converted {replaced} values in {col}")
                    
                    del col_copy
                    
                    
                    """ PRINT EFF_YEAR COUNTS IN EACH DF"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nEff Year Count:")
                    df['NAM_HL'] = df['NGAY_HL'].dt.year 
                    if dup_year & diagnostics:
                        print(f"Effective Year Count in {file}: {df['NAM_HL'].value_counts()}")
                    elif diagnostics:
                        print(f"Effective Year Count in CY{year}: {df['NAM_HL'].value_counts()}")
                    
                    
                    """ SAVE DF TO GLOBAL VARIABLE"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nSaving DF:")
                    # Assign DataFrame to a global variable dynamically using the year
                    if dup_year:
                        df_name = f'{file}'
                    else:    
                        df_name = f'df_rev_{year}'
                    globals()[df_name] = df
                    global_df_names.append(df_name)
                    if dup_year & diagnostics:
                        print(f"Summary of {file}:\n   -NUM POLS = {df.shape[0]:,.0f}\n   -TOTAL REVENUE = {df['PHI_BH'].sum():,.0f}")
                    elif diagnostics:    
                        print(f"Summary of CY{year}:\n   -NUM POLS = {df.shape[0]:,.0f}\n   -TOTAL REVENUE = {df['PHI_BH'].sum():,.0f}")
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
    df_rev = pd.concat(all_dataframes, ignore_index=True)
    print(f"   -NUM POLS = {df_rev.shape[0]:,.0f}\n   -TOTAL REVENUE = {df_rev['PHI_BH'].sum():,.0f}")
    
    print("==========================================================================\n==========================================================================")
    for name in global_df_names:
        del globals()[name]
        
    global_df_names.clear()
    
    return df_rev