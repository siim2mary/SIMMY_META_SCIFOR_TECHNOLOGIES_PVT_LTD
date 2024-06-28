import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.data_processing import load_data, preprocess_data
from utils.visualization import plot_data
import config

DATA_PATH = "data/sample_data.csv"

def plot_data(data):
    fig, ax = plt.subplots()
    ax.plot(data['processed_column'])
    st.pyplot(fig)

def main():
    st.title("My streamlit app")

    data = load_data(config.DATA_PATH)
    processed_data = preprocess_data(data)

    #display data
    st.subheader("Processed data")
    st.write(processed_data.head())

    #plot data
    st.subheader("Data plot")
    plot_data(processed_data)

if __name__ == '__main__':
    main()