import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



df = pd.read_csv("data/cardata.csv")

# Convert 'persons' to a numeric type, coercing non-numeric values to NaN
df['persons'] = pd.to_numeric(df['persons'], errors='coerce')

# Drop rows where 'persons' is NaN
df = df.dropna(subset=['persons'])
## Summary statistics
mean = np.mean(df['persons'])
median = np.median(df['persons'])
std  = np.std(df['persons'])


# print("mean:", mean)
print(mean)
print(median)
print(std)

## Buying price frequency bar plot
plt.figure(figsize=(8, 6))
sns.countplot(x='buying', data=df)
plt.title('Frequency Distribution of Buying')
plt.savefig('results/buying_distribution.png')
plt.show()

