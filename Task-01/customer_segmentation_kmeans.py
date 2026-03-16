import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Create simple dataset
data = {
    "AnnualIncome": [15,16,17,20,21,22,25,30,35,40,45,50],
    "SpendingScore": [39,81,6,77,40,76,94,3,72,14,99,15]
}

df = pd.DataFrame(data)

# Apply KMeans
kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(df)

print(df)

# Plot clusters
plt.scatter(df["AnnualIncome"], df["SpendingScore"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.show()