# Oftentimes data will come to us with column names, index names, or other naming conventions that we are not satisfied with.
# In that case, you'll learn how to use pandas functions to change the names of the offending entries to something better.
# You'll also explore how to combine data from multiple DataFrames and/or Series.

import pandas as pd

abc = pd.read_csv("pandas_data.csv")

# The first function we'll introduce here is rename(), which lets you change index names and/or column names.
# For example, to change the Calories column in our dataset to Cal, we would do:

db = abc.rename(columns = {"Calories": "Cal"})
print(db)

# rename() lets you rename index or column values by specifying a index or column keyword parameter, respectively.
# It supports a variety of input formats, but usually a Python dictionary is the most convenient.
# Here is an example using it to rename some elements of the index.




