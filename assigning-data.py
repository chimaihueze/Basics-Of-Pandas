# Going the other way, assigning data to a DataFrame is easy.
# You can assign either a constant value:

import pandas as pd

abc = pd.read_csv("pandas_data.csv")
db = abc['Heartrate'] = 100
print(db)
print(abc)