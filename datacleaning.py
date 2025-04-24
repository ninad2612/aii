import pandas as pd

data = pd.read_csv('exp2_DATA-CLEANING-EXT2-DATASET - DATA-CLEANING-EXT2-DATASET.csv')

data.info()

data.isnull().sum()

data['Age'] = data['Age'].fillna(data['Age'].mean())

data['Name'] = data['Name'].fillna(data['Name'].mode().iloc[0])
data['Salary'] = data['Salary'].fillna(data['Salary'].mean())

import numpy as np
data['Gender'] = data['Gender'].replace({'M': 'Male', 'F': 'Female', 'Unknown': np.nan})
data['Gender'] = data['Gender'].fillna(data['Gender'].mode()[0])
data['Joining_Date'] = data['Joining_Date'].fillna(data['Joining_Date'].mode()[0])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['Gender'] = le.fit_transform(data['Gender'])

data['Name'] = le.fit_transform(data['Name'])
data['Joining_Date'] = le.fit_transform(data['Joining_Date'])
data['Department'] = le.fit_transform(data['Department'])


# For Age
Q1 = data['Age'].quantile(0.25)
Q3 = data['Age'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
# data = data[(data['Age'] >= lower) & (data['Age'] <= upper)]
outage=[]
for d in data['Age'] :
    if d< lower or d > upper :
        outage.append(d)
print(outage)

# For Salary
Q1 = data['Salary'].quantile(0.25)
Q3 = data['Salary'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
print(lower )
print(upper )
# data = data[(data['Salary'] >= lower) & (data['Salary'] <= upper)]
outsal=[]
for d in data['Salary'] :
    if d< lower or d > upper :
        outsal.append(d)
print(outsal)

index_to_drop = data[data['ID'] == 6].index

# Now drop that row using .drop()
data = data.drop(index_to_drop)

from sklearn.preprocessing import StandardScaler

# Select only numeric columns
numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns

# Initialize scaler
scaler = StandardScaler()

# Apply scaling
data[numeric_cols] = scaler.fit_transform(data[numeric_cols])