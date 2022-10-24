# MADE BY 0RCL aka NOVAIS
#importing the libraries
import requests
import json
import time

response1 = requests.get('https://www.rolimons.com/api/activity2').json() # MARKET ACTIVITY API
response2 = requests.get('https://www.rolimons.com/itemapi/itemdetails').json() # ITEM INFO API

config = open('config.json')
data = json.load(config)
max_robux = data['max'] # maximum robux
min_robux = data['min'] # minimum robux
profit = data['profit'] # how much profit do you want MINIMUM

while True:
  for item in response1['activities']:
    type = item[1]
    id = item[2]
    price = item[4]
    info = response2['items'][id]
    name = info[0]
    value = info[4]
    proj = info[7]
    if type == 0: # 0 = price updates, 1 = rap updates
      if price > min_robux and price < max_robux:
        if proj == -1:
          if value > price:
            if value - price >= profit:
              print(f'https://www.roblox.com/catalog/{id} -- {name} selling for {price} ({value-price} win)')
              time.sleep(1) # let's chill for a while
