import streamlit as st
import pandas as pd

st.title("Read only Supermarket data")

supermarket_df = pd.read_csv("./16/data/supermarket_sales.csv")
st.dataframe(supermarket_df)

st.title("Dataframe with write permissions")
editable_df = st.data_editor(supermarket_df)
print(editable_df.loc[0, "Branch"])

#st.title("Static table - no filters, no search, no download")
#static_table = st.table(supermarket_df)

#showing metric for KPIs:

st.header("Metrics")
st.metric(label="Total sales:", value=f"${supermarket_df['Total'].sum():,.2f}")