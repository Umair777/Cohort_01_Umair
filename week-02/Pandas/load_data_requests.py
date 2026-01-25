import pandas as pd
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"
filename = "Product-sales.csv"

response = requests.get(url)
response.raise_for_status()


with open(filename, "wb") as f:
    f.write(response.content)

df = pd.read_csv(filename)
print(df.head())

'''
Output:
   OrderID     Product     Category  Quantity  Price  Total   OrderDate CustomerCity
0        1      Laptop  Electronics         2    800   1600  2022-01-10     New York
1        2  Smartphone  Electronics         3    600   1800  2022-02-15  Los Angeles
2        3  Desk Chair    Furniture         5    150    750  2022-03-12      Chicago
3        4    Notebook   Stationery        10      2     20  2022-04-05      Houston
4        5     Monitor  Electronics         1    300    300  2022-05-21        Miami'''
