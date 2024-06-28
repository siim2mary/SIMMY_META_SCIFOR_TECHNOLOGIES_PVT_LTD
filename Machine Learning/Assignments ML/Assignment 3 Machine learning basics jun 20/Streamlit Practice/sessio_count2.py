import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Simple Streamlit App")

# Text input
name = st.text_input("Enter your name:")

# Slider for age
age = st.slider("Select your age:", 0, 100, 25)

# Display the entered data
if name:
    st.write(f"Hello, {name}!")
    st.write(f"You are {age} years old.")
else:
    st.write("Please enter your name.")

# Sample DataFrame
data = pd.DataFrame({
    'Column 1': np.random.randn(10),
    'Column 2': np.random.randn(10)
})

# Display DataFrame
st.write("Here is a sample DataFrame:")
st.write(data)
