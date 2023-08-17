from matplotlib import pyplot as plt
import requests

url = requests.get("https://countriesnow.space/api/v0.1/countries/population/cities")
response = url.json()

countryinput = input("Enter the Country : ")
cityInput = input("enter the City :")
startyear = input("enter startYear :")
endYear = input("enter endyear :")
yearList = []
valueList = []
index1 = []
index2 = 0
found_city = False
found_country = False
found_syear = False
found_eyear = False
cityindex = 0
sum1 = 0
indexesofdate = 0

for i in range(len(response["data"])):
    if countryinput == response["data"][i]["country"]:
        found_country = True
        if cityInput == response["data"][i]["city"]:
            cityindex = i
            found_city = True

for j in range(len(response["data"][cityindex]["populationCounts"])):
    if response["data"][cityindex]["populationCounts"][j]["year"] == startyear:
        if len(index1) == 0:
            index1.append(j)
        found_syear = True
    if response["data"][cityindex]["populationCounts"][j]["year"] == endYear:
        index2 = j
        found_eyear = True

if found_country == False:
    print("Invalid Country")
elif found_city == False:
    print("invalid city")
elif found_syear == False:
    print(found_syear)
    print("invalid s")
elif found_eyear == False:
    print("invalid e")
else:
    for k in range(index1[0], index2 + 1):
        if (
            int(response["data"][cityindex]["populationCounts"][k]["year"])
            not in yearList
        ):
            yearList.append(
                int(response["data"][cityindex]["populationCounts"][k]["year"])
            )
            valueList.append(
                float(response["data"][cityindex]["populationCounts"][k]["value"])
            )
        elif (
            int(response["data"][cityindex]["populationCounts"][k]["year"]) in yearList
        ):
            sum1 = float(response["data"][cityindex]["populationCounts"][k]["value"])
            indexesofdate = yearList.index(int(response["data"][cityindex]["populationCounts"][k]["year"]))
            finalValue = sum1 + valueList[indexesofdate]
            valueList[indexesofdate] = finalValue
if found_country and found_city and found_syear and found_eyear == True:
    print("Value : ", valueList)
    print("year : ", yearList)
    plt.bar(yearList, valueList)
    plt.xlabel("Years")
    plt.ylabel("Value")
    plt.title("Countries API")
    plt.show()
