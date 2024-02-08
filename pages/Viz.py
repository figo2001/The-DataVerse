import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import os

# Set page configuration
st.set_page_config(page_title="Data Viz",
                   layout='centered',
                   page_icon="📊")

st.title("Data Viz 📊")

# Allow users to upload CSV files
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the uploaded data
    st.write("Uploaded data:")
    st.write(df.head())

    # User selection for the columns
    x_axis = st.selectbox("Select the x-axis", options=df.columns.tolist()+['None'], index=None)
    y_axis = st.selectbox("Select the y-axis", options=df.columns.tolist()+['None'], index=None)

    plot_list = ["Line Plot", "Bar Chart", "Scatter Plot", "Distribution Plot", "Count Plot"]
    selected_plot = st.selectbox("Select the plot type", options=plot_list, index=None)

    st.write("Selected x-axis: ", x_axis)
    st.write("Selected y-axis: ", y_axis)
    st.write("Selected plot type: ", selected_plot)

    # button to generate plots
    if st.button("Generate Plot"):
        fig, ax = plt.subplots(figsize=(6, 4))

        if selected_plot == 'Line Plot':
            sn.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)

        elif selected_plot == 'Bar Chart':
            sn.barplot(x=df[x_axis], y=df[y_axis], ax=ax)

        elif selected_plot == 'Scatter Plot':
            sn.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)

        elif selected_plot == 'Distribution Plot':
            sn.histplot(df[x_axis], kde=True, ax=ax)

        elif selected_plot == 'Count Plot':
            sn.countplot(x=df[x_axis], ax=ax)

        # adjust labels sizes
        ax.tick_params(axis='x', labelsize=10)
        ax.tick_params(axis='y', labelsize=10)

        # title and axis labels for the plot
        plt.title(f"{selected_plot} of {y_axis} vs {x_axis}", fontsize=12)
        plt.xlabel(x_axis, fontsize=10)
        plt.ylabel(y_axis, fontsize=10)

        st.pyplot(fig)
