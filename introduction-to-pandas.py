# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.
# Pandas allows us to analyze big data and make conclusions based on statistical theories.
# Pandas can clean messy data sets, and make them readable and relevant.
# Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.
# In pandas, a data table is called a DataFrame.

import pandas as pd

my_dataset = {'cars': ['Volvo', 'Volkswagen', 'Maybach'], 'passings': [2, 5, 9]}
my_var = pd.DataFrame(my_dataset)
print(my_var)

# Checking Pandas Version
# The version string is stored under __version__ attribute.

print(pd.__version__)

# I want to store passenger data of the Titanic.
# For a number of passengers, I know the name (characters), age (integers) and sex (male/female) data.

titanic = {'name': ["Braund, Mr. Owen Harris", "Allen, Mr. William Henry", "Bonnell, Miss. Elizabeth"], 'age': [22, 35, 58], 'sex': ["male", "male", "female"]}
print(pd.DataFrame(titanic))








