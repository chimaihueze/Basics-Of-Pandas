# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".
# Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.
# If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.
# It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes.

import pandas as pd

abc = pd.read_csv("dirtydata.csv")
abc['Date'] = pd.to_datetime(abc['Date'])
abc.dropna(subset=['Date'], inplace = True)

# How can we fix wrong values, like the one for "Duration" in row 7?
# Replacing Values
# One way to fix wrong values is to replace them with something else.
# In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:

abc.loc[7, 'Duration'] = 45
print(abc.to_string)