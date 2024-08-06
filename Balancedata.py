#We use under sampler algorith to balance the dataset
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from imblearn.under_sampling import RandomUnderSampler 
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('DatasetRemovingAllTheOutliers.csv')

x = data.drop(['SeriousDlqin2yrs'],axis =1)
y = data['SeriousDlqin2yrs']
print(y.value_counts())

(data['SeriousDlqin2yrs'].value_counts()/np.float(len(data))).plot.pie(autopct = '%.2f')
plt.show()
print("It shows that dataset is highly imbalance.")
print("To balance this dataset we use under sampler approach.")
rus = RandomUnderSampler(sampling_strategy= 1)
x_res,y_res = rus.fit_resample(x,y)
print(y_res.value_counts())
print("Now the dataset is balance.")
data = pd.DataFrame(x_res)
data['SeriousDlqin2yrs'] = y_res
data.to_csv('BalanceDataSet.csv')