# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

import pandas as pd

# Create a simple Pandas Series from a list:

a = [1, 2, 3, 4]
myvar = pd.Series(a)
print(myvar)

# Labels
# If nothing else is specified, the values are labeled with their index number.
# First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value.

print(myvar[1])
print(myvar[2])

# Create Labels
# With the index argument, you can name your own labels.
# Create you own labels:

myvar2 = pd.Series(a, index = ['w', 'x', 'y', 'z'])
print(myvar2)

# When you have created labels, you can access an item by referring to the label.
# Return the value of "y":

print(myvar2['y'])
print(myvar2['x'])

# Key/Value Objects as Series.
# You can also use a key/value object, like a dictionary, when creating a Series.
# Create a simple Pandas Series from a dictionary:

calories = {'day1': '10', 'day2': '15', 'day3': '20'}
my_cal = pd.Series(calories)
print(my_cal)

# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
# Create a Series using only data from "day1" and "day2":

print(pd.Series(calories, index = ['day1', 'day2']))