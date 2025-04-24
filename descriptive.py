import pandas as pd
data = pd.read_csv('exp1_bmi - exp1_bmi.csv')

print(data[['Height','Weight','bmi','Age']].mean())

print(data[['Height','Weight','bmi','Age']].median())

print(data[['Height','Weight','bmi','Age']].mode().iloc[0])

print(data[['Height','Weight','bmi','Age']].std())

print(data[['Height','Weight','bmi','Age']].var())

rangevalues = data[['Height','Weight','bmi','Age']].max() - data[['Height','Weight','bmi','Age']].min()
rangevalues

q1 = data[['Height','Weight','bmi','Age']].quantile(0.25)
q2 = data[['Height','Weight','bmi','Age']].mean()
q3 = data[['Height','Weight','bmi','Age']].quantile(0.7)
print(q1)
print(q2)
print(q3)

iqr = q3 - q1
iqr

print(data[['Height','Weight','bmi','Age']].skew())

print(data[['Height','Weight','bmi','Age']].kurtosis())