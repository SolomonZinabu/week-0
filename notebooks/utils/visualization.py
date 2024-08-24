import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
# Time Series Analysis
def plot_time_series(df_dict, columns, titles):
    for country, df in df_dict.items():
        if 'Timestamp' in df.columns:
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            for column, title in zip(columns, titles):
                plt.figure(figsize=(12, 6))
                plt.plot(df['Timestamp'], df[column])
                plt.title(f'{country} - {title}')
                plt.xlabel('Time')
                plt.ylabel(column)
                plt.show()
        else:
            print(f"Column 'Timestamp' not found in {country} dataset.")


# Cleaning Impact Analysis
def cleaning_impact_plot(df, column, country):
    plt.figure(figsize=(12, 6))
    plt.scatter(df[df['Cleaning'] == 1]['Timestamp'], df[df['Cleaning'] == 1][column], color='blue', label='Cleaning')
    plt.scatter(df[df['Cleaning'] == 0]['Timestamp'], df[df['Cleaning'] == 0][column], color='red', label='No Cleaning')
    plt.title(f'{country} - Cleaning Impact on {column}')
    plt.xlabel('Time')
    plt.ylabel(column)
    plt.legend()
    plt.show()

# Correlation Analysis
def correlation_analysis_plot(df, country):
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    plt.figure(figsize=(12, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title(f'{country} - Correlation Matrix')
    plt.show()

# Wind Analysis
def wind_analysis_plot(df, country):
    plt.figure(figsize=(12, 6))
    plt.scatter(df['WD'], df['WS'])
    plt.title(f'{country} - Wind Speed vs Wind Direction')
    plt.xlabel('Wind Direction')
    plt.ylabel('Wind Speed')
    plt.show()

# Temperature Analysis
def temperature_analysis_plot(df, country):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df['Tamb'], label='Tamb')
    plt.plot(df['Timestamp'], df['TModA'], label='TModA')
    plt.plot(df['Timestamp'], df['TModB'], label='TModB')
    plt.title(f'{country} - Temperature Over Time')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.show()

# Histogram Analysis
def histograms_plot(df, columns, country):
    df[columns].hist(figsize=(15, 10), bins=20)
    plt.suptitle(f'{country} - Histograms')
    plt.show()

# Z-Score Analysis
def z_score_analysis_plot(df, column, country):
    df['zscore'] = zscore(df[column].dropna())
    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df['zscore'])
    plt.axhline(y=3, color='r', linestyle='--')
    plt.title(f'{country} - Z-Score Analysis for {column}')
    plt.xlabel('Time')
    plt.ylabel('Z-Score')
    plt.show()

# Bubble Chart
def bubble_chart_plot(df, x_col, y_col, size_col, color_col, country):
    plt.figure(figsize=(12, 6))
    plt.scatter(df[x_col], df[y_col], s=df[size_col]*10, c=df[color_col], cmap='viridis', alpha=0.5)
    plt.colorbar(label=color_col)
    plt.title(f'{country} - Bubble Chart')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()
