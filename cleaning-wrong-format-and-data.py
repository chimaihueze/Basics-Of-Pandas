# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
# Convert Into a Correct Format

# In our Data Frame, we have two cells with the wrong format.
# Check out row 22 and 26, the 'Date' column should be a string that represents a date:

import pandas as pd

abc = pd.read_csv("dirtydata.csv")
print(abc) 

# Let's try to convert all cells in the 'Date' column into dates.
# Pandas has a to_datetime() method for this:

abc['Date'] = pd.to_datetime(abc['Date'])
print(abc.to_string())

# As you can see from the result, the date in row 26 where fixed, but the empty date in row 22 got a NaT (Not a Time) value, in other words an empty value.
# One way to deal with empty values is simply removing the entire row.

# Removing Rows
# The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value.
# We can remove the row by using the dropna() method.

abc.dropna(subset=['Date'], inplace = True)
print(abc.to_string())

# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".
# Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.
# If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.
# It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes.

# How can we fix wrong values, like the one for "Duration" in row 7?
# Replacing Values
# One way to fix wrong values is to replace them with something else.
# In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:

abc.loc[7, 'Duration'] = 45
print(abc.to_string)

# For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
# To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

# Loop through all values in the "Duration" column.
# If the value is higher than 120, set it to 120:

abc = pd.read_csv("dirtydata.csv")
abc['Date'] = pd.to_datetime(abc['Date'])
abc.dropna(subset=['Date'], inplace = True) 

for x in abc.index:
    if abc.loc[x, "Duration"] > 120:
        abc.loc[x, "Duration"] = 120
        
print(abc.to_string())

# Removing Rows
# Another way of handling wrong data is to remove the rows that contains wrong data.
# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
# Example
# Delete rows where "Duration" is higher than 120:

abc = pd.read_csv("dirtydata.csv")
abc['Date'] = pd.to_datetime(abc['Date'])
abc.dropna(subset=['Date'], inplace = True) 

for y in abc.index:
    if abc.loc[y, "Duration"] > 120:
        abc.drop(y, inplace = True)
        
print(abc.to_string())