# Combining
# When performing operations on a dataset, we will sometimes need to combine different DataFrames and/or Series in non-trivial ways.
# Pandas has three core methods for doing this.
# In order of increasing complexity, these are concat(), join(), and merge().

import pandas as pd

# Most of what merge() can do can also be done more simply with join(), so we will omit it and focus on the first two functions here.
# The simplest combining method is concat().
# Given a list of elements, this function will smush those elements together along an axis.

can_youtube = pd.read_csv("ca_videos.csv")
gb_youtube = pd.read_csv("gb_videos.csv")
print(can_youtube)
print(gb_youtube)

print(pd.concat([can_youtube, gb_youtube]))

# The middlemost combiner in terms of complexity is join().
# join() lets you combine different DataFrame objects which have an index in common.
# For example, to pull down videos that happened to be trending on the same day in both Canada and the UK, we could do the following:

left = can_youtube.set_index(['title', 'trending_date'])
right = gb_youtube.set_index(['title', 'trending_date'])

ab = left.join(right, lsuffix = '_CAN', rsuffix = '_UK')
print(ab)






