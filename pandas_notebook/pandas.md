# Pandas Training Resource
## Introduction to Pandas
Pandas is a powerful and flexible open-source data manipulation and analysis library for Python. It provides data structures and functions needed to work with structured data seamlessly.

## Table of Contents
1. Introduction to Pandas
2. DataFrame Data Structure
3. Reading and Writing CSV Files Using DataFrame
4. Manipulating DataFrame


## 1. Introduction to Pandas
Pandas is built on top of NumPy and provides data structures like Series (one-dimensional) and DataFrame (two-dimensional) for data manipulation.

### Installing Pandas
You can install Pandas using pip:

```bash
pip install pandas
```
Importing Pandas
To use Pandas, you need to import it in your Python script:

```python
import pandas as pd
```

## 2. DataFrame Data Structure
A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).

### Creating a DataFrame
You can create a DataFrame from a variety of inputs such as lists, dictionaries, or NumPy arrays.

```python
import pandas as pd

# Creating DataFrame from a dictionary
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)
print(df)
```

## 3. Reading and Writing CSV Files Using DataFrame
### Reading CSV Files
You can read a CSV file into a DataFrame using the read_csv function.

``` python
df = pd.read_csv('data.csv')
print(df)
```

### Writing CSV Files
You can write a DataFrame to a CSV file using the to_csv function.

```python
df.to_csv('output.csv', index=False)
```

## 4. Manipulating DataFrame
### Viewing Data
```python
# Display the first few rows
print(df.head())

# Display the last few rows
print(df.tail())

# Display summary statistics
print(df.describe())
```

### Selecting Data
```python
# Select a single column
print(df['Name'])

# Select multiple columns
print(df[['Name', 'Age']])

# Select rows by index
print(df.iloc[0])  # First row
print(df.iloc[1:3])  # Second and third rows

# Select rows by condition
print(df[df['Age'] > 30])
```

### Modifying Data
```python
# Add a new column
df['Country'] = ['USA', 'France', 'Germany', 'UK']
print(df)

# Update values
df.loc[df['Name'] == 'John', 'Age'] = 29
print(df)

# Drop a column
df = df.drop(columns=['Country'])
print(df)

# Drop a row
df = df.drop(index=0)  # Drop the first row
print(df)
```

### Handling Missing Data
```python
# Check for missing values
print(df.isnull())

# Drop rows with missing values
df = df.dropna()
print(df)

# Fill missing values
df = df.fillna(value={'Age': 30})
print(df)
```

# Conclusion

This training resource provides a brief overview of Pandas and some essential operations you can perform with DataFrames. For more detailed information, refer to the official Pandas documentation.