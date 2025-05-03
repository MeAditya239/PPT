#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
pf = pd.read_csv(r"C:\Users\Aditya\Downloads\archive\iris.csv")
pf


# In[5]:


from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Step 1: Load Iris dataset
iris = load_iris()

# Step 2: Create DataFrame with feature data
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Step 3: Add the species column (using the target and target_names)
df['species'] = [iris.target_names[i] for i in iris.target]

# Step 4: Encode species column to numeric
label_encoder = LabelEncoder()
df['species'] = label_encoder.fit_transform(df['species'])

# Display the first few rows
print(df.head())

import os
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Suppress the warning about CPU cores
os.environ["LOKY_MAX_CPU_COUNT"] = "1"  # You can adjust this if needed

# Step 1: Load Iris dataset
iris = load_iris()

# Step 2: Create DataFrame with feature data
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Step 3: Add the species column (using the target and target_names)
df['species'] = [iris.target_names[i] for i in iris.target]

# Step 4: Encode species column to numeric
label_encoder = LabelEncoder()
df['species'] = label_encoder.fit_transform(df['species'])

# Step 5: Apply KMeans with 3 clusters (since we know there are 3 iris species)
X = df.drop('species', axis=1)  # Use all features except the species column
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Step 6: Add cluster labels to the DataFrame
df['cluster'] = kmeans.labels_



# In[6]:


# Step 7: Visualize the clusters using 2 features (e.g., petal length & petal width)
plt.figure(figsize=(8, 5))
plt.scatter(df['petal length (cm)'], df['petal width (cm)'], c=df['cluster'], cmap='viridis', s=50)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('K-Means Clustering on Iris Dataset')
plt.grid(True)
plt.show()


# In[ ]:




