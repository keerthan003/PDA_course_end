# Bank Customer Demographic Analysis

A Python-based data analysis project that explores customer demographics and financial behavior using pandas. It uncovers patterns across age groups, income levels, balances, and transaction activity.

---


## Overview

This project performs an end-to-end demographic analysis of bank customers. It covers data exploration, missing value detection, descriptive statistics, age-group segmentation, and correlation analysis — all printed in a clean, structured console format.

---

## Dataset

The project uses a sample dataset with the following columns:

| Column         | Type    | Description                          |
|----------------|---------|--------------------------------------|
| `Age`          | int     | Customer age                         |
| `Gender`       | string  | Male / Female                        |
| `Balance`      | int     | Account balance (₹)                  |
| `Income`       | int     | Annual income (₹)                    |
| `Loan`         | string  | Whether customer has a loan (Yes/No) |
| `Transactions` | int     | Number of transactions               |

> You can replace the sample data dictionary with your own CSV file using `pd.read_csv("your_file.csv")`.

---

## Features

- ✅ Dataset preview
- ✅ Missing value detection
- ✅ Descriptive statistics (count, mean, std, min, percentiles, max)
- ✅ Average balance segmented by age group (Young / Adult / Senior)
- ✅ Correlation matrix across numeric features
- ✅ Auto-generated key insights

---

## Project Structure

```
bank-customer-demographic-analysis/
│
├── bank_customer_analysis.py   # Main analysis script
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

---

## Usage

Run the analysis script directly:

```bash
python bank_customer_analysis.py
```

To use your own dataset, replace the `data` dictionary in the script with:

```python
df = pd.read_csv("your_dataset.csv")
```

---

## Sample Output

```
--- DATASET PREVIEW ---
   Age  Gender  Balance  Income Loan  Transactions
0   22    Male     2000   25000   No            15
1   35  Female     5000   50000  Yes            30
...

--- MISSING VALUES ---
Age             0
Gender          0
Balance         0
...

--- STATISTICS ---
              Age      Balance       Income  Transactions
count    10.00000    10.000000    10.000000     10.000000
mean     35.50000  5750.000000  48700.000000     22.700000
...

--- BALANCE BY AGE GROUP ---
Age_Group
Young     3125.0
Adult     6500.0
Senior    9500.0
Name: Balance, dtype: float64

--- CORRELATION MATRIX ---
                  Age   Balance    Income  Transactions
Age          1.000000  0.968610  0.971311      0.199241
Balance      0.968610  1.000000  0.979792      0.232277
...

--- INSIGHTS ---
Young customers → more transactions
Older customers → higher balance
Income influences financial behavior
```

---


