import pandas as pd

df = pd.read_csv("data/raw/luxury_housing_bangalore.csv")

# -----------------------------
# Clean Ticket_Price_Cr column
# -----------------------------

# Remove 'Cr' and any commas if present
df["Ticket_Price_Cr"] = df["Ticket_Price_Cr"].str.replace("Cr", "", regex=False)
df["Ticket_Price_Cr"] = df["Ticket_Price_Cr"].str.replace(",", "", regex=False)

# Convert to numeric
df["Ticket_Price_Cr"] = pd.to_numeric(df["Ticket_Price_Cr"], errors="coerce")

print("Updated Data Types:\n")
print(df.dtypes)

print("\nMissing Values After Conversion:\n")
print(df.isnull().sum())

df["Micro_Market"] = df["Micro_Market"].str.title()
df["Developer_Name"] = df["Developer_Name"].str.title()
df["Project_Name"] = df["Project_Name"].str.title()
# Fill numeric missing values with median
df["Unit_Size_Sqft"] = df["Unit_Size_Sqft"].fillna(df["Unit_Size_Sqft"].median())
df["Ticket_Price_Cr"] = df["Ticket_Price_Cr"].fillna(df["Ticket_Price_Cr"].median())
df["Amenity_Score"] = df["Amenity_Score"].fillna(df["Amenity_Score"].median())

df.to_csv("data/processed/luxury_housing_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")