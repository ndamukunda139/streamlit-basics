#Import libraries 

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# Start our spp
st.title("Introduction on Streamlit Web app")

# Add a header
st.header("Basics of text in Streamlit header")
# Add a subheader
st.subheader("Basic subheader") 

#Add markdown
st.markdown("""
## This is a simple list
            - Python basics
            - Machine learning
            - Deep learning
            - Model deployment """)


st.write("Once installed, run streamlit using command ' streamlit hello' in the terminal")
st.caption("This is a simple equation")
st.latex(r'st = \frac{1}{2}gt^2')


# Dipsplay Dataframes
st.header("Iris Dataset")
st.subheader("Iris Dataset Dataframe Sample")

# Load the iris dataset
df = sns.load_dataset("iris")

# Display the first 5 rows of the dataset
st.dataframe(df.head())

# Tables
st.subheader("Iris Dataset Table Sample")
st.table(df.head())