import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit App
st.title("Data Visualization App")

# File Uploader
uploaded_file = st.file_uploader("Upload Data (CSV)", type="csv")

# Visualization Type Selector
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Display the number of rows and columns
    st.write(f"Number of rows: {df.shape[0]}")
    st.write(f"Number of columns: {df.shape[1]}")

    st.sidebar.header("Visualization Options")

    # Analyze sample-data types of columns
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_columns = df.select_dtypes(include=['object']).columns

    # Display the columns
    st.sidebar.write("Numeric Columns:")
    st.sidebar.write(numeric_columns)
    st.sidebar.write("Categorical Columns:")
    st.sidebar.write(categorical_columns)

    # Suggest suitable visualizations
    if len(numeric_columns) >= 2:
        visualization_type = st.sidebar.selectbox("Select Visualization Type:", ["Bar Graph", "Line Chart", "Scatter Plot", "Histogram", "Box Plot", "Heatmap", "Pairplot"])
    elif len(numeric_columns) == 1 and len(categorical_columns) >= 1:
        visualization_type = st.sidebar.selectbox("Select Visualization Type:", ["Bar Graph"])
    else:
        st.sidebar.write("Not enough sample-data for visualization")
        visualization_type = None

    if visualization_type:
        # Column selectors based on the visualization type
        if visualization_type in ["Bar Graph", "Line Chart"]:
            x_column = st.sidebar.selectbox("Select X-axis column:", df.columns)
            y_column = st.sidebar.selectbox("Select Y-axis column:", df.columns)
        elif visualization_type == "Scatter Plot":
            x_column = st.sidebar.selectbox("Select X-axis column:", numeric_columns)
            y_column = st.sidebar.selectbox("Select Y-axis column:", numeric_columns)
        elif visualization_type == "Histogram":
            x_column = st.sidebar.selectbox("Select column for Histogram:", numeric_columns)
        elif visualization_type == "Box Plot":
            x_column = st.sidebar.selectbox("Select column for Box Plot:", numeric_columns)
        elif visualization_type == "Heatmap":
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.heatmap(df.corr(), annot=True, ax=ax)
            st.pyplot(fig)
        elif visualization_type == "Pairplot":
            fig = sns.pairplot(df)
            st.pyplot(fig)

        # Additional customization options
        width = st.sidebar.number_input("Width of the chart", min_value=1, max_value=20, value=10)
        height = st.sidebar.number_input("Height of the chart", min_value=1, max_value=20, value=5)

        # Axis scale options
        x_scale = st.sidebar.selectbox("Select X-axis scale:", ["linear"])
        y_scale = st.sidebar.selectbox("Select Y-axis scale:", ["linear"])

        # Submit Button
        if st.sidebar.button("Submit"):
            # Display the selected visualization
            if visualization_type == "Bar Graph":
                fig, ax = plt.subplots(figsize=(width, height))
                df.plot(kind='bar', x=x_column, y=y_column, ax=ax)
                ax.set_xscale(x_scale)
                ax.set_yscale(y_scale)
                plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
                st.pyplot(fig)
            elif visualization_type == "Line Chart":
                fig, ax = plt.subplots(figsize=(width, height))
                df.plot(kind='line', x=x_column, y=y_column, ax=ax)
                ax.set_xscale(x_scale)
                ax.set_yscale(y_scale)
                plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
                st.pyplot(fig)
            elif visualization_type == "Scatter Plot":
                fig, ax = plt.subplots(figsize=(width, height))
                ax.scatter(df[x_column], df[y_column])
                ax.set_xscale(x_scale)
                ax.set_yscale(y_scale)
                plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
                st.pyplot(fig)
            elif visualization_type == "Histogram":
                fig, ax = plt.subplots(figsize=(width, height))
                df.hist(ax=ax)
                ax.set_xscale(x_scale)
                ax.set_yscale(y_scale)
                plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
                st.pyplot(fig)
            elif visualization_type == "Box Plot":
                fig, ax = plt.subplots(figsize=(width, height))
                df.boxplot(ax=ax)
                ax.set_xscale(x_scale)
                ax.set_yscale(y_scale)
                plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
                st.pyplot(fig)
            elif visualization_type == "Pie Chart":
                fig, ax = plt.subplots(figsize=(width, height))
                df[y_column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
                df[y_column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
                plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
                st.pyplot(fig)
            elif visualization_type == "Heatmap":
                fig, ax = plt.subplots(figsize=(width, height))
                sns.heatmap(df.corr(), annot=True, ax=ax)
                plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
                st.pyplot(fig)
            elif visualization_type == "Pairplot":
                fig = sns.pairplot(df)
                st.pyplot(fig)
            elif visualization_type == "Count Plot":
                fig, ax = plt.subplots(figsize=(width, height))
                sns.countplot(x=x_column, data=df, ax=ax)
                ax.set_xscale(x_scale)
                ax.set_yscale(y_scale)
                plt.xticks(rotation=45, ha='right')
                st.pyplot(fig)
            elif visualization_type == "Violin Plot":
                fig, ax = plt.subplots(figsize=(width, height))
                sns.violinplot(x=x_column, y=y_column, data=df, ax=ax)
                ax.set_xscale(x_scale)
                ax.set_yscale(y_scale)
                plt.xticks(rotation=45, ha='right')
                st.pyplot(fig)
            elif visualization_type == "Boxen Plot":
                fig, ax = plt.subplots(figsize=(width, height))
                sns.boxenplot(x=x_column, y=y_column, data=df, ax=ax)
                ax.set_xscale(x_scale)
                ax.set_yscale(y_scale)
                plt.xticks(rotation=45, ha='right')
                st.pyplot(fig)
            elif visualization_type == "Swarm Plot":
                fig, ax = plt.subplots(figsize=(width, height))
                sns.swarmplot(x=x_column, y=y_column, data=df, ax=ax)
                ax.set_xscale(x_scale)
                ax.set_yscale(y_scale)
                plt.xticks(rotation=45, ha='right')
                st.pyplot(fig)
            elif visualization_type == "Strip Plot":
                fig, ax = plt.subplots(figsize=(width, height))
                sns.stripplot(x=x_column, y=y_column, data=df, ax=ax)
                ax.set_xscale(x_scale)
                ax.set_yscale(y_scale)
                plt.xticks(rotation=45, ha='right')
                st.pyplot(fig)