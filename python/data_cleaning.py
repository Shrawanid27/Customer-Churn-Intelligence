import pandas as pd

# Load dataset
df = pd.read_csv("customer_churn_5000.csv")

print("Original Shape:", df.shape)

# ==========================================
# 1. Remove duplicate rows
# ==========================================

df.drop_duplicates(inplace=True)

print("After removing duplicates:", df.shape)


# ==========================================
# 2. Remove duplicate Customer IDs
# ==========================================

df.drop_duplicates(
    subset=["Customer_ID"],
    keep="first",
    inplace=True
)

print("After checking Customer IDs:", df.shape)


# ==========================================
# 3. Check missing values
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())


# ==========================================
# 4. Convert numerical columns
# ==========================================

numeric_columns = [
    "Age",
    "Tenure_Months",
    "Monthly_Charges",
    "Total_Charges",
    "Support_Tickets",
    "Satisfaction_Score",
    "Usage_Hours",
    "Last_Login_Days"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# ==========================================
# 5. Handle missing numerical values
# ==========================================

for column in numeric_columns:
    df[column] = df[column].fillna(
        df[column].median()
    )


# ==========================================
# 6. Handle missing categorical values
# ==========================================

categorical_columns = [
    "Gender",
    "City",
    "Contract_Type",
    "Payment_Method",
    "Internet_Service",
    "Churn",
    "Churn_Reason"
]

for column in categorical_columns:
    df[column] = df[column].fillna(
        df[column].mode()[0]
    )


# ==========================================
# 7. Check final missing values
# ==========================================

print("\nFinal Missing Values:")
print(df.isnull().sum())


# ==========================================
# 8. Save cleaned dataset
# ==========================================

df.to_csv(
    "customer_churn_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")

print("Final Shape:", df.shape)