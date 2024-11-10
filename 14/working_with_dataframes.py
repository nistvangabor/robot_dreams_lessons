import pandas as pd

df = pd.read_csv("14/supermarket_sales.csv", dtype={"Branch": "string"}) #pre-defining types if needed, oszlopoknál ahol 0-val kezdődik a szám
print(df.dtypes)
print(df.info())
print(df.dtypes)
print(df.head())
print(df.tail())


#basic statistical data:
print(df.describe())

#selecting columns:

product_price_df = df[["Product line", "Unit price"]]
ratings_df = df["Rating"]
print(product_price_df)
print(type(ratings_df))

# Sor kiválasztása címkékkel (loc)
print("\nloc példák:\n", df.loc[1, 'Product line'])  # Második sor, 'name' oszlop

# Több sor és oszlop kiválasztása loc-kal
print("\nTöbb sor és oszlop kiválasztása loc-kal:\n", df.loc[1:3, ["Product line", "Unit price"]])

# Sor kiválasztása pozíció alapján (iloc)
print("\niloc példák:\n", df.iloc[1, 1])  # Második sor, második oszlop

# Több sor és oszlop kiválasztása iloc-kal
print("\nTöbb sor és oszlop kiválasztása iloc-kal:\n", df.iloc[1:3, [1, 2]])


#aggregation and grouping:
total_sales_df = df.groupby(['City', 'Product line'])['Total'].sum().reset_index()
print(total_sales_df)

avg_rating_df = df.groupby(['Customer type', 'Payment'])['Rating'].mean().reset_index()
print(avg_rating_df)

#sorting:
sorted_df = df.sort_values(["Product line", "Unit price"], ascending=[True, False])
print(sorted_df)

#filtering
yangon_df = df[df['City'] == 'Yangon']

result = (
    df[df['City'] == 'Yangon']  # Filter for 'Yangon'
    .groupby('Gender')  # Group by Gender
    .agg({'Unit price': 'mean'})  # Calculate the average unit price
    .reset_index()  # Reset index to flatten the DataFrame
    .sort_values('Unit price', ascending=True)  # Sort by average unit price ascending
)
print("----------------------")
print(result)
print("----------------------")


# adatok létrehozása
data1 = {
    'id': [1, 2, 3, 4],
    'name': ['Apple', 'Tesla', 'Amazon', 'Microsoft'],
    'price': [150, 700, 3300, 290],
    'quantity': [100, 50, 30, 200]
}

data2 = {
    'id': [1, 2, 3, 5],
    'symbol': ['AAPL', 'TSLA', 'AMZN', 'GOOGL'],
    'market_cap': [2500000000, 800000000, 1600000000, 1200000000]
}

df_stock_base = pd.DataFrame(data1)
df_stock_extension = pd.DataFrame(data2)


df_stock_base.to_csv("14/stock_base.csv", index=False)
df_stock_extension.to_csv("14/stock_extension.csv", index=False)

merged_stock_df = pd.merge(df_stock_base, df_stock_extension, on="id", how="outer")
print(merged_stock_df)

#calculated field létrehozása:
merged_stock_df['total_value'] = merged_stock_df['price'] * merged_stock_df['quantity']
print(merged_stock_df)


def categorize_stock(row):
    if row['price'] > 1000 or row['quantity'] < 50:
        return 'Premium'
    else:
        return 'Standard'
    
merged_stock_df['category'] = merged_stock_df.apply(categorize_stock, axis=1)


#filtering:

filtered_stock_df = merged_stock_df[merged_stock_df['price'] > 300]
print("\nSzűrt DataFrame (ár > 100):\n", filtered_stock_df)


