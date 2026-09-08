import pandas as pd

# Load the raw dataset
df = pd.read_csv("data/raw_data.csv")

print("========== ORIGINAL DATA ==========")
print(df)

print("\n========== MISSING VALUES BEFORE CLEANING ==========")
print(df.isnull().sum())

# Create a copy for cleaning
cleaned_df = df.copy()

# Fill missing customer names
cleaned_df["First_Name"] = cleaned_df["First_Name"].fillna("Unknown")

# Fill missing quantity
cleaned_df["Quantity"] = cleaned_df["Quantity"].fillna(0)

# Fill missing status
cleaned_df["Status"] = cleaned_df["Status"].fillna("Pending")


print("\n========== ROW COUNT CHECK ==========")

print("Original rows:", len(df))
print("Cleaned rows:", len(cleaned_df))

print("\n========== MISSING VALUES AFTER CLEANING ==========")
print(cleaned_df.isnull().sum())

print("\n========== CLEANED DATA ==========")
print(cleaned_df)

# Clean city names
cleaned_df["City"] = cleaned_df["City"].str.strip().str.title()

print("\n========== CITIES AFTER CLEANING ==========")
print(cleaned_df["City"].unique())


# Convert all date formats into standard date format
cleaned_df["Order_Date"] = pd.to_datetime(
    cleaned_df["Order_Date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

print("\n========== ORDER DATES AFTER CLEANING ==========")
print(cleaned_df["Order_Date"].head(10))

print("\n========== INVALID DATES ==========")
print(cleaned_df["Order_Date"].isnull().sum())

# Convert Quantity to numeric
cleaned_df["Quantity"] = pd.to_numeric(
    cleaned_df["Quantity"],
    errors="coerce"
)

# Convert Unit_Price to numeric
cleaned_df["Unit_Price"] = pd.to_numeric(
    cleaned_df["Unit_Price"],
    errors="coerce"
)

print("\n========== DATA TYPES AFTER NUMERIC CLEANING ==========")
print(cleaned_df[["Quantity", "Unit_Price"]].dtypes)

print("\n========== MISSING NUMERIC VALUES ==========")
print(cleaned_df[["Quantity", "Unit_Price"]].isnull().sum())

# Clean Status values
cleaned_df["Status"] = (
    cleaned_df["Status"]
    .str.strip()
    .str.title()
)

print("\n========== STATUS AFTER CLEANING ==========")
print(cleaned_df["Status"].unique())

# Check duplicate records
duplicate_rows = cleaned_df[cleaned_df.duplicated(keep=False)]

print("\n========== DUPLICATE RECORDS ==========")
print(duplicate_rows)

print("\n========== DUPLICATE ROW COUNT ==========")
print(cleaned_df.duplicated().sum())

# Save the cleaned dataset
cleaned_df.to_csv(
    "output/cleaned_sales_data.csv",
    index=False
)

print("\n========== FILE SAVED ==========")
print("Cleaned dataset saved successfully!")

# Final Data Quality Checks

print("\nFinal Data Quality Report")
print("-------------------------")

print("Total rows:", cleaned_df.shape[0])
print("Total columns:", cleaned_df.shape[1])

print("\nMissing values after cleaning:")
print(cleaned_df.isnull().sum())

print("\nDuplicate records after cleaning:")
print(cleaned_df.duplicated().sum())

print("\nFinal data information:")
cleaned_df.info()