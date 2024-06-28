import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title("Interactive Data Analysis with Streamlit")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

    if uploaded_file is not None:
        # Read data from CSV file
        data = pd.read_csv(uploaded_file)

        # Display raw data
        st.subheader("Raw Data")
        st.write(data)

        # Basic statistics
        st.subheader("Basic Statistics")
        st.write(data.describe())

        # Data manipulation example: filtering
        st.subheader("Filtered Data Example")
        # Example: filtering data where 'Sales' > 500
        filtered_data = data[data['Sales'] > 500]
        st.write(filtered_data)

        # Interactive widgets example: scatter plot
        st.subheader("Interactive Plot")
        x_axis = st.selectbox("Select x-axis data", data.columns)
        y_axis = st.selectbox("Select y-axis data", data.columns)

        # Create scatter plot based on user selection
        fig, ax = plt.subplots()
        ax.scatter(data[x_axis], data[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)

        # Data export example
        st.subheader("Export Filtered Data")
        if st.button("Export Filtered Data to CSV"):
            filtered_data.to_csv("filtered_data.csv", index=False)
            st.success("Filtered data exported successfully.")

if __name__ == "__main__":
    main()
