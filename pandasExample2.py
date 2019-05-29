import pandas as pd

df = pd.read_csv("aapl.csv", parse_dates=["Date"], index_col="Date")


# print(df["2016-09"])

# print(df["2017-3"].Close.mean())

# print(df["2017-3-5"].Close)

print(df["2017-3-20":"2017-3-2"])

# print(df.Close.resample("M").mean())

# %matplotlib inline
# print(df.Close.resample("M").mean().plot())

