# Mutual Funds API

import requests

url = requests.get("https://api.mfapi.in/mf")
response = url.json()

#print(response[0].keys())

#for i in response[0].keys():
#    print(i, end=" ")

#print()
#print(response[2]["schemeCode"])

schemeCode = int(input("Enter Scheme Code: "))

for i in range(len(response)):
    if schemeCode == response[i]["schemeCode"]:
        print(f'Scheme Name for scheme code {schemeCode} is: {response[i]["schemeName"]}')
        break
else:
    print("Scheme not Found")
