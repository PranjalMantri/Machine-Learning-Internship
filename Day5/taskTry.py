# Create a python script using https://countriesnow.space/api/v0.1/countries/population/cities API
# to create a graph on the basis of country, city, start year and end year entered by user

import requests
from matplotlib import pyplot as plt

url = requests.get("https://countriesnow.space/api/v0.1/countries/population/cities")
response = url.json()

years = []
population = []
sum = 0
index = 0
final_value = 0
low_index = 0
high_index = 0
cityindex = 0

country = "Australia"
city = "Adelaide"
start_year = "2011"
end_year = "2003"

for i in range(len(response["data"])):
    if country == response["data"][i]["country"]:
        if city == response["data"][i]["city"]:
            city_index = i
            for j in range(len(response["data"][i]["populationCounts"])):
                if start_year == response["data"][i]["populationCounts"][j]["year"]:
                    if low_index == 0:
                        low_index = j
                if end_year == response["data"][i]["populationCounts"][j]["year"]:
                    high_index = j
            break
else:
    print("Invalid Country and City")

print(low_index)
print(high_index)

# for i in range(len(response["data"][cityindex]["populationCounts"])):
#     if int(response["data"][cityindex]["populationCounts"][i]["year"]) != years[i]:
#         years.append(int(response["data"][cityindex]["populationCounts"][i]["year"]))
#         population.append(float(response["data"][cityindex]["populationCounts"][i]["value"]))
#     elif int(response["data"][cityindex]["populationCounts"][i]["year"]) == years[i]:
#         sum = int(response["data"][cityindex]["populationCounts"][i]["value"]) + int(response["data"][cityindex]["populationCounts"][i - 1]["value"])
#         population[i] = sum



plt.show()
print(years)
print(population)

