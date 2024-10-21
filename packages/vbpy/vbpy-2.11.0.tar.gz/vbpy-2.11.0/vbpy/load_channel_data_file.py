import pandas as pd
import numpy as np

def load_channel_data(directory):
    df = pd.read_excel(directory)
    df.drop(df.columns[-2:], axis=1, inplace=True)
    df.rename(columns = {
        'Mã Đại lý': 'MA_DL',
        'Tên Đại lý': 'TEN_DL',
        'Nguồn khai thác': 'NGUON_KT',
        'Phân loại Đại lý': 'LOAI_DL',
        'Thông tin đại lý': 'THONG_TIN_DL'
    }, inplace = True)

    def replace_blanks(x):
        if isinstance(x, str) and x.strip() == '':
            return np.nan
        else:
            return x
                        
    for col in df.columns:
        df[col] = df[col].astype(str)
        col_copy = df[col].copy()
        df[col] = df[col].apply(replace_blanks)
        replaced = (col_copy != df[col]).sum()
        if replaced > 0:
            print(f"   Converted {replaced} values in {col}")
    
    del col_copy

    df.dropna(subset = 'MA_DL', inplace = True)
    
    return df