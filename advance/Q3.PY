import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

print("\nStatistics:")
print(df.describe())

print("\nFiltered DataFrame (Age > 28):")
print(df[df['Age'] > 28])
