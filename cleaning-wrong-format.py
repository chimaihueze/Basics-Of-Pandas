# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
# Convert Into a Correct Format

# In our Data Frame, we have two cells with the wrong format.
# Check out row 22 and 26, the 'Date' column should be a string that represents a date:

import pandas as pd

abc = pd.read_csv("dirtydata.csv")
print(abc) 

# Let's try to convert all cells in the 'Date' column into dates.
# Pandas has a to_datetime() method for this:

abc['Date'] = pd.to_datetime(abc['Date'])
print(abc.to_string())

# As you can see from the result, the date in row 26 where fixed, but the empty date in row 22 got a NaT (Not a Time) value, in other words an empty value.
# One way to deal with empty values is simply removing the entire row.

# Removing Rows
# The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value.
# We can remove the row by using the dropna() method.

abc.dropna(subset=['Date'], inplace = True)
print(abc.to_string())



