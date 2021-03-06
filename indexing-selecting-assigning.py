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
