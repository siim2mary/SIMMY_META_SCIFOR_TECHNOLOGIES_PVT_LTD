import streamlit as st
import numpy as np
import pandas as pd

st.title("MY STREAMLIT APP WITH IMAGE")
st.header("The image")
st.subheader("This is the image of MODI")
st.write("THIS IS MY STREAMLIT APP WITH THE IMAGE OF MODI.I AM DEPLOYING IT WITH STREAMLIT")

st.image("Modi.jpg", caption = "Deployment of Image of MODI using Streamlit", width =200)
st.slider("IMAGE",0,100,25)
st.button("This Streamlit App I have created during Test")
st.markdown("*streamlit* is used to **Deploy**")