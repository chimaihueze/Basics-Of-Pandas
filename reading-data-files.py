# Being able to create a DataFrame or Series by hand is handy.
# But, most of the time, we won't actually be creating our own data by hand.
# Instead, we'll be working with data that already exists.

# Data can be stored in any of a number of different forms and formats. 
# By far the most basic of these is the humble CSV file.

# So a CSV file is a table of values separated by commas. Hence the name: "Comma-Separated Values", or CSV.
# Let's now set aside our toy datasets and see what a real dataset looks like when we read it into a DataFrame.
# We'll use the pd.read_csv() function to read the data into a DataFrame. This goes thusly:

import pandas as pd  

abc = pd.read_csv("pandas_data.csv")
print(abc.to_string())
print(abc.shape)

# So our new DataFrame has 169 records split across 4 different columns. That's about 676 entries!
# We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:

print(abc.head())

# The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify.
# For example, you can see in this dataset that the CSV file has a built-in index, which pandas did not pick up on automatically.
# To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.

abcd = pd.read_csv("pandas_data.csv", index_col = 0)
print(abcd)

print(abcd.head())