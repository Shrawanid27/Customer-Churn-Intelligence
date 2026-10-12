import pandas as pd

# Load dataset
df = pd.read_csv("customer_churn_5000.csv")

print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATASET INFORMATION")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

print("\nSTATISTICAL SUMMARY")
print(df.describe())

print("\nCHURN COUNT")
print(df["Churn"].value_counts())

print("\nCHURN PERCENTAGE")
print(df["Churn"].value_counts(normalize=True) * 100)

# ==========================================
# STEP 3: DATA CLEANING
# ==========================================

print("\n" + "="*50)
print("DATA CLEANING")
print("="*50)

# 1. Check data types
print("\nDATA TYPES")
print(df.dtypes)

# 2. Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# 3. Check duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# 4. Check duplicate Customer IDs
print("\nDUPLICATE CUSTOMER IDs")
print(df["Customer_ID"].duplicated().sum())

# 5. Check unique values in categorical columns
print("\nGENDER VALUES")
print(df["Gender"].unique())

print("\nCITY VALUES")
print(df["City"].unique())

print("\nCONTRACT TYPES")
print(df["Contract_Type"].unique())

print("\nPAYMENT METHODS")
print(df["Payment_Method"].unique())

print("\nINTERNET SERVICES")
print(df["Internet_Service"].unique())

print("\nCHURN VALUES")
print(df["Churn"].unique())

# 6. Check numerical ranges
print("\nAGE RANGE")
print(df["Age"].min(), "to", df["Age"].max())

print("\nTENURE RANGE")
print(df["Tenure_Months"].min(), "to", df["Tenure_Months"].max())

print("\nSATISFACTION SCORE RANGE")
print(
    df["Satisfaction_Score"].min(),
    "to",
    df["Satisfaction_Score"].max()
)

print("\nSUPPORT TICKETS RANGE")
print(
    df["Support_Tickets"].min(),
    "to",
    df["Support_Tickets"].max()
)