import pandas as pd
import matplotlib.pyplot as plt

# Load CSV Files
transactions = pd.read_csv("personal_transactions.csv")
budget = pd.read_csv("Budget.csv")

# Convert Date column to datetime
transactions["Date"] = pd.to_datetime(transactions["Date"], format="%m/%d/%Y")

# Ensure Category column is consistent
transactions["Category"] = transactions["Category"].str.strip()
budget["Category"] = budget["Category"].str.strip()

# Summarize total spending per category
category_spending = transactions[transactions["Transaction Type"] == "debit"].groupby("Category")["Amount"].sum().reset_index()

# Merge with Budget
merged_data = budget.merge(category_spending, on="Category", how="left").fillna(0)
merged_data.rename(columns={"Amount": "Actual Spending"}, inplace=True)

# Identify categories that exceed budget
merged_data["Over Budget"] = merged_data["Actual Spending"] > merged_data["Budget"]

# Summarize spending per account
account_summary = transactions.groupby("Account Name")["Amount"].sum().reset_index()

# Flag Unusual Transactions (above $500)
unusual_transactions = transactions[transactions["Amount"] > 500]

# Print Summary
print("\n==== Budget vs. Actual Spending ====")
print(merged_data)

print("\n==== Spending Summary by Account ====")
print(account_summary)

print("\n==== Unusual Transactions (Above $500) ====")
print(unusual_transactions)

# Visualization: Spending vs. Budget
plt.figure(figsize=(10, 5))
plt.bar(merged_data["Category"], merged_data["Budget"], label="Budget", alpha=0.7)
plt.bar(merged_data["Category"], merged_data["Actual Spending"], label="Actual Spending", alpha=0.7)
plt.xticks(rotation=45, ha="right")
plt.xlabel("Category")
plt.ylabel("Amount ($)")
plt.title("Budget vs. Actual Spending")
plt.legend()
plt.tight_layout()
plt.show()

# Save Reports
merged_data.to_csv("budget_vs_spending_report.csv", index=False)
account_summary.to_csv("account_summary_report.csv", index=False)
unusual_transactions.to_csv("unusual_transactions.csv", index=False)

print("\n✅ Reports Saved Successfully!")
