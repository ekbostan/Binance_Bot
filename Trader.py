import json
import requests
import pandas as pd
import datetime

market_symbol = "btcusd"
url = f"https://www.bitstamp.net/api/v2/ohlc/{market_symbol}/"

start = "2023-01-01"
end = "2023-04-06"

dates = pd.date_range(start,end,freq="6H")
dates = [ int(x.value/10**9) for x in list(dates)]

master_data = []


for first,last in zip(dates,dates[1:]):
    params = {
        "step":60,
        "limit":1000,
        "start":first,
        "end":last
    }

    data  = requests.get(url,params=params)
    master_data += data.json()["data"]["ohlc"]
df = pd.DataFrame(master_data)
df = df.drop_duplicates()
df["timestamp"] = df["timestamp"].astype(int)
df = df.sort_values(by="timestamp")

df = df[ df["timestamp"] >= dates[0]]

df.to_csv("data.csv")


print(df)
