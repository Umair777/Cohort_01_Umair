import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

# Pandas downloads the CSV directly
df = pd.read_csv(url)

print(df.head())
