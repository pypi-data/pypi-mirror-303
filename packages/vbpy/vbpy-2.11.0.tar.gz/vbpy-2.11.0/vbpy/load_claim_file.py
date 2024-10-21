import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None) 
pd.set_option('display.max_columns', None)  
import os
import re
from tqdm import tqdm

def load_claim_auto(directory, skip_rows=13, lhnv = None, dup_year = False, diagnostics = True):
    # Regular expression to find a four-digit year in the file name
    year_pattern = re.compile(r'\b(\d{4})\b')

    # List to keep track of the names of the DataFrames stored as globals
    global_df_names = []

    # Iterate through each file in the specified directory
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
                    df_clm_dict = {
                        'mã đơn vị quản lý': 'MA_DVI',
                        'Mã đơn vị xử lý': 'MA_DVI_XL',
                        'Mã khai thác': 'MA_KT',
                        'Mã khách hàng': 'MA_KH',
                        'Số hồ sơ': 'SO_HSBT',
                        'Ngày mở HSBT': 'NGAY_MO_HSBT',
                        'Ngày thông báo': 'NGAY_THONG_BAO',
                        'Ngày xảy ra': 'NGAY_XAY_RA',
                        'Số ngày tồn': 'SO_NGAY_TON',
                        'Ngày giải quyết': 'NGAY_GIAI_QUYET',
                        'Phòng': 'PHONG_BT',
                        'Cán bộ bồi thường': 'CAN_BO_BT',
                        'Nghiệp vụ': 'MA_LHNV',
                        'Tên LHNV': 'TEN_LHNV',
                        'Số hợp đồng': 'SO_HD',
                        'Tên khách hàng': 'TEN_KH',
                        'Địa chỉ': 'DIA_CHI',
                        'Nguồn KT': 'NGUON_KT',
                        'Số GCN': 'SO_GCN',
                        'Biển xe': 'SO_BIEN_XE',
                        'Số khung/Số máy': 'SO_KHUNG/SO_MAY',
                        'Đối tượng bảo hiểm': 'TEN_DTBH',
                        'Tuổi xe': 'TUOI_XE',
                        'Ngày cấp': 'NGAY_CAP',
                        'Ngày HL': 'NGAY_HL',
                        'Ngày KT': 'NGAY_KT',
                        'Mã NT': 'MA_NGUYEN_TE',
                        'Số tiền bảo hiểm': 'STBH',
                        'Phí bảo hiểm VNĐ': 'PHI_BH',
                        'Nhóm': 'NHOM_XE', 
                        'Loại xe': 'LOAI_XE',
                        'Nguyên nhân': 'NGUYEN_NHAN_BT',
                        'Số tiền tổn thất': 'STTT',
                        'Số tiền bồi thường': 'STBT', 
                        'Ngày thanh toán bồi thường': 'NGAY_TT_BT',
                        'Gara': 'GARA',
                        'Hạch toán': 'HACH_TOAN',
                        'Ghi chú': 'GHI_CHU'
                    }

                    df.rename(columns={col: df_clm_dict[col] for col in df.columns if col in df_clm_dict}, inplace=True)

                            
                    """ REMOVE UNNECESSARY COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
                    removed_cols = [
                        'Lĩnh vực kinh doanh',
                        'Cán bộ cấp đơn',
                        'Tổng giảm trừ', 
                        'STT',
                        'Số CV KN',
                        'Ngày hồ sơ đầy đủ', 
                        'Khu vực', 
                        'Điện thoại', 
                        'Danh mục cơ sở', 
                        'Email', 
                        'Số tiền bảo hiểm đưa vào tái',  
                        'Ngày thanh toán phí',
                        'Kiểu ĐBH', 
                        'Tỷ lệ ĐBH', 
                        'Thu đòi đồng BH', 
                        'Tỷ lệ tái CĐ', 
                        'Thu đòi tái bảo hiểm CĐ', 
                        'Tỷ lệ tái TT', 
                        'Thu đòi tái bảo hiểm TT',
                        'Giảm trừ tỷ lệ bảo hiểm',
                        'Giảm trừ khấu hao',
                        'Giảm trừ chế tài',
                        'Giảm trừ khác',
                        'Miễn thường',
                        'Thu hồi bồi thường',
                        'Phí giám định'
                    ]

                    # Removing columns, check if the columns exist
                    for col in removed_cols:
                        if col in df.columns:
                            df.drop(columns=col, inplace=True)
                        elif diagnostics:
                            print(f"   Column {col} not found in DataFrame.")                       


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


                    # """ SEPARATE SO MAY and SO KHUNG"""
                    # print("--------------------------------------------------------------------------\nSeparating SO MAY/SO KHUNG:")
                    # df['SO_KHUNG/SO_MAY'].fillna('/')
                    # def get_part(x, index):
                    #     parts = x.split('/')
                    #     return parts[index] if len(parts) > index else np.nan

                    # # Apply this function to create the new columns
                    # df['SO_KHUNG'] = df['SO_KHUNG/SO_MAY'].apply(lambda x: get_part(x, 0))
                    # df['SO_MAY'] = df['SO_KHUNG/SO_MAY'].apply(lambda x: get_part(x, 1))
                    # df.drop('SO_KHUNG/SO_MAY', axis = 1, inplace = True)
                    
                    
                    """ CONVERT DATE COLUMNS""" 
                    if diagnostics:          
                        print("--------------------------------------------------------------------------\nReformatting Date Cols:")
                    dates_columns = [
                        "NGAY_MO_HSBT",
                        "NGAY_THONG_BAO",
                        "NGAY_XAY_RA",
                        "NGAY_GIAI_QUYET",
                        "NGAY_CAP",
                        "NGAY_HL",
                        "NGAY_KT",
                        "NGAY_TT_BT"
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
                        'STTT',
                        'STBT'
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
                    # print("--------------------------------------------------------------------------\nProcessing Dup/Coins Rows:")
                    # """ Step 1 - Remove Duplicated Transactions and Aggregate """
                    # _nrows_bf1 = df.shape[0]
                    # _clms_bf1 = df['STBT'].sum()
                    # # Identify duplicates that need to be summed
                    # duplicates_to_sum = df.duplicated(subset=['MA_DVI', 'SO_HSBT', 'STBT'], keep=False)
                    # df_duplicates = df[duplicates_to_sum]

                    # # Aggregate the data for duplicates
                    # df_agg = df_duplicates.groupby(['MA_DVI', 'SO_HSBT']).agg({
                    #     'STBT': 'sum'
                    # }).reset_index()

                    # # Remove the original duplicated rows from df
                    # df = df[~duplicates_to_sum]

                    # # Append aggregated results back to the main DataFrame
                    # df = pd.concat([df, df_agg], ignore_index=True)

                    # print(f"Step 1 - Remove Duplicates\n   -Removed {(_nrows_bf1 - df.shape[0]):,.0f} Rows\n   -Change in Tot Claims = {(_clms_bf1 - df['STBT'].sum()):,.0f} ({((_clms_bf1 - df['STBT'].sum())/_clms_bf1*100):,.0f}%)")

                    # """ Step 2 - Aggregate Claims with Multiple Transactions into One"""  # Policies with same Claim ID, department ID, and different Claim amounts 
                    # _nrows_bf2 = df.shape[0]
                    # _clms_bf2 = df['STBT'].sum()
                    # df['HACH_TOAN'] = df['HACH_TOAN'].astype(bool)
                    # df_many_trans = df[df.duplicated(subset=['MA_DVI', 'SO_HSBT'], keep = False)]
                    # df_many_trans_agg = df_many_trans.groupby(by = 'SO_HSBT')[['STBT']].sum()
                    # _many_trans_chuaht = df.duplicated(subset=['MA_DVI', 'SO_HSBT'], keep = False) & ~df["HACH_TOAN"]

                    # df = df[~_many_trans_chuaht] # Bo nhung dong trung va chua HT (giu da HT lam cot chinh)

                    # for index, row in df_many_trans_agg.iterrows():
                    #     SO_HSBT = index
                    #     STBT = row['STBT']

                    #     df.loc[df['SO_HSBT'] == SO_HSBT, ['STBT']] = STBT

                    # print(f"Step 2 - Adjust for Multiple Claims\n   -Removed {(_nrows_bf2 - df.shape[0]):,.0f} Rows\n   -Change in Tot Claims = {(_clms_bf2 - df['STBT'].sum()):,.0f} ({((_clms_bf2 - df['STBT'].sum())/_clms_bf2*100):,.0f}%)")

                    # """ Step 3 - Aggregate Claims with Internal Coinsurance into One """  # Poclies with same Claim ID, different Department ID
                    # _nrows_bf3 = df.shape[0]
                    # _clms_bf3 = df['STBT'].sum()
                    # df["IS_MAIN"] = df.apply(lambda x: x["SO_HSBT"][:3] == x["MA_DVI"], axis=1)

                    # df_many_qly = df[df.duplicated(subset=['SO_HSBT'], keep = False)]
                    # df_many_qly_agg = df_many_qly.groupby(by = 'SO_HSBT')[['STBT']].sum()
                    # _many_qly_notmain = df.duplicated(subset=['SO_HSBT'], keep = False) & ~df["IS_MAIN"]

                    # df = df[~_many_qly_notmain] # Bo nhung dong trung va khong phai dvi qly chinh 

                    # for index, row in df_many_qly_agg.iterrows():
                    #     SO_HSBT = index
                    #     STBT = row['STBT']

                    #     df.loc[df['SO_HSBT'] == SO_HSBT, ['STBT']] = STBT

                    # print(f"Step 3 - Adjust for Internal Insurance\n   -Removed {(_nrows_bf3 - df.shape[0]):,.0f} Rows\n   -Change in Tot Claims = {(_clms_bf3 - df['STBT'].sum()):,.0f} ({((_clms_bf3 - df['STBT'].sum())/_clms_bf3*100):,.0f}%)")

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
                        "Xe cứu thương": "NHOM.2C",
                        "Xe cứu hộ": "NHOM.2C",

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
                        print("--------------------------------------------------------------------------\nRemoving Rows Missing NGAY_HL:")    
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
                    
                    
                    """ PRINT EFF_YEAR COUNTS IN EACH DF"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nEff Year Count:")
                    df['NAM_HL'] = df['NGAY_HL'].dt.year 
                    if dup_year & diagnostics:
                        print(f"Effective Year Count in {file}: {df['NAM_HL'].value_counts()}")
                    elif diagnostics:    
                        print(f"Effective Year Count in CY{year}: {df['NAM_HL'].value_counts()}")
                        
                                      
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
                    df_name = f'{file}'
                    globals()[df_name] = df
                    global_df_names.append(df_name)
                    if dup_year & diagnostics:
                        print(f"Summary of {file}:\n   -NUM CLAIMS = {df.shape[0]:,.0f}\n   -TOTAL CLAIMS = {df['STBT'].sum():,.0f}")
                    elif diagnostics:
                        print(f"Summary of CY{year}:\n   -NUM CLAIMS = {df.shape[0]:,.0f}\n   -TOTAL CLAIMS = {df['STBT'].sum():,.0f}")
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
    df_clm = pd.concat(all_dataframes, ignore_index=True)
    print(f"   Total Rows = {df_clm.shape[0]:,.0f}\n   Total Claims = {df_clm['STBT'].sum():,.0f}")
    
    print("==========================================================================\n==========================================================================")
    for name in global_df_names:
        del globals()[name]
        
    global_df_names.clear()
    
    return df_clm

def load_claim_property(directory, skip_rows=13, lhnv = None, dup_year = False, diagnostics = True):
    # Regular expression to find a four-digit year in the file name
    year_pattern = re.compile(r'\b(\d{4})\b')

    # List to keep track of the names of the DataFrames stored as globals
    global_df_names = []

    # Iterate through each file in the specified directory
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
                    df_clm_dict = {
                        'mã đơn vị quản lý': 'MA_DVI',
                        'Mã đơn vị xử lý': 'MA_DVI_XL',
                        'Số hồ sơ': 'SO_HSBT',
                        'Ngày mở HSBT': 'NGAY_MO_HSBT',
                        'Ngày thông báo': 'NGAY_THONG_BAO',
                        'Ngày xảy ra': 'NGAY_XAY_RA',
                        'Số ngày tồn': 'SO_NGAY_TON',
                        'Ngày giải quyết': 'NGAY_GIAI_QUYET',
                        'Phòng': 'PHONG_BT',
                        'Cán bộ bồi thường': 'CAN_BO_BT',
                        'Nghiệp vụ': 'MA_LHNV',
                        'Tên LHNV': 'TEN_LHNV',
                        'Số hợp đồng': 'SO_HD',
                        'Tên khách hàng': 'TEN_KH',
                        'Mã khai thác': 'MA_KT',
                        'Mã khách hàng': 'MA_KH',
                        'Địa chỉ': 'DIA_CHI',
                        'Nguồn KT': 'NGUON_KT',
                        'Đối tượng bảo hiểm': 'LOAI_TS',
                        'Ngày cấp': 'NGAY_CAP',
                        'Ngày HL': 'NGAY_HL',
                        'Ngày KT': 'NGAY_KT',
                        'Mã NT': 'MA_NGUYEN_TE',
                        'Số tiền bảo hiểm': 'STBH',
                        'Phí bảo hiểm VNĐ': 'PHI_BH',
                        'Nhóm': 'NHOM_TS', 
                        'Nguyên nhân': 'NGUYEN_NHAN_BT',
                        'Số tiền tổn thất': 'STTT',
                        'Số tiền bồi thường': 'STBT', 
                        'Ngày thanh toán bồi thường': 'NGAY_TT_BT',
                        'Hạch toán': 'HACH_TOAN',
                        'Ghi chú': 'GHI_CHU'

                    }

                    df.rename(columns={col: df_clm_dict[col] for col in df.columns if col in df_clm_dict}, inplace=True)

                            
                    """ REMOVE UNNECESSARY COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
                    removed_cols = [
                        'Gara',
                        'Loại xe',
                        'Biển xe',
                        'Tuổi xe',
                        'Số GCN',
                        'Số khung/Số máy',
                        'Lĩnh vực kinh doanh',
                        'Cán bộ cấp đơn',
                        'Tổng giảm trừ', 
                        'STT',
                        'Số CV KN',
                        'Ngày hồ sơ đầy đủ', 
                        'Khu vực', 
                        'Điện thoại', 
                        'Danh mục cơ sở', 
                        'Email', 
                        'Số tiền bảo hiểm đưa vào tái',  
                        'Ngày thanh toán phí',
                        'Kiểu ĐBH', 
                        'Tỷ lệ ĐBH', 
                        'Thu đòi đồng BH', 
                        'Tỷ lệ tái CĐ', 
                        'Thu đòi tái bảo hiểm CĐ', 
                        'Tỷ lệ tái TT', 
                        'Thu đòi tái bảo hiểm TT',
                        'Giảm trừ tỷ lệ bảo hiểm',
                        'Giảm trừ khấu hao',
                        'Giảm trừ chế tài',
                        'Giảm trừ khác',
                        'Miễn thường',
                        'Thu hồi bồi thường',
                        'Phí giám định'
                    ]

                    # Removing columns, check if the columns exist
                    for col in removed_cols:
                        if col in df.columns:
                            df.drop(columns=col, inplace=True)
                        elif diagnostics:
                            print(f"   Column {col} not found in DataFrame.")                       


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
                        "NGAY_MO_HSBT",
                        "NGAY_THONG_BAO",
                        "NGAY_XAY_RA",
                        "NGAY_GIAI_QUYET",
                        "NGAY_CAP",
                        "NGAY_HL",
                        "NGAY_KT",
                        "NGAY_TT_BT"
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
                        'STTT',
                        'STBT'
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
                        print("--------------------------------------------------------------------------\nRemoving Rows Missing NGAY_HL:")    
                    rows_b4 = df.shape[0]    
                    df = df[df['NGAY_HL'].notna()]
                    if diagnostics:
                        print(f'   Removed: {(rows_b4 - df.shape[0]):,.0f} Rows, ({((rows_b4 - df.shape[0])/rows_b4*100):.2f}%)')
                    
                    
                    
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
                    df_name = f'{file}'
                    globals()[df_name] = df
                    global_df_names.append(df_name)
                    if dup_year & diagnostics:
                        print(f"Summary of {file}:\n   -NUM CLAIMS = {df.shape[0]:,.0f}\n   -TOTAL CLAIMS = {df['STBT'].sum():,.0f}")
                    elif diagnostics:
                        print(f"Summary of CY{year}:\n   -NUM CLAIMS = {df.shape[0]:,.0f}\n   -TOTAL CLAIMS = {df['STBT'].sum():,.0f}")
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
    df_clm = pd.concat(all_dataframes, ignore_index=True)
    print(f"   Total Rows = {df_clm.shape[0]:,.0f}\n   Total Claims = {df_clm['STBT'].sum():,.0f}")
    
    print("==========================================================================\n==========================================================================")
    for name in global_df_names:
        del globals()[name]
        
    global_df_names.clear()
    
    return df_clm

def load_claim_marine(directory, skip_rows=13, lhnv = None, dup_year = False, diagnostics = True):
    # Regular expression to find a four-digit year in the file name
    year_pattern = re.compile(r'\b(\d{4})\b')

    # List to keep track of the names of the DataFrames stored as globals
    global_df_names = []

    # Iterate through each file in the specified directory
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
                    df_clm_dict = {
                        'mã đơn vị quản lý': 'MA_DVI',
                        'Mã đơn vị xử lý': 'MA_DVI_XL',
                        'Số hồ sơ': 'SO_HSBT',
                        'Ngày mở HSBT': 'NGAY_MO_HSBT',
                        'Ngày thông báo': 'NGAY_THONG_BAO',
                        'Ngày xảy ra': 'NGAY_XAY_RA',
                        'Số ngày tồn': 'SO_NGAY_TON',
                        'Ngày giải quyết': 'NGAY_GIAI_QUYET',
                        'Phòng': 'PHONG_BT',
                        'Cán bộ bồi thường': 'CAN_BO_BT',
                        'Nghiệp vụ': 'MA_LHNV',
                        'Tên LHNV': 'TEN_LHNV',
                        'Số hợp đồng': 'SO_HD',
                        'Tên khách hàng': 'TEN_KH',
                        'Mã khai thác': 'MA_KT',
                        'Mã khách hàng': 'MA_KH',
                        'Địa chỉ': 'DIA_CHI',
                        'Nguồn KT': 'NGUON_KT',
                        'Đối tượng bảo hiểm': 'LOAI_HH',
                        'Ngày cấp': 'NGAY_CAP',
                        'Ngày HL': 'NGAY_HL',
                        'Ngày KT': 'NGAY_KT',
                        'Mã NT': 'MA_NGUYEN_TE',
                        'Số tiền bảo hiểm': 'STBH',
                        'Phí bảo hiểm VNĐ': 'PHI_BH',
                        'Nguyên nhân': 'NGUYEN_NHAN_BT',
                        'Số tiền tổn thất': 'STTT',
                        'Số tiền bồi thường': 'STBT', 
                        'Kiểu ĐBH': 'KIEU_DBH',
                        'Tỷ lệ ĐBH': 'TI_LE_DBH', 
                        'Thu đòi đồng BH': 'THU_DBH', 
                        'Ngày thanh toán bồi thường': 'NGAY_TT_BT',
                        'Hạch toán': 'HACH_TOAN',
                        'Ghi chú': 'GHI_CHU'

                    }

                    df.rename(columns={col: df_clm_dict[col] for col in df.columns if col in df_clm_dict}, inplace=True)

                            
                    """ REMOVE UNNECESSARY COLUMNS"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nRemoving Unneeded Columns:")
                    removed_cols = [
                        'Nhóm', 
                        'Gara',
                        'Loại xe',
                        'Biển xe',
                        'Tuổi xe',
                        'Số GCN',
                        'Số khung/Số máy',
                        'Lĩnh vực kinh doanh',
                        'Cán bộ cấp đơn',
                        'Tổng giảm trừ', 
                        'STT',
                        'Số CV KN',
                        'Ngày hồ sơ đầy đủ', 
                        'Khu vực', 
                        'Điện thoại', 
                        'Danh mục cơ sở', 
                        'Email', 
                        'Số tiền bảo hiểm đưa vào tái',  
                        'Ngày thanh toán phí',
                        'Tỷ lệ tái CĐ', 
                        'Thu đòi tái bảo hiểm CĐ', 
                        'Tỷ lệ tái TT', 
                        'Thu đòi tái bảo hiểm TT',
                        'Giảm trừ tỷ lệ bảo hiểm',
                        'Giảm trừ khấu hao',
                        'Giảm trừ chế tài',
                        'Giảm trừ khác',
                        'Miễn thường',
                        'Thu hồi bồi thường',
                        'Phí giám định'
                    ]

                    # Removing columns, check if the columns exist
                    for col in removed_cols:
                        if col in df.columns:
                            df.drop(columns=col, inplace=True)
                        elif diagnostics:
                            print(f"   Column {col} not found in DataFrame.")                       


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
                        "NGAY_MO_HSBT",
                        "NGAY_THONG_BAO",
                        "NGAY_XAY_RA",
                        "NGAY_GIAI_QUYET",
                        "NGAY_CAP",
                        "NGAY_HL",
                        "NGAY_KT",
                        "NGAY_TT_BT"
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
                        'STTT',
                        'STBT'
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

                        
                    
                    """ SAVE DF TO GLOBAL VARIABLE"""
                    if diagnostics:
                        print("--------------------------------------------------------------------------\nSaving DF:")
                    # Assign DataFrame to a global variable dynamically using the year
                    df_name = f'{file}'
                    globals()[df_name] = df
                    global_df_names.append(df_name)
                    if dup_year & diagnostics:
                        print(f"Summary of {file}:\n   -NUM CLAIMS = {df.shape[0]:,.0f}\n   -TOTAL CLAIMS = {df['STBT'].sum():,.0f}")
                    elif diagnostics:
                        print(f"Summary of CY{year}:\n   -NUM CLAIMS = {df.shape[0]:,.0f}\n   -TOTAL CLAIMS = {df['STBT'].sum():,.0f}")
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
    df_clm = pd.concat(all_dataframes, ignore_index=True)
    print(f"   Total Rows = {df_clm.shape[0]:,.0f}\n   Total Claims = {df_clm['STBT'].sum():,.0f}")
    
    print("==========================================================================\n==========================================================================")
    for name in global_df_names:
        del globals()[name]
        
    global_df_names.clear()
    
    return df_clm

