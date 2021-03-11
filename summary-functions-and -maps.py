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