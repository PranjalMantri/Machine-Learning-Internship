# Pincode API

import requests

pincode = input("Enter a pincode: ")

url1 = "https://api.postalpincode.in/pincode/"
finalurl = url1 + pincode

url = requests.get(finalurl)
response = url.json()

if response[0]["Status"] == "Success":
    for i in range(len(response[0]["PostOffice"])):
        print(response[0]["PostOffice"][i]["Name"])
else:
    print("Invalid Pincode")


