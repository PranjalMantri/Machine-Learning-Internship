# ISRO API

import requests

url = requests.get("https://isro.vercel.app/api/spacecrafts")
response = url.json()

#for i in response:
#   print(i)

#print(response.keys())

#print(response["spacecrafts"][0]["name"])

spaceCraftId = int(input("Enter ID: "))

for i in range(len((response["spacecrafts"]))):
    if spaceCraftId == response["spacecrafts"][i]["id"]:
        print(f'Spacecraft name for the ID {spaceCraftId} is: {response["spacecrafts"][i]["name"]}')
        break
else:
    print("ID not found")
