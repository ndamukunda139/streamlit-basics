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

st.latex(r"s \left ( t \right ) = ut + \dfrac{1}{2} at^2")


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


## Add Charts
st.subheader("Area Chart: Sepal Length and sepal Width")
chart_data = df[["sepal_length", "sepal_width"]]
st.area_chart(chart_data)

# Line chart
st.subheader("Line: Sepal Length and sepal Width")
st.line_chart(chart_data)

# Bar chart
st.subheader("Bar Chart: Sepal Length and sepal Width")
st.bar_chart(chart_data)

# scatter plot
st.subheader("Scatter Plot: Sepal Length vs Petal Length")
chart_data1 = df[["sepal_length", "petal_length"]]
st.scatter_chart(chart_data1)

##Create sample matplotlib plot and seaborn in columns
st.subheader("Matplotlib and seaborn Plot")
st.text("This is a simple plot using matplotlib and seaborn")


# Create columns
col1, col2 = st.columns(2)

#Create a sample plot using matplotlib
with col1:
    st.subheader("Matplotlib Plot")
    fig, ax = plt.subplots()
    ax.plot(df["sepal_length"], df["sepal_width"], "o")
    ax.set_xlabel("Sepal Length")
    ax.set_ylabel("Sepal Width")
    st.pyplot(fig)  # equivalent to plt.show(fig)

with col2:
    st.subheader("Seaborn Plot")
    fig, ax = plt.subplots()
    sns.scatterplot(x="sepal_length", y="sepal_width", data=df, ax=ax)
    ax.set_xlabel("Sepal Length")
    ax.set_ylabel("Sepal Width")
    st.pyplot(fig)  # equivalent to plt.show(fig)


# Display executable and non-executable code
st.header("Executable and Non-Executable Code")
st.subheader("Non-Executable Code")
st.code("""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
        
# Load the iris dataset
df = sns.load_dataset("iris")
        
# Display the first 5 rows of the dataset
st.dataframe(df.head())
""", language='python') 


st.code("""
# sample plot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the iris dataset
df = sns.load_dataset("iris")

# Create a sample plot
plt.figure(figsize=(10, 6))
plt.scatter(df["sepal_length"], df["sepal_width"], c=df["species"].astype("category").cat.codes)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Dataset: Sepal Length vs Sepal Width")
plt.show()
""", language="python")


## Executable code
st.subheader("Executable Code")
## Executable plotting Code
st.subheader("Executable Code with Plotting")
with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    st.subheader("Seaborn Plot")
    fig, ax = plt.subplots()
    sns.scatterplot(x="sepal_length", y="sepal_width", data=df, ax=ax)
    ax.set_xlabel("Sepal Length")
    ax.set_ylabel("Sepal Width")
    st.pyplot(fig) # Equivalent to plt.show()
# And now we're back to _not_ printing to the screen
st.write('Done!')   




# Add Button
if st.button("Display bar chart?"):
    st.subheader("Bar Chart: Sepal Length and sepal Width")
    st.bar_chart(chart_data)

#Add checkbox
if st.checkbox("Display bar chart?"):
    st.subheader("Bar Chart: Sepal Length and sepal Width")
    st.bar_chart(chart_data) 


# Add a selectbox
option = st.selectbox(
    'What car do you drive?',
    ['Audi', 'BMW', 'Mercedes', 'Toyota', 'Honda', 'Nissan', 'Ford', 'Chevrolet', 'Volkswagen', 'Hyundai'])
st.write('You selected:', option)

#Add slider
st.subheader("Slider")
st.slider('What is your CC capacity', 
            min_value=500, 
            max_value=5000,
            value=1000,
            step=100,
            format="%d CC")
