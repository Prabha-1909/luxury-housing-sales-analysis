import pandas as pd

df = pd.read_csv("data/raw/luxury_housing_bangalore.csv")

print("Shape of dataset:", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSample Data:")
print(df.head())