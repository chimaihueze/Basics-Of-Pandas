# So far we've been indexing various strides of data, using structural properties of the DataFrame itself. 
# To do interesting things with the data, however, we often need to ask questions based on conditions.
# For example, suppose that we're interested specifically in pulses greater than 100.
# We can start by checking if each pulse is greater than 100 or not:

import pandas as pd

abc = pd.read_csv("pandas_data.csv")

print(abc.Pulse > 100)

# This operation produced a Series of True/False booleans based on the country of each record. 
# This result can then be used inside of loc to select the relevant data:

db = abc.loc[abc.Pulse > 100]
print(db)

# This DataFrame has 110 rows. The original had 169. That means that around 65% of the Pulses are greater than 100.

# We can also check for those Calories greater than 400.0
# We can use the ampersand (&) to bring the two questions together:

print(abc.loc[(abc.Pulse > 100) & (abc.Calories > 400.0)])

# Suppose we want to check Pulse that's greater than 100 or Maxppulse greater than 130. For this we use a pipe (|):

print(abc.loc[(abc.Pulse > 100) | (abc.Maxpulse > 130)]) 

# Pandas comes with a few built-in conditional selectors, two of which we will highlight here.
# The first is isin. isin lets you select data whose value "is in" a list of values.
# For example, here's how we can use it to select Pulses of 100 or 110:

print(abc.loc[(abc.Pulse.isin([100, 110]))])
