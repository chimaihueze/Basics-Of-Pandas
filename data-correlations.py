# Finding Relationships
# A great aspect of the Pandas module is the corr() method.
# The corr() method calculates the relationship between each column in your data set.

import pandas as pd

abc = pd.read_csv("pandas_data.csv")

# Example
# Show the relationship between the columns:

print(abc.corr())