import streamlit as st
import pandas as pd

# Title of the app
st.title("CSV File Upload and Display")

# Upload CSV file
st.markdown("### Upload your CSV file")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the uploaded file as a Pandas DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the DataFrame
    st.markdown("### Data Preview")
    st.dataframe(df)
    
    # Show the shape of the DataFrame (rows, columns)
    st.markdown(f"**Shape of DataFrame**: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Optionally, show some statistics about the data
    st.markdown("### Basic Statistics")
    st.write(df.describe())
else:
    st.info("Please upload a CSV file to display its content.")