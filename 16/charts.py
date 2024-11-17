import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt


st.title("Charts")
supermarket_df = pd.read_csv("./16/data/supermarket_sales.csv", parse_dates=["Date"])
supermarket_df.set_index("Date", inplace=True)

# Plot the 'Total' column with the 'Date' index
st.subheader("Sales Trend Over Time")
sales_trend = supermarket_df.groupby("Date")["Total"].sum()
st.line_chart(sales_trend)

# Bar chart: Sales by branch
st.subheader("Total Sales by Branch")
branch_sales = supermarket_df.groupby("Branch")["Total"].sum()
st.bar_chart(branch_sales)

# sales by product line

st.subheader("Sales by Product Line")
product_line_sales = supermarket_df.groupby("Product line")["Total"].sum()
st.bar_chart(product_line_sales)

st.subheader("Payment Method Distribution")
payment_distribution = supermarket_df["Payment"].value_counts()


# Create a Matplotlib figure and axis
fig, ax = plt.subplots()
payment_distribution.plot.pie(autopct='%1.1f%%', ax=ax, ylabel='')
st.pyplot(fig)


st.subheader("Customer Ratings Distribution")

# Round ratings to the nearest whole number
supermarket_df["Rounded Rating"] = supermarket_df["Rating"].round()

# Count the number of occurrences for each rounded rating
rating_distribution = supermarket_df["Rounded Rating"].value_counts().sort_index()

# Display the bar chart with Streamlit
st.bar_chart(rating_distribution)