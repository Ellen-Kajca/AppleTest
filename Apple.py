#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 16:22:33 2024

@author: ellenkajca
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
file_path = 'apple_quality.csv'  # Update the path if necessary
data = pd.read_csv(file_path)

# Streamlit app
st.title('Apple Quality Visualization App')

# User inputs for selecting qualities
quality1 = st.selectbox('Select the first quality to compare:', data.columns[:-1], index=3)  # Default to 'Sweetness'
quality2 = st.selectbox('Select the second quality to compare:', data.columns[:-1], index=4)  # Default to 'Crunchiness'

# Plotting
st.write(f"Interactive Scatter Plot comparing {quality1} and {quality2}")
fig = px.scatter(data, x=quality1, y=quality2, color='Quality', title=f"{quality1} vs {quality2}")
st.plotly_chart(fig)

# Display data (optional)
if st.checkbox('Show raw data'):
    st.write(data)
