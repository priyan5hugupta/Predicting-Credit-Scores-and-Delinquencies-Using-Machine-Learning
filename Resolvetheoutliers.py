import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv('CleanDataSet.csv')

for x in data.index:
  if data.loc[x, "NumberOfTime30-59DaysPastDueNotWorse"] > 10:
    data.drop(x, inplace = True)

for x in data.index:
  if data.loc[x, "NumberOfTime60-89DaysPastDueNotWorse"] > 10:
    data.drop(x, inplace = True)

for x in data.index:
  if data.loc[x, "NumberOfTimes90DaysLate"] > 10:
    data.drop(x, inplace = True)

for x in data.index:
  if data.loc[x, "age"] < 20 or data.loc[x, "age"] >100 :
    data.drop(x, inplace = True)

for x in data.index:
  if data.loc[x, "DebtRatio"] > 3500 :
    data.drop(x, inplace = True)
    
for x in data.index:
  if data.loc[x, "MonthlyIncome"] > 35000 :
    data.drop(x, inplace = True)
   
for x in data.index:
  if data.loc[x, "RevolvingUtilizationOfUnsecuredLines"] < 0 :
    data.drop(x, inplace = True)

for x in data.index:
  if data.loc[x, "RevolvingUtilizationOfUnsecuredLines"] > 1 :
    data.drop(x, inplace = True)
    
for x in data.index:
  if data.loc[x, "NumberOfDependents"] > 10 :
    data.drop(x, inplace = True)    

for x in data.index:
  if data.loc[x, "NumberRealEstateLoansOrLines"] > 10 :
    data.drop(x, inplace = True)
  
for x in data.index:
  if data.loc[x, "NumberOfOpenCreditLinesAndLoans"] > 30 :
    data.drop(x, inplace = True)

plt.scatter(data['NumberOfTimes90DaysLate'].to_numpy(), data['SeriousDlqin2yrs'].to_numpy())
plt.xlabel('Number Of Times 90 Days Lat')
plt.ylabel('Serious Dlq in 2 yrs')
plt.show() 

plt.scatter(data['NumberOfTime30-59DaysPastDueNotWorse'].to_numpy(), data['SeriousDlqin2yrs'].to_numpy())
plt.xlabel('Number Of Time 30-59 Days Past Due Not Worse')
plt.ylabel('Serious Dlq in 2yrs')
plt.show() 

plt.scatter(data['NumberOfTime60-89DaysPastDueNotWorse'].to_numpy(), data['SeriousDlqin2yrs'].to_numpy())
plt.xlabel('Number Of Time 60-89 Days Past Due Not Worse')
plt.ylabel('Serious Dlq in 2 yrs')
plt.show() 

plt.scatter(data['RevolvingUtilizationOfUnsecuredLines'].to_numpy(), data['SeriousDlqin2yrs'].to_numpy())
plt.xlabel('Revolving Utilization Of Unsecured Lines')
plt.ylabel('Serious Dlq in 2 yrs')
plt.show() 

plt.scatter(data['age'].to_numpy(), data['SeriousDlqin2yrs'].to_numpy())
plt.xlabel('Age')
plt.ylabel('Serious Dlq in 2 yrs')
plt.show() 

plt.scatter(data['DebtRatio'].to_numpy(), data['SeriousDlqin2yrs'].to_numpy())
plt.xlabel('Debt Ratio')
plt.ylabel('Serious Dlq in 2 yrs')
plt.show() 

plt.scatter(data['MonthlyIncome'].to_numpy(), data['SeriousDlqin2yrs'].to_numpy())
plt.xlabel('Monthly Income')
plt.ylabel('Serious Dlq in 2 yrs')
plt.show() 

plt.scatter(data['NumberOfOpenCreditLinesAndLoans'].to_numpy(), data['SeriousDlqin2yrs'].to_numpy())
plt.xlabel('Number Of Open Credit Lines And Loans')
plt.ylabel('Serious Dlq in 2 yrs')
plt.show() 

plt.scatter(data['NumberRealEstateLoansOrLines'].to_numpy(), data['SeriousDlqin2yrs'].to_numpy())
plt.xlabel('Number Real Estate Loans Or Lines')
plt.ylabel('Serious Dlq in 2 yrs')
plt.show() 

plt.scatter(data['NumberOfDependents'].to_numpy(), data['SeriousDlqin2yrs'].to_numpy())
plt.xlabel('Number Of Dependents')
plt.ylabel('Serious Dlq in 2 yrs')
plt.show() 

dataplot = sb.heatmap(data.corr(), cmap="YlGnBu", annot=True)
plt.show()

data.to_csv('DatasetRemovingAllTheOutliers.csv')