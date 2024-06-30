import streamlit as st
import pandas as pd
import numpy as np

st.title("This is my streamlit app")

name = st.text_input("Enter your name")
age = st.slider("Select your age", 0, 100, 25)

if name:
    st.write(f"Hello ! {name}")
    st.write(f"You are {age} years old")

else:
    st.write("Please enter your name")

data = pd.DataFrame({'column1': np.random.randn(10), 'column2':np.random.randn(10)})

st.write("This is the dataframe")
st.write(data)