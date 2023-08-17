# Bitcoin Price using CoinDesk
# Getting data from API

import requests

url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
response = url.json()

for i in response:
    print(i)

print(response.keys())

print(f'Bitcoin rate in USD is {response["bpi"]["USD"]["rate"]}')
