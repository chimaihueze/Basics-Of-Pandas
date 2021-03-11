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
