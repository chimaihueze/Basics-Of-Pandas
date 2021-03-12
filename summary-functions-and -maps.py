# Plucking the right data out of our data representation is critical to getting work done.
# However, the data does not always come out of memory in the format we want it in right out of the bat.
# Sometimes we have to do some more work ourselves to reformat it for the task at hand.
# This tutorial will cover different operations we can apply to our data to get the input "just right".

import pandas as pd

abc = pd.read_csv('pandas_data.csv')

# Summary functions
# Pandas provides many simple "summary functions" which restructure the data in some useful way.
# For example, consider the describe() method:

db = abc.Pulse.describe()
print(db)

de = abc.Maxpulse.describe()
print(de)

# This method generates a high-level summary of the attributes of the given column.
# It is type-aware, meaning that its output changes based on the data type of the input.

# If you want to get some particular simple summary statistic about a column in a DataFrame or a Series
# There is usually a helpful pandas function that makes it happen.
# For example, to see the mean of the points allotted (e.g. how well an averagely rated Pulse, Maxpulse), we can use the mean() function:

print(abc.Pulse.mean())
print(abc.Maxpulse.mean())

# For the median, we can use the median() function

print(abc.Pulse.median())
print(abc.Maxpulse.median())