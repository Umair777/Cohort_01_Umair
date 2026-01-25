import pandas as pd

# Sample DataFrame
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print("Original DataFrame:")
print(df)

selected_columns = df[['Name', 'Salary']]
print("\nSelected Columns:")
print(selected_columns)

print("\nDataFrame Info:")
df.info()


print("\nType of selected_columns:")
print(type(selected_columns))

# Access the value on the first row and the first column

# df.iloc[0, 0]
print("\nValue at first row and first column:")
print(df.iloc[0, 0])
print("\nValue at second row and third column:")
print(df.iloc[1, 2])

print("\nValue at first row and 'Salary' column:")
print(df.loc[0, 'Salary'])

df2 = df
df2 = df2.set_index('Name')
print("\nDataFrame with 'Name' as index:")
print(df2)

#To display the first 5 rows of new dataframe
df2.head()
# access the column using the name
print(df2.loc['Jane', 'Salary'])

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"


'''
Output:
Original DataFrame:
   Name  ID       Department  Salary
0  Rose   1  Architect Group  100000
1  John   2   Software Group   80000
2  Jane   3      Design Team   50000
3  Mary   4   Infrastructure   60000

Selected Columns:
   Name  Salary
0  Rose  100000
1  John   80000
2  Jane   50000
3  Mary   60000

DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 4 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Name        4 non-null      object
 1   ID          4 non-null      int64 
 2   Department  4 non-null      object
 3   Salary      4 non-null      int64 
dtypes: int64(2), object(2)
memory usage: 256.0+ bytes

Type of selected_columns:
<class 'pandas.core.frame.DataFrame'>

Value at first row and first column:
Rose

Value at second row and third column:
Software Group

Value at first row and 'Salary' column:
100000

DataFrame with 'Name' as index:
      ID       Department  Salary
Name                             
Rose   1  Architect Group  100000
John   2   Software Group   80000
Jane   3      Design Team   50000
Mary   4   Infrastructure   60000
50000'''