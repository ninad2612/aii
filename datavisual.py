import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
file_path = "tips-expt4 - tips-expt4.csv"
df = pd.read_csv(file_path)

print(df.head())

sns.boxplot(y=df["total_bill"] )
plt.title("Box Plot of Total Bill")
plt.show()

sns.boxplot(y=df["tip"])
plt.title("Box Plot of Tip")
plt.show()

# Bar plot for average tip by day
sns.barplot(x="day", y="tip", data=df)
plt.title("Average Tip by Day")
plt.ylabel("Average Tip")
plt.show()

sns.histplot(data=df, x="sex", hue="smoker")
plt.title("Smoker Distribution by Gender")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.show()

# Box plot: avg Tip by day and gender
sns.barplot(x=df["day"], y=df["tip"], hue="sex", data=df)
plt.title("Tip Distribution by Day and Gender")
plt.xlabel("Day")
plt.ylabel("Tip")
plt.show()

# Box plot: avg Tip by day and gender
sns.histplot(x=df["sex"])
plt.title("Male and Female count")
plt.xlabel("Day")
plt.ylabel("Tip")
plt.show()

sns.barplot(x=df["day"], y=df["tip"])
plt.title("Tip Distribution by Day")
plt.xlabel("Day")
plt.ylabel("Tip")
plt.show()