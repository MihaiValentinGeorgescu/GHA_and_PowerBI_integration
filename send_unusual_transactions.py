import requests
import pandas as pd


POWER_BI_URL_UNUSUAL_TRANSACTIONS = "https://api.powerbi.com/beta/2d8cc8ba-8dda-4334-9e5c-fac2092e9bac/datasets/9a0fc937-eb67-4e0e-9372-330e1ad7370a/rows?experience=power-bi&key=Inf%2FpYNdXib3CiuiIkX2Cr0r1%2FHCgfuz4e1ZrRqeStwMZhGJfpnaYg2grEQgPy0vLFplTa%2BparLqIjIZHrhLbA%3D%3D"

# Load your processed data
df = pd.read_csv("unusual_transactions.csv")

# Convert data to Power BI JSON format
data = []
for _, row in df.iterrows():
    data.append({
        "Account Name": row["Account Name"],
        "Amount": row["Amount"],
        "Date": row["Date"],
        "Description": row["Description"],
        "Category": row["Category"],
        "Transaction Type": row["Transaction Type"],
    })

# Send data to Power BI API
response = requests.post(POWER_BI_URL_UNUSUAL_TRANSACTIONS, json=data)

# Check response status
if response.status_code == 200:
    print("✅ Data from unusual tranzactions report was sent successfully to Power BI!")
else:
    print(f"❌ Error sending data: {response.text}")