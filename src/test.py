from urllib.request import urlopen

import json

url = "https://api.energidataservice.dk/dataset/Elspotprices?limit=100&offset=0&start=2022-08-18T00:00&end=2022-08-19T00:00&filter=%7B%22PriceArea%22:%22DK1%22%7D&sort=HourDK%20DESC&timezone=dk"

print("Henter data..."),

response = urlopen(url)

json = json.loads(response.read())

print("Data hentet:")
print(json)