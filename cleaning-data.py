# Data cleaning means fixing bad data in your data set.

# Bad data could be:
# 1. Empty cells
# 2. Data in wrong format
# 3. Wrong data
# 4. Duplicates

import pandas as pd

our_dataset = pd.read_csv("dirtydata.csv")
print(our_dataset)