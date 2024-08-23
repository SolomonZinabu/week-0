
import streamlit as st
import pandas as pd
from utils.utils import summarize_data, data_quality_check, plot_time_series_all, clean_data

def main():
    st.title("Exploratory Data Analysis (EDA) App")

    # File upload
    uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)

    # Dictionary to hold dataframes
    df_dict = {}

    for uploaded_file in uploaded_files:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        df_dict[uploaded_file.name] = df

    if df_dict:
        st.sidebar.title("EDA Options")
        option = st.sidebar.selectbox("Select EDA Task", ["Summarize Data", "Data Quality Check", "Plot Time Series", "Clean Data"])

        if option == "Summarize Data":
            st.subheader("Summary Statistics")
            for name, df in df_dict.items():
                st.write(f"**{name}**")
                st.write(summarize_data(df))

        elif option == "Data Quality Check":
            st.subheader("Data Quality Check")
            for name, df in df_dict.items():
                st.write(f"**{name}**")
                missing_values, negative_values = data_quality_check(df)
                st.write("Missing Values:\n", missing_values)
                st.write("Negative Values:\n", negative_values)

        elif option == "Plot Time Series":
            st.subheader("Time Series Plots")
            columns = st.multiselect("Select Columns to Plot", options=df_dict[list(df_dict.keys())[0]].columns)
            titles = st.text_input("Enter Titles for Plots (comma-separated)", value="Time Series Plot").split(",")
            if columns and titles:
                for fig in plot_time_series_all(df_dict, columns, titles):
                    if fig:
                        st.pyplot(fig)

        elif option == "Clean Data":
            st.subheader("Cleaned Data")
            for name, df in df_dict.items():
                st.write(f"**{name}**")
                cleaned_df = clean_data(df)
                st.write(cleaned_df.head())

if __name__ == "__main__":
    main()
