import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
# Replace 'sample.csv' with the actual path to your file
df = pd.read_csv('C:\Users\Admin\Desktop\pda\all\example.csv')

# (a) Handle Missing Data
# Detect missing values
print("\nMissing Data:\n", df.isnull().sum())

# Drop rows with missing values
df_cleaned = df.dropna()
print("\nDataFrame after dropping missing values:\n", df_cleaned)

# Fill missing values with the median for numeric columns
df_filled = df.fillna(df.median(numeric_only=True))
print("\nDataFrame after filling missing values with median:\n", df_filled)

# (b) Transform Data Using apply() and map()
# Applying a custom function to square the 'Age' column
df['Age Squared'] = df['Age'].apply(lambda x: x ** 2)
print("\nDataFrame after applying function (Age Squared):\n", df[['Name', 'Age', 'Age Squared']])

# Using map() to substitute values in the 'City' column
city_mapping = {'New York': 'NY', 'Los Angeles': 'LA', 'Chicago': 'CHI'}
df['City Short'] = df['City'].map(city_mapping)
print("\nDataFrame after using map() to transform 'City':\n", df[['City', 'City Short']])

# (c) Detect and Filter Outliers
# Detect outliers using the IQR (Interquartile Range) method
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Age'] < (Q1 - 1.5 * IQR)) | (df['Age'] > (Q3 + 1.5 * IQR))]
print("\nDetected outliers in 'Age':\n", outliers)

# Filter out the outliers
df_filtered = df[~((df['Age'] < (Q1 - 1.5 * IQR)) | (df['Age'] > (Q3 + 1.5 * IQR)))]
print("\nDataFrame after filtering out outliers:\n", df_filtered)

# (d) Perform Vectorized String Operations on Pandas Series
# Convert 'Name' column to lowercase
df['Name Lower'] = df['Name'].str.lower()
print("\nDataFrame after converting 'Name' to lowercase:\n", df[['Name', 'Name Lower']])

# Check if 'Name' contains a specific substring (e.g., 'a')
df['Contains A'] = df['Name'].str.contains('a', case=False)
print("\nDataFrame after checking if 'Name' contains the letter 'a':\n", df[['Name', 'Contains A']])

# (e) Visualize Data Using Different Plots
plt.figure(figsize=(10, 8))

# Line Plot: Age vs Salary
plt.subplot(2, 2, 1)
plt.plot(df['Age'], df['Salary'], marker='o')
plt.title('Line Plot: Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')

# Bar Plot: City Count
plt.subplot(2, 2, 2)
df['City'].value_counts().plot(kind='bar', color='orange')
plt.title('Bar Plot: City Count')
plt.xlabel('City')
plt.ylabel('Count')

# Histogram: Age Distribution
plt.subplot(2, 2, 3)
df['Age'].plot(kind='hist', bins=10, color='lightblue', edgecolor='black')
plt.title('Histogram: Age Distribution')
plt.xlabel('Age')

# Density Plot: Salary Distribution
plt.subplot(2, 2, 4)
df['Salary'].plot(kind='density', color='green')
plt.title('Density Plot: Salary Distribution')
plt.xlabel('Salary')

# Display all plots
plt.tight_layout()
plt.show()
