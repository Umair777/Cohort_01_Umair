import pandas as pd
import aiohttp
import asyncio

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

print("Starting asynchronous download...")
async def download(url, filename):
    
    print(f"Preparing to download {url}...")
    async with aiohttp.ClientSession() as session:
        
        print(f"Sending request to {url}...")
        async with session.get(url) as response:
            
            print(f"Response status: {response.status}")
            if response.status == 200:
                
                print(f"Downloading {filename}...")
                with open(filename, "wb") as f:
                    f.write(await response.read())

async def main():
    await download(url, "Product-sales2.csv")
    df = pd.read_csv("Product-sales2.csv")
    print(df.head())

if __name__ == "__main__":
    asyncio.run(main())
    
'''Output:
Preparing to download https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv...
Sending request to https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv...
Response status: 200
Downloading Product-sales2.csv...
   OrderID     Product     Category  Quantity  Price  Total   OrderDate CustomerCity
0        1      Laptop  Electronics         2    800   1600  2022-01-10     New York
1        2  Smartphone  Electronics         3    600   1800  2022-02-15  Los Angeles
2        3  Desk Chair    Furniture         5    150    750  2022-03-12      Chicago
3        4    Notebook   Stationery        10      2     20  2022-04-05      Houston
4        5     Monitor  Electronics         1    300    300  2022-05-21        Miami
'''
