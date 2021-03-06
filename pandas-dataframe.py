# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# A DataFrame is a table.
# It contains an array of individual entries, each of which has a certain value.
# Each entry corresponds to a row (or record) and a column.

import pandas as pd

# For Example

print(pd.DataFrame({'Yes': [10, 20], 'No': [30, 40], 'Maybe': [50, 60]}))

# DataFrame entries are not limited to integers.
# For instance, here's a DataFrame whose values are strings:

print(pd.DataFrame({'Chima': ['Kingsley'], 'Onyinye': ['Esther'], 'Kosi': ['Cynthia']}))

# Create a DataFrame from two Series

data = {'calories': [10, 15, 20], 'duration': [20, 40, 60]}
my_data = pd.DataFrame(data)
print(my_data)

# Locate Row
# As you can see from the result above, the DataFrame is like a table with rows and columns.
# Pandas use the loc attribute to return one or more specified row(s)
# Return row 1:
#refer to the row index:

print(my_data.loc[1])

# Return rows 0 and 1:

print(my_data.loc[[0, 1]])

# Note: When using [], the result is a Pandas DataFrame.


# Named Indexes
# With the index argument, you can name your own indexes.
# Add a list of names to give each row a name:

my_data2 = pd.DataFrame(data, index = ['Day1', 'Day2', 'Day3'])
print(my_data2)

# Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s).
# Return "day2":

print(my_data2.loc['Day2'])



