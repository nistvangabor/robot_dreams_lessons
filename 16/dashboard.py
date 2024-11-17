import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv('16/data/supermarket_sales.csv')
    return df

df = load_data()

# KPI Calculations
total_sales = df['Total'].sum()
total_quantity = df['Quantity'].sum()
avg_sales = df['Total'].mean()
sales_by_product = df.groupby('Product line')['Total'].sum().reset_index()

# Title and KPIs
st.title("Supermarket Sales Dashboard")
st.markdown("### Key Performance Indicators (KPIs)")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", f"${total_sales:,.2f}")
    
with col2:
    st.metric("Total Quantity Sold", f"{total_quantity:,}")
    
with col3:
    st.metric("Average Sales per Transaction", f"${avg_sales:,.2f}")

# Sales by Product Line (using Streamlit's built-in chart)
st.markdown("### Sales by Product Line")
sales_by_product_chart = sales_by_product.set_index('Product line')['Total']
st.bar_chart(sales_by_product_chart)

# Monthly Sales Trend
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total'].sum().reset_index()

st.markdown("### Monthly Sales Trend")
monthly_sales_chart = monthly_sales.set_index('Month')['Total']
st.line_chart(monthly_sales_chart)

# Top 5 Products by Sales (using Streamlit's built-in chart)
top_products = df.groupby('Product line')['Total'].sum().reset_index().sort_values('Total', ascending=False).head(5)

st.markdown("### Top 5 Products by Sales")
top_products_chart = top_products.set_index('Product line')['Total']
st.bar_chart(top_products_chart)

# Display Data Table
st.markdown("### Raw Data")
st.dataframe(df)