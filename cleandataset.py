
import pandas as pd
data = pd.read_csv('creditdataset.csv')
print(data)
data.dropna(inplace=True)
data.to_csv('CleanDataSet.csv')