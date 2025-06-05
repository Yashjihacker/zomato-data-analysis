import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('E:/Python/Presentation/Data Analysis/zomato.csv', encoding='latin-1')

# Standardize column names
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# Drop unnecessary columns if they exist
columns_to_drop = ['url', 'address', 'phone', 'menu_item', 'dish_liked', 'reviews_list']
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

# Remove duplicates and null values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Rename columns
df = df.rename(columns={
    'listed_in(type)': 'type',
    'average_cost_for_two': 'cost',
    'aggregate_rating': 'rating',
    'has_online_delivery': 'online_order',
    'restaurant_name': 'name'
})

# Clean and convert 'cost' column
df['cost'] = df['cost'].astype(str).apply(lambda x: x.replace(',', '')).astype(float)

# Convert rating to float (remove '/5' if present)
df['rating'] = df['rating'].astype(float)

# ---- Visualizations ---- #

# Top 10 restaurant names
plt.figure(figsize=(8,5))
df['name'].value_counts().head(10).plot(kind='barh', color='skyblue')
plt.title("Top 10 Most Frequent Restaurants")
plt.xlabel("Count")
plt.tight_layout()
plt.show()

# Online order availability
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='online_order', palette='Set2')
plt.title("Online Order Availability")
plt.tight_layout()
plt.show()

# Top 10 cuisines
plt.figure(figsize=(10,5))
df['cuisines'].value_counts().head(10).plot(kind='bar', color='orange')
plt.title("Top 10 Cuisines")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Cost distribution
plt.figure(figsize=(8,4))
sns.histplot(df['cost'], bins=20, color='green')
plt.title("Distribution of Cost for Two")
plt.tight_layout()
plt.show()

# Scatterplot of Cost vs Rating
plt.figure(figsize=(6,4))
sns.scatterplot(x='cost', y='rating', data=df)
plt.title("Cost vs Rating")
plt.tight_layout()
plt.show()

# Pie chart of types
plt.figure(figsize=(6,6))
df['type'].value_counts().head(5).plot(kind='pie', autopct='%1.1f%%')
plt.title("Top Restaurant Types")
plt.ylabel('')
plt.tight_layout()
plt.show()

# Top 10 locations
plt.figure(figsize=(8,5))
df['location'].value_counts().head(10).plot(kind='barh', color='purple')
plt.title("Top 10 Locations")
plt.tight_layout()
plt.show()

# Save cleaned dataset
df.to_csv('cleaned_zomato.csv', index=False)
