import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("customer_churn_cleaned.csv")

# Churn count
print("Churn Count:")
print(df["Churn"].value_counts())

# Churn percentage
print("\nChurn Percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)

# Create graph
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Churn"
)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.show()

# Churn by Contract Type
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Contract_Type",
    hue="Churn"
)

plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")

plt.show()


# Churn Rate by Contract Type
contract_churn = pd.crosstab(
    df["Contract_Type"],
    df["Churn"],
    normalize="index"
) * 100

print("\nChurn Rate by Contract Type:")
print(contract_churn)

# Churn by Satisfaction Score
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Satisfaction_Score",
    hue="Churn"
)

plt.title("Customer Churn by Satisfaction Score")
plt.xlabel("Satisfaction Score")
plt.ylabel("Number of Customers")

plt.show()

# Churn by Support Tickets
plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="Support_Tickets",
    hue="Churn"
)

plt.title("Customer Churn by Support Tickets")
plt.xlabel("Number of Support Tickets")
plt.ylabel("Number of Customers")

plt.show()

# Churn by Payment Method
plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="Payment_Method",
    hue="Churn"
)

plt.title("Customer Churn by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")

plt.xticks(rotation=15)

plt.show()

# Churn by Internet Service
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Internet_Service",
    hue="Churn"
)

plt.title("Customer Churn by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")

plt.show()

# Churn Reason Analysis

churned_customers = df[df["Churn"] == "Yes"]

reason_counts = churned_customers["Churn_Reason"].value_counts()

print("\nChurn Reasons:")
print(reason_counts)

# Create graph
plt.figure(figsize=(9, 5))

sns.countplot(
    data=churned_customers,
    x="Churn_Reason",
    order=reason_counts.index
)

plt.title("Customer Churn Reasons")
plt.xlabel("Churn Reason")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20)

plt.show()

# Monthly Charges vs Churn

plt.figure(figsize=(9, 5))

sns.boxplot(
    data=df,
    x="Churn",
    y="Monthly_Charges"
)

plt.title("Monthly Charges vs Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")

plt.show()

# Tenure vs Churn

plt.figure(figsize=(9, 5))

sns.boxplot(
    data=df,
    x="Churn",
    y="Tenure_Months"
)

plt.title("Tenure vs Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Tenure (Months)")

plt.show()

# Revenue at Risk

churned_customers = df[df["Churn"] == "Yes"]

revenue_at_risk = churned_customers["Monthly_Charges"].sum()

print("\nRevenue at Risk:")
print(round(revenue_at_risk, 2))