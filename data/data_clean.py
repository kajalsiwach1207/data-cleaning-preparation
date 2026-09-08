import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw_data.csv")

print("========== DATASET PREVIEW ==========")
print(df.head())

print("\n========== LAST FIVE ROWS ==========")
print(df.tail())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

print("\n========== UNIQUE CITIES ==========")
print(df["City"].unique())

print("\n========== UNIQUE STATUSES ==========")
print(df["Status"].unique())

print("\n========== ORDER DATE VALUES ==========")
print(df["Order_Date"].head(10))

print("\n========== QUANTITY VALUES ==========")
print(df["Quantity"].unique())

print("\n========== UNIT PRICE VALUES ==========")
print(df["Unit_Price"].unique())