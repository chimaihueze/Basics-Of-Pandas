# Duplicate rows are rows that have been registered more than one time.
# By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.
# To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row:
# Example
# Returns True for every row that is a duplicate, othwerwise False:

import pandas as pd

abc = pd.read_csv("dirtydata.csv")
abc["Date"] = pd.to_datetime(abc["Date"])