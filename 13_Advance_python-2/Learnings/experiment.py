import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a sample dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Sales': [1200, 1500, 1100, 1800, 2500, 2200]
}

# Step 2: Create a DataFrame
df = pd.DataFrame(data)

# Step 3: Analyze data - Add a column for Sales Growth
df['Growth (%)'] = df['Sales'].pct_change().fillna(0) * 100

# Step 4: Print the DataFrame
print("Sales Data:")
print(df)

# Step 5: Visualize the data with a bar plot
plt.figure(figsize=(8, 5))
plt.bar(df['Month'], df['Sales'], color='skyblue', label='Monthly Sales')

# Add Growth Line
plt.plot(df['Month'], df['Sales'], marker='o', color='orange', label='Sales Trend')

# Add labels and title
plt.title('Monthly Sales Analysis')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
