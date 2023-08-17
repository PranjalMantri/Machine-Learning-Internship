# Using Covid API to plot the number of cases in each State

import requests
from matplotlib import pyplot as plt

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

states = ""
cases = 0


for i in range(1, len(response["statewise"])):
    states = response["statewise"][i]["state"]
    cases = int(response["statewise"][i]["confirmed"])
    plt.barh(states, cases)

plt.xlabel("States")
plt.ylabel("Cases")
plt.show()

