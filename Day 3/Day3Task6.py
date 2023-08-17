# Taking User Input specified range and finding the total number of cases in the range

import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

low = 0
high = 0
total_cases = 0
max_cases = 0
date = ""

start_date = input("Enter a Start date: ")
end_date = input("Enter a End date: ")

for i in range(len(response["cases_time_series"])):
    if start_date == response["cases_time_series"][i]["date"]:
        low = i
    if end_date == response["cases_time_series"][i]["date"]:
        high = i

if low == 0 or high == 0:
    print("Invalid Date")
else:
    for i in range(low, high + 1):
        total_cases += int(response["cases_time_series"][i]["dailyconfirmed"])

        if int(response["cases_time_series"][i]["dailyconfirmed"]) >= max_cases:
            max_cases = int(response["cases_time_series"][i]["dailyconfirmed"])
            date = response["cases_time_series"][i]["date"]

    print(f"Total cases in the specified range: {total_cases}")
    print(max_cases)
    print(date)
