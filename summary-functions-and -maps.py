# Plucking the right data out of our data representation is critical to getting work done.
# However, the data does not always come out of memory in the format we want it in right out of the bat.
# Sometimes we have to do some more work ourselves to reformat it for the task at hand.
# This tutorial will cover different operations we can apply to our data to get the input "just right".

import pandas as pd

abc = pd.read_csv('pandas_data.csv')
print(abc)
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

# To see a list of unique values we can use the unique() function:

print(abc.Pulse.unique())
print(abc.Maxpulse.unique())

# To see a list of unique values and how often they occur in the dataset, we can use the value_counts() method:

print(abc.Pulse.value_counts())
print(abc.Maxpulse.value_counts())

# Maps
# A map is a term, borrowed from mathematics, for a function that takes one set of values and "maps" them to another set of values.
# In data science we often have a need for creating new representations from existing data, or for transforming data from the format it is in now to the format that we want it to be in later. 
# Maps are what handle this work, making them extremely important for getting your work done!

# There are two mapping methods that you will use often.
# map() is the first, and slightly simpler one.
# For example, suppose that we wanted to remean the scores of the Pulse to 0.
# We can do this as follows: 

abcpulse_mean = abc.Pulse.mean()
print(abc.Pulse.map(lambda p: p - abcpulse_mean))

# The function you pass to map() should expect a single value from the Series, and return a transformed version of that value.
# map() returns a new Series where all the values have been transformed by your function.

# apply() is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.

def remean_Points(row):
    row.Pulse = row.Pulse - abcpulse_mean
    return row

print(abc.apply(remean_Points, axis = 'columns'))

# If we had called abc.apply() with axis='index', then instead of passing a function to transform each row, we would need to give a function to transform each column.
# Note that map() and apply() return new, transformed Series and DataFrames, respectively.
# They don't modify the original data they're called on.
# If we look at the first row of abc, we can see that it still has its original points value.

print(abc.head(1))

# Pandas provides many common mapping operations as built-ins.
# For example, here's a faster way of remeaning our Pulse column:

abcpulse_mean = abc.Pulse.mean()
remean_Pulse = abc.Pulse - abcpulse_mean
print(remean_Pulse)