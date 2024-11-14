import pandas as pd 

# Load the CSV file into a DataFrame
# Assuming 'sample.csv' is the file to be loaded
df = pd.read_csv(r'C:\Users\Admin\Desktop\pda\all\example.csv') 

# (a) Visualize the first and last 10 records
print("First 10 records:\n", df.head(10)) 
print("\nLast 10 records:\n", df.tail(10)) 

# (b) Get the shape, index, and column details
print("\nShape of the DataFrame:", df.shape) 
print("\nIndex of the DataFrame:", df.index) 
print("\nColumns of the DataFrame:", df.columns) 

# (c) Select/Delete records based on conditions
# Selecting records where 'Age' column is greater than 25
selected_records = df[df['Age'] > 25] 
print("\nRecords where Age > 25:\n", selected_records) 

# Deleting the 'City' column
df_deleted_column = df.drop(columns=['City']) 
print("\nDataFrame after deleting 'City' column:\n", df_deleted_column) 

# (d) Perform ranking and sorting operations
# Ranking based on the 'Age' column
df['Age Rank'] = df['Age'].rank(ascending=False) 
print("\nDataFrame with 'Age' ranked:\n", df[['Name', 'Age', 'Age Rank']]) 

# Sorting by 'Age' column in ascending order
sorted_df = df.sort_values(by='Age', ascending=True) 
print("\nDataFrame sorted by 'Age':\n", sorted_df) 

# (e) Perform statistical operations on a given column
print("\nMean of 'Age':", df['Age'].mean()) 
print("Median of 'Salary':", df['Salary'].median()) 
print("Standard Deviation of 'Salary':", df['Salary'].std()) 

# (f) Find the count and uniqueness of the given categorical values
print("\nCount of unique values in 'City':\n", df['City'].value_counts()) 
print("\nUnique values in 'City':", df['City'].unique()) 

# (g) Rename single/multiple columns
df_renamed = df.rename(columns={'Name': 'Employee Name', 'Age': 'Employee Age'}) 
print("\nDataFrame after renaming columns:\n", df_renamed) 
