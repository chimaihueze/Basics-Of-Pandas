# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.

import pandas as pd

# Create a DataFrame from two Series

data = {'calories': [10, 15, 20], 'duration': [20, 40, 60]}
print(pd.DataFrame(data))