# So far we've been indexing various strides of data, using structural properties of the DataFrame itself. 
# To do interesting things with the data, however, we often need to ask questions based on conditions.
# For example, suppose that we're interested specifically in pulses greater than 100.
# We can start by checking if each pulse is greater than 100 or not:

import pandas as pd

