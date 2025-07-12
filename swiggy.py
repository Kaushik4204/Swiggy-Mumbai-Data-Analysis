import pandas as pd
import sqlite3

# Load the CSV
df = pd.read_csv('Mumbai_restaurants.csv')

# Connect to SQLite DB (this will create mumbai_restaurants.db)
conn = sqlite3.connect('mumbai_restaurants.db')

# Import the data into a new table
df.to_sql('restaurants', conn, if_exists='replace', index=False)

print("✅ Data imported successfully!")
conn.close()


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# --- Connect to SQLite ---
conn = sqlite3.connect("mumbai_restaurants.db")

# --- Load full dataset ---
df = pd.read_sql("SELECT * FROM restaurants", conn)

# --- Clean 'Cost' column ---
df["Clean_Cost"] = df["Cost"].str.extract(r'₹?([\d,]+)').replace(",", "", regex=True).astype(float)

# --- Clean 'Delivery time' column ---
df["Delivery_Minutes"] = df["Delivery time"].str.extract(r'(\d+)').astype(float)

# --- RATING vs COST SCATTERPLOT ---
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Clean_Cost", y="Rating")
plt.title("Ratings vs Cost")
plt.xlabel("Cost for Two (₹)")
plt.ylabel("Rating")
plt.grid(True)
plt.tight_layout()
plt.show()

# --- DELIVERY TIME HISTOGRAM ---
plt.figure(figsize=(8, 5))
sns.histplot(df["Delivery_Minutes"].dropna(), bins=15, kde=True)
plt.title("Delivery Time Distribution")
plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# --- TOP CUISINES BAR CHART ---
# Expand comma-separated cuisines
specials_exploded = df["Specials"].dropna().str.split(',').explode().str.strip()
top_cuisines = specials_exploded.value_counts().head(10)

plt.figure(figsize=(8, 5))
sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette="viridis")
plt.title("Top 10 Cuisines")
plt.xlabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# --- DISCOUNT USAGE PIE CHART ---
df["Discount_50"] = df["Coupons"].str.contains("50%", na=False)
discount_counts = df["Discount_50"].value_counts().rename({True: "50%+ Discount", False: "Others"})

fig = px.pie(values=discount_counts.values, names=discount_counts.index, title="Restaurants Offering 50%+ Discount")
fig.show()
