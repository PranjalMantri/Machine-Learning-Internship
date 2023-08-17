# Storing all dates in a list that are having more2 lac+ cases

import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

dates = []

for i in range(len(response["cases_time_series"])):
    if int(response["cases_time_series"][i]["dailyconfirmed"]) >= 100000:
        dates.append(response["cases_time_series"][i]["date"])

print(dates)

