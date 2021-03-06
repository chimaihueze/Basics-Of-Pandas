# Selecting specific values of a pandas DataFrame or Series to work on is an implicit step in almost any data operation you'll run.
# So one of the first things you need to learn in working with data in Python is how to go about selecting the data points relevant to you quickly and effectively.

import pandas as pd

# Native Python objects provide good ways of indexing data.
# Pandas carries all of these over, which helps make it easy to start with.

ab = (pd.read_csv("pandas_data.csv"))
print(ab)

# In Python, we can access the property of an object by accessing it as an attribute.
# A book object, for example, might have a title property, which we can access by calling book.title.
# Columns in a pandas DataFrame work in much the same way.
# Hence to access the Pulse property of python_data we can use:

print(ab['Pulse'])
print(ab['Maxpulse'])

print(ab['Pulse'][0])
print(ab['Maxpulse'][0])

# Indexing in pandas
# The indexing operator and attribute selection are nice because they work just like they do in the rest of the Python ecosystem.
# As a novice, this makes them easy to pick up and use.
# However, pandas has its own accessor operators, loc and iloc.
# For more advanced operations, these are the ones you're supposed to be using.

print(ab.iloc[0])

# Both loc and iloc are row-first, column-second.
# This is the opposite of what we do in native Python, which is column-first, row-second.
# This means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns.
# To get a column with iloc, we can do the following:

print(ab.iloc[:, 0])

# On its own, the : operator, which also comes from native Python, means "everything".
# When combined with other selectors, however, it can be used to indicate a range of values.
# For example, to select the country column from just the first, second, and third row, we would do:

