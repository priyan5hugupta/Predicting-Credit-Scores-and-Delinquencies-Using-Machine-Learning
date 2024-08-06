import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('BalanceDataSet.csv')

x = data.drop(['SeriousDlqin2yrs','Unnamed: 0.1','Unnamed: 0'],axis =1)
y = data['SeriousDlqin2yrs']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30, random_state = 0)

modelLogistic = LogisticRegression()
modelLogistic.fit(x_train,y_train)

print("The intercept b0= ", modelLogistic.intercept_)
print("The coefficient b1= ", modelLogistic.coef_)

y_pred= modelLogistic.predict(x_test)

ConfusionMatrix = confusion_matrix(y_test, y_pred)
print(ConfusionMatrix)


ax = sb.heatmap(ConfusionMatrix, annot=True, cmap='BuPu')
ax.set_title('Confusion Matrix for SeriousDlqin2yrs predicition')
ax.set_xlabel('Prediction made for SeriousDlqin2yrs')
ax.set_ylabel('Actual status of SeriousDlqin2yrs')
ax.xaxis.set_ticklabels(['Not SeriousDlqin2yrs','SeriousDlqin2yrs'])
ax.yaxis.set_ticklabels(['Not SeriousDlqin2yrs','SeriousDlqin2yrs'])
plt.show()

TP= ConfusionMatrix[1,1] 
TN= ConfusionMatrix[0,0] 
Total=len(y_test)
print("Accuracy from confusion matrix is ", (TN+TP)/Total)



