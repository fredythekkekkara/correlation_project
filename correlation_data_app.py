import streamlit as st
import pandas as pd
import numpy as np

st.title('Correlation of Total electron content in ionosphere with solar forcing parameters')

add_selectbox = st.sidebar.selectbox(
    'Process Line',
    ("Data Configuration", "Data Cleaning & Formatting", "Computations", "Data Visualisation")
)
print(add_selectbox)