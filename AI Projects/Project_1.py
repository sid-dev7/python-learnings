import pandas as pd
data = pd.read_csv('world_gdp.csv')

print(data.columns)

import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
data = pd.read_csv('world_gdp.csv')

# Clean / Filter for top 10 countries
top_countries = data.sort_values(by='GDP', ascending=False).head(10)

# Plot
plt.figure(figsize=(12,6))
sns.barplot(x='Country', y='GDP', data=top_countries, palette='viridis')
plt.title('Top 10 Countries by GDP')
plt.xticks(rotation=45)
plt.show()
