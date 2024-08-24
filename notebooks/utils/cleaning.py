from scipy.stats import zscore
import pandas as pd

def clean_data(df):
    df = df.dropna(axis=1, how='all').copy()
    
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = df[column].fillna('Unknown')
        else:
            df[column] = df[column].ffill()
    
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df = df[(zscore(df[numeric_cols]) < 3).all(axis=1)].copy()
    
    df = df.drop_duplicates().copy()
    
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    
    return df
