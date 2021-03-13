# Data cleaning means fixing bad data in your data set.

# Bad data could be:
# 1. Empty cells
# 2. Data in wrong format
# 3. Wrong data
# 4. Duplicates

import pandas as pd

our_dataset = pd.read_csv("dirtydata.csv")
print(our_dataset)

# The data set contains some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).
# The data set contains wrong format ("Date" in row 26).
# The data set contains wrong data ("Duration" in row 7).
# The data set contains duplicates (row 11 and 12).

