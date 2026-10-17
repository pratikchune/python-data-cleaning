
import pandas as pd

# Load raw dataset
df = pd.read_csv("sales.csv")

print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing values
for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            mode = df[col].mode()
            if not mode.empty:
                df[col] = df[col].fillna(mode.iloc[0])
            else:
                df[col] = df[col].fillna("Unknown")

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("\nCleaning completed!")
