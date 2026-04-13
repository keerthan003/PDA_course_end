import pandas as pd
import numpy as np

# ─────────────────────────────────────────
#  Sample Dataset
# ─────────────────────────────────────────
data = {
    "Age":          [22, 35, 45, 52, 23],
    "Gender":       ["Male", "Female", "Male", "Female", "Male"],
    "Balance":      [2000, 5000, 7000, 10000, 3000],
    "Income":       [25000, 50000, 60000, 70000, 30000],
    "Loan":         ["No", "Yes", "No", "Yes", "No"],
    "Transactions": [15, 30, 25, 20, 18],
}

df = pd.DataFrame(data)

# ─────────────────────────────────────────
#  1. DATASET PREVIEW
# ─────────────────────────────────────────
print("--- DATASET PREVIEW ---")
print(df.to_string())
print()

# ─────────────────────────────────────────
#  2. MISSING VALUES
# ─────────────────────────────────────────
print("--- MISSING VALUES ---")
print(df.isnull().sum().to_string())
print("dtype: int64")
print()

# ─────────────────────────────────────────
#  3. STATISTICS  (numeric columns only)
# ─────────────────────────────────────────
print("--- STATISTICS ---")
numeric_cols = ["Age", "Balance", "Income", "Transactions"]
print(df[numeric_cols].describe().to_string())
print()

# ─────────────────────────────────────────
#  4. BALANCE BY AGE GROUP
# ─────────────────────────────────────────
def age_group(age):
    if age < 30:
        return "Young"
    elif age < 45:
        return "Adult"
    else:
        return "Senior"

df["Age_Group"] = df["Age"].apply(age_group)

print("--- BALANCE BY AGE GROUP ---")
balance_by_age = df.groupby("Age_Group")["Balance"].mean()

# Enforce display order
order = ["Young", "Adult", "Senior"]
balance_by_age = balance_by_age.reindex([g for g in order if g in balance_by_age.index])

print(balance_by_age.to_string())
print("Name: Balance, dtype: float64")
print()

# ─────────────────────────────────────────
#  5. CORRELATION MATRIX
# ─────────────────────────────────────────
print("--- CORRELATION MATRIX ---")
corr = df[numeric_cols].corr()
print(corr.to_string())
print()

# ─────────────────────────────────────────
#  6. INSIGHTS
# ─────────────────────────────────────────
print("--- INSIGHTS ---")

# Insight 1: age vs transactions
young_txn  = df[df["Age_Group"] == "Young"]["Transactions"].mean()
senior_txn = df[df["Age_Group"] == "Senior"]["Transactions"].mean()
if young_txn > senior_txn:
    print("Young customers → more transactions")
else:
    print("Senior customers → more transactions")

# Insight 2: age vs balance
young_bal  = df[df["Age_Group"] == "Young"]["Balance"].mean()
senior_bal = df[df["Age_Group"] == "Senior"]["Balance"].mean()
if senior_bal > young_bal:
    print("Older customers → higher balance")
else:
    print("Younger customers → higher balance")

# Insight 3: income-balance correlation
income_balance_corr = df["Income"].corr(df["Balance"])
if income_balance_corr > 0.5:
    print("Income influences financial behavior")
else:
    print("Income has weak correlation with financial behavior")
