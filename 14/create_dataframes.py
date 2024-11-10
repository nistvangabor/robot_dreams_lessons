import pandas as pd

#CREATING DATAFRAMES:
#from 2 or more series with the same index:
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['a', 'b', 'c'])

df = pd.DataFrame({'col1': s1, 'col2': s2})

print(df)

#from 2 or more series with different indexes:
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])


df = pd.DataFrame({'col1': s1, 'col2': s2})
df = df.fillna(0) #ezt utólag megmutatni

print(df)


#create a dataframe from a dictionary:

data = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

print(df)

#create a dataframe from a list of dictionaries:
data = [{'ID': 1, 'Name': 'Alice', 'Age': 25},
        {'ID': 2, 'Name': 'Bob', 'Age': 30},
        {'ID': 3, 'Name': 'Charlie', 'Age': 35}]

df = pd.DataFrame(data)

print(df)

#create dataframe from a list of lists:

data = [[1, 'Alice', 25], [2, 'Bob', 30], [3, 'Charlie', 35]]
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])

print(df)


#create dataframe from a csv file:

df = pd.read_csv("14/supermarket_sales.csv")
print(df)

#create dataframe from a json:

df = pd.read_json('14/test.json')

print(df)


# converting dataframe back to basic python data structures:

data_as_list_of_dicts = df.to_dict(orient='records')
print(data_as_list_of_dicts)
data_as_dict_of_lists = df.to_dict(orient='list')
print(data_as_dict_of_lists)
data_as_list_of_lists = df.values.tolist()
print(data_as_list_of_lists)
