# Empty cells can potentially give you a wrong result when you analyze data.

# Remove Rows
# One way to deal with empty cells is to remove rows that contain empty cells.
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

# Example
# Return a new Data Frame with no empty cells:

import pandas as pd

abc = pd.read_csv("dirtydata.csv")
new_abc = abc.dropna()
print(new_abc.to_string())

# By default, the dropna() method returns a new DataFrame, and will not change the original.

print(abc)

# If you want to change the original DataFrame, use the inplace = True argument:

abc.dropna(inplace = True)
print(abc.to_string())
print(abc)