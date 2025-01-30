import requests
import pandas as pd


POWER_BI_URL_ACCOUNT_SUMMARY_REPORT = "https://api.powerbi.com/beta/2d8cc8ba-8dda-4334-9e5c-fac2092e9bac/datasets/4ac7c731-c11a-4d31-ac6f-69f933f3c4c2/rows?experience=power-bi&key=etH6g7JcSAUaSu0fr%2F497E3DfOu8t%2FwxN%2FuaqzGMC9N7zi5wnuI7As0LN%2FL96JOiCUB6p3YuVRvHEaLS30fZEQ%3D%3D"

# Load your processed data
df = pd.read_csv("account_summary_report.csv")

# Convert data to Power BI JSON format
data = []
for _, row in df.iterrows():
    data.append({
        "Account Name": row["Account Name"],
        "Amount": row["Amount"]
    })

# Send data to Power BI API
response = requests.post(POWER_BI_URL_ACCOUNT_SUMMARY_REPORT, json=data)

# Check response status
if response.status_code == 200:
    print("✅ Data from account summary report was sent successfully to Power BI!")
else:
    print(f"❌ Error sending data: {response.text}")