# Highest Cases

import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

max_cases = 0
date = ""

for i in range(len(response["cases_time_series"])):
    if int(response["cases_time_series"][i]["dailyconfirmed"]) >= max_cases:
        max_cases = int(response["cases_time_series"][i]["dailyconfirmed"])
        date = response["cases_time_series"][i]["date"]

print(max_cases)
print(date)
