# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("Basic Streamlit App Structure")

# Add headers
st.header("Input Section")

# Widgets for user input
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0, 100, 25)
show_data = st.checkbox("Show sample data")

# Logic to process input
if name:
    greeting = f"Hello, {name}! You are {age} years old."
else:
    greeting = "Please enter your name."

# Display greeting
st.subheader("Greeting")
st.write(greeting)

# Conditional display of data
if show_data:
    st.subheader("Sample Data")
    # Generate sample data
    data = pd.DataFrame({
        'A': np.random.randn(10),
        'B': np.random.randn(10)
    })
    st.write(data)
    
    # Simple plot
    st.subheader("Sample Plot")
    fig, ax = plt.subplots()
    ax.plot(data['A'], label='A')
    ax.plot(data['B'], label='B')
    ax.legend()
    st.pyplot(fig)
