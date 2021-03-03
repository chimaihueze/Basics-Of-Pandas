# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.

import pandas as pd

# Create a DataFrame from two Series

data = {'calories': [10, 15, 20], 'duration': [20, 40, 60]}
my_data =pd.DataFrame(data)
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

print(pd.DataFrame(data, index = ['Day1', 'Day2', 'Day3']))