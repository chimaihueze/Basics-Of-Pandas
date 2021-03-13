# Maps allow us to transform data in a DataFrame or Series one value at a time for an entire column.
# However, often we want to group our data, and then do something specific to the group the data is in.
# As you'll learn, we do this with the groupby() operation.
# We'll also cover some additional topics, such as more complex ways to index your DataFrames, along with how to sort your data.

import pandas as pd

abc = pd.read_csv('pandas_data.csv')

# Groupwise analysis
# One function we've been using heavily thus far is the value_counts() function. 
# We can replicate what value_counts() does by doing the following:

print(abc.groupby('Pulse').Pulse.count())
print(abc.groupby('Maxpulse').Maxpulse.count())

# groupby() created a group of reviews which allotted the same Pulse values.
# Then, for each of these groups, we grabbed the Pulse() column and counted how many times it appeared.
# value_counts() is just a shortcut to this groupby() operation.
# We can use any of the summary functions we've used before with this data.
# For example, to get the lowest Calories in each Pulse value category, we can do the following:

print(abc.groupby('Pulse').Calories.min())


