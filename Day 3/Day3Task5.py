# User Input

import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

dates = []

for i in range(len(response["cases_time_series"])):
    if int(response["cases_time_series"][i]["dailyconfirmed"]) >= 100000:
        dates.append(response["cases_time_series"][i]["date"])

userdate = input("Enter a date: ")

if userdate in dates:
    print("YES")
else:
    print("NO")
