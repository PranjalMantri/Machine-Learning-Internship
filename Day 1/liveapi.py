import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

print(response)
#print(type(response))

#for i in response:
#    print(i)

#print(response.keys())
#print(len(response["cases_time_series"]))

#for i in range(len(response["cases_time_series"])):
#    print(f'{i + 1} - Date : {response["cases_time_series"][i]["date"]}, Cases : {response["cases_time_series"][i]["dailyconfirmed"]}')

# date = str(input("Enter the date to find number of cases: "))
#
# for i in range(len(response["cases_time_series"])):
#     if date == response["cases_time_series"][i]["date"]:
#         print(f'Number of cases on {date}: {response["cases_time_series"][i]["dailyconfirmed"]}')
#         break
# else:
#     print("Date Not Found")
