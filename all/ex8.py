import pandas as pd 
import numpy as np 
# Series from a list 
list_data = [10, 20, 30, 40, 50] 
series_from_list = pd.Series(list_data) 
print("Series from List:\n", series_from_list) 
#Series from a dictionary 
dict_data = {'a': 100, 'b': 200, 'c': 300} 
series_from_dict = pd.Series(dict_data) 
print("\nSeries from Dictionary:\n", series_from_dict) 
#Series from a NumPy array 
numpy_array = np.array([1, 2, 3, 4, 5]) 
series_from_array = pd.Series(numpy_array) 
print("\nSeries from NumPy Array:\n", series_from_array) 
#Create a DataFrame from various inputs 
# DataFrame from a dictionary 
data_dict = { 
'Name': ['Alice', 'Bob', 'Charlie'], 
'Age': [24, 27, 22], 
'City': ['New York', 'Los Angeles', 'Chicago'] 
} 
df_from_dict = pd.DataFrame(data_dict) 
print("\nDataFrame from Dictionary:\n", df_from_dict) 
# DataFrame from a list of lists 
data_list = [ 
['John', 28, 'London'], 
['Anna', 24, 'Paris'], 
['Mike', 32, 'Berlin'] 
] 
df_from_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City']) 
print("\nDataFrame from List of Lists:\n", df_from_list) 
# DataFrame from a NumPy array 
numpy_array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
df_from_numpy = pd.DataFrame(numpy_array_2d, columns=['A', 'B', 'C']) 
print("\nDataFrame from NumPy Array:\n", df_from_numpy) 
