# Use Covid API to get dailyconfirmed, dailydeceased and dailyrecovered on a particular date and generate a chart

import requests
from matplotlib import pyplot as plt

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

days = []
daily_confirmed = []
daily_recovered = []
daily_deceased = []

for i in range(len(response["cases_time_series"])):
    days.append(i)
    daily_confirmed.append(int(response["cases_time_series"][i]["dailyconfirmed"]))
    daily_recovered.append(int(response["cases_time_series"][i]["dailyrecovered"]))
    daily_deceased.append(int(response["cases_time_series"][i]["dailydeceased"]))

plt.subplot(2, 3, 1)
plt.plot(days, daily_confirmed)
plt.title("Daily Confirmed")

plt.subplot(2, 3, 2)
plt.plot(days, daily_recovered)
plt.title("Daily Recovered")

plt.subplot(2, 3, 3)
plt.plot(days, daily_deceased)
plt.title("Daily Deceased")

plt.show()
