import pandas as pd
print(pd.__version__)

#read from a list
s_from_list = pd.Series(["1", "2", "3", "4"])
print(s_from_list)
s_from_list = s_from_list.astype('string')
print(s_from_list)

#read from a dictionary
s = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(s)


#indexing
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s['a'])  # Accessing data by index) it will be a numpy array element


#limiting records with indexing:
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

#vectorization
s = pd.Series([1, 2, 3, 4])
print(s + 2)  # Adding 2 to each element

print(s % 3 == 0)

#conditional vectorization
s = s + 2 * (s % 3 == 0)
print(s)

"""
1 + 2 * 0
2 + 2 * 0
3 + 2 * 1
4 + 2 * 0
"""


