import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import statistics as sta
    # Page title
st.markdown("<h1><center>📈 AnalytiXplorer</center></h1>",unsafe_allow_html = True)

    # Uploading file from user input
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        columns = df.columns.tolist()

        st.write("")
        st.write(df.head())

        col1,col2 = st.columns(2)
        with col1:
             x_axis = st.selectbox("Select the Column for X-axis", options=columns + ["None"], index=None)
        with col2:
             y_axis = st.selectbox("Select the Column for Y-axis", options=columns + ["None"], index=None)

        plot_list = ["Line Plot", "Bar Chart", "Scatter Plot", "Distribution Plot"]
        selected_plot = st.selectbox("Select the Plot type", options=plot_list, index=None)

        if st.button("Generate Plot"):
            fig, ax = plt.subplots(figsize=(6, 4))

            if selected_plot == "Line Plot":
                sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif selected_plot == "Bar Chart":
                sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif selected_plot == "Scatter Plot":
                sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif selected_plot == "Distribution Plot":
                sns.histplot(x=df[x_axis], y=df[y_axis], kde=True, ax=ax)
            
            # Adjust label size
            ax.tick_params(axis="x", labelsize=10)
            ax.tick_params(axis="y", labelsize=10)
        
            plt.title(f"{selected_plot} of {x_axis} and {y_axis}", fontsize=12)
            plt.xlabel(x_axis, fontsize=10)
            plt.ylabel(y_axis, fontsize=10)
        
            st.pyplot(fig)

            col1,col2 = st.columns(2)

            with col1:
                 st.subheader(x_axis)
                 st.write("Mean of the",x_axis,np.mean(df[x_axis]))
                 st.write("Median of the",x_axis,np.median(df[x_axis]))
                 st.write("Mode of the",x_axis,sta.mode(df[x_axis]))
                 st.write("SD of the",x_axis,np.std(df[x_axis]))
            with col2:
                 st.subheader(y_axis)
                 st.write("Mean of the",y_axis,np.mean(df[y_axis]))
                 st.write("Median of the",y_axis,np.median(df[y_axis]))
                 st.write("Mode of the",y_axis,sta.mode(df[y_axis]))
                 st.write("SD of the",y_axis,np.std(df[y_axis]))
            st.subheader("Co-relation values")
            st.write(df[x_axis].corr(df[y_axis]))
