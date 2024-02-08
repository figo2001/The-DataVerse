import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import os

# Set page configuration
st.set_page_config(page_title="Data Stats",
                   layout='centered',
                   page_icon="📈")

st.title("Data Stats 📈")

# Allow users to upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)

    # Show the data
    st.subheader("Showing the first five rows")
    st.write(data.head())

    # Show the tail
    st.subheader("Showing the last five rows")
    st.write(data.tail())

    # Show the shape
    st.subheader("Showing the shape of the dataset")
    st.write(data.shape)

    # Show the data types
    st.subheader("Showing the data types of the columns")
    st.write(data.dtypes)

    # Show the summary of the data
    st.subheader("Showing Extra statistics of the data")
    st.write(data.describe())

    # Show the categorical columns
    st.subheader("Showing all the categorical columns")
    cat = data.select_dtypes(include=['object'])
    st.write(cat)

    # Show the numerical columns
    st.subheader("Showing all the numerical columns")
    num = data.select_dtypes(include=['int', 'float'])
    st.write(num)

    # Show the missing values
    st.subheader("Showing the missing values of dataset")
    st.write(data.isnull().sum())

    # Show the duplicate values
    st.subheader("Showing the duplicate values of dataset")
    st.write(data.duplicated().sum())

    # Showing the distribution of the dataset
    st.subheader("Showing the distribution")
    his = data.hist(figsize=(14, 10))
    st.pyplot()

    # Showing the co-relation of the dataset
    st.subheader("Showing the Co-relation")
    htm = sn.heatmap(num.corr(), annot=True)
    st.pyplot()

    # Showing Pie chart and bar chart for the categorical columns
    st.subheader("Showing Pie chart and Bar chart for categorical columns")
    for column in cat:
        # Pie chart
        fig, ax = plt.subplots(1, 2, figsize=(18, 5.5))
        data[column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax[0])
        ax[0].set_title(f'Pie chart for {column}')
        ax[0].set_ylabel('')  # Clear ylabel
        # Bar chart
        sn.countplot(x=column, data=data, ax=ax[1])
        ax[1].set_title(f'Bar chart for {column}')
        st.pyplot(fig)
