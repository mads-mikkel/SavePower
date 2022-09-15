from ast import operator
from operator import truediv
import string
from urllib.request import urlopen
from datetime import datetime
import json

class HourPrice(object):
    def __init__(self, date, hour, price):
        self.date = date,
        self.hour = hour,
        self.price = price

    def __str__(self): 
        return "{0} {1} {2}".format(self.date, self.hour, self.price)

def getData():
    url = "https://api.energidataservice.dk/dataset/Elspotprices?limit=100&offset=0&start=2022-08-18T00:00&end=2022-08-19T00:00&filter=%7B%22PriceArea%22:%22DK1%22%7D&sort=HourDK%20DESC&timezone=dk"
    #response = urlopen(url)
    response = open(r"C:\Users\jona63m2\source\repos\SavePower\src\example.json")
    jsonData = json.loads(response.read())
    response.close()    #test file close
    return jsonData


def getPowerPrices(jsonData):
    prices = []
    for entry in jsonData['records']:
        date = entry['HourDK'][0:10]
        hour = entry['HourDK'][11:13]
        price = round(entry['SpotPriceDKK'])
        prices.append(date + hour + " " + str(price))
    prices.sort(key = lambda x: x.split()[0])
    for entry in prices:  
        print(f"{entry[0:10]} kl. {entry[10:12]}: {entry[13:]} øre/kWh")
    return prices

def getCheapestHourToday(prices):
    price4Hour = []
    for each in range(len(prices) - 3):
        averagePrice = 0
        if prices[each][8:10] == str(18): #Replace 18 with current date 
            for i in range(4):
                averagePrice += int(prices[each + i][13:])
            averagePrice = averagePrice / 4
            price4Hour.append(prices[each][10:12] + " " + str(averagePrice))
            print(prices[each][10:12] + " " + str(averagePrice))
    price4Hour.sort(key = lambda x: x.split()[1])
    return price4Hour[0][0:2]

def getCheapestHourTomorrow(prices):
    price4Hour = []
    for each in range(len(prices) - 3):
        averagePrice = 0
        if prices[each][8:10] == str(19): #Replace 19 with date tomorrow
            for i in range(4):
                averagePrice += int(prices[each + i][13:])
            averagePrice = averagePrice / 4
            price4Hour.append(prices[each][10:12] + " " + str(averagePrice))
            print(prices[each][10:12] + " " + str(averagePrice))
    price4Hour.sort(key = lambda x: x.split()[1])
    if len(price4Hour) == 0: 
        return None
    else:
        return price4Hour[0][0:2]


print("henter data...")
json = getData()
print(json)
prices = getPowerPrices(json)
getCheapestHourToday(prices)
getCheapestHourTomorrow(prices)
