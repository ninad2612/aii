import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np

# 1. Load dataset
df = pd.read_csv("dbscan_outlier_dataset - dbscan_outlier_dataset.csv")  # Replace with your actual CSV filename

# 2. Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['X', 'Y']])

# 3. Apply DBSCAN
db = DBSCAN(eps=0.5, min_samples=5).fit(X_scaled)
df['Cluster'] = db.labels_

# 4. Plotting
plt.figure(figsize=(12, 5))

# Before Clustering
plt.subplot(1, 2, 1)
plt.scatter(df['X'], df['Y'], c='gray', s=50)
plt.title("Before Clustering")
plt.xlabel("X")
plt.ylabel("Y")

# After Clustering
plt.subplot(1, 2, 2)

# Separate core clusters and outliers
outliers = df[df['Cluster'] == -1]
clusters = df[df['Cluster'] != -1]

# Plot clusters with colormap
plt.scatter(clusters['X'], clusters['Y'], c=clusters['Cluster'], cmap='tab10', s=50, label='Clusters')

# Plot outliers in red
plt.scatter(outliers['X'], outliers['Y'], c='red', s=50, label='Outliers')

plt.title("After DBSCAN Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.tight_layout()
plt.show()
