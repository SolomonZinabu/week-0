import pandas as pd
from scipy.stats import zscore
def summarize_data(df):
    return df.describe(include='all')

def data_quality_check(df):
    missing_values = df.isnull().sum()
    negative_values = (df.select_dtypes(include='number') < 0).sum()
    return missing_values, negative_values
