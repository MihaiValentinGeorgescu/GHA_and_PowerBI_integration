import requests
import pandas as pd

# Your Power BI Push Dataset URL (replace with your actual URL)
POWER_BI_URL = "https://api.powerbi.com/beta/2d8cc8ba-8dda-4334-9e5c-fac2092e9bac/datasets/9a12d9a4-54ba-483a-82c7-1d5012d83310/rows?experience=power-bi&key=impJHC%2B4pX25yrNsiLk0TVWpKdPFoWKt2qCGzLCGkIXK%2FW%2BbdlikPxnIC6tqydiwnZgmTqJs13u1rfBHBct7zQ%3D%3D"

# Load your processed data
df = pd.read_csv("budget_vs_spending_report.csv")

# Convert data to Power BI JSON format
data = []
for _, row in df.iterrows():
    data.append({
        "Category": row["Category"],
        "Budget": row["Budget"],
        "Actual Spending": row["Actual Spending"],
        "Over Budget": row["Over Budget"]
    })

# Send data to Power BI API
response = requests.post(POWER_BI_URL, json=data)

# Check response status
if response.status_code == 200:
    print("✅ Data sent successfully to Power BI!")
else:
    print(f"❌ Error sending data: {response.text}")