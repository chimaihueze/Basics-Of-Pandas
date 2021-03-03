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