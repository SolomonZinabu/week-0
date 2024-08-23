import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    return pd.read_csv('../data/benin-malanville.csv')


def main():
    st.title("Solar Farm Data Dashboard")
    data = load_data()
    
    st.sidebar.header('User Input')
    selected_metric = st.sidebar.selectbox('Select Metric', ['GHI', 'DNI', 'DHI'])

    if selected_metric:
        st.write(f"### {selected_metric} Over Time")
        st.line_chart(data[selected_metric])

if __name__ == "__main__":
    main()
