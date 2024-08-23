# utils.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Function to summarize data
def summarize_data(df):
    return df.describe(include='all')

# Function for data quality check
def data_quality_check(df):
    missing_values = df.isnull().sum()
    negative_values = df[df.select_dtypes(include='number') < 0].count()
    return missing_values, negative_values

# Function for plotting time series
def plot_time_series_all(df_dict, columns, titles):
    for country, df in df_dict.items():
        if 'Timestamp' in df.columns:
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            for column, title in zip(columns, titles):
                if column in df.columns:
                    plt.figure(figsize=(12, 6))
                    plt.plot(df['Timestamp'], df[column], label=column)
                    plt.title(f'{country} - {title}')
                    plt.xlabel('Time')
                    plt.ylabel(column)
                    plt.legend()
                    plt.close()
                    yield plt
                else:
                    yield None

# Function for cleaning data
def clean_data(df):
    df = df.dropna(axis=1, how='all').copy()
    for column in df.columns:
        if df[column].dtype == 'object':
            df.loc[:, column] = df[column].fillna('Unknown')
        else:
            df.loc[:, column] = df[column].ffill()
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df = df[(zscore(df[numeric_cols]) < 3).all(axis=1)].copy()
    df = df.drop_duplicates().copy()
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    return df
