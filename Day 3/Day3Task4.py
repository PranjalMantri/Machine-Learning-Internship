# Printing total number of days having more than 1 Lac cases

import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

count = 0

for i in range(len(response["cases_time_series"])):
    if int(response["cases_time_series"][i]["dailyconfirmed"]) >= 100000:
        count += 1

print(f"Number of days having greater than 1 Lac cases are : {count}")
