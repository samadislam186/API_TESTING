import requests

API_STRING="http://dataservice.accuweather.com/locations/v1/adminareas/countryCode?"
API_KEY="apikey=sihgDcEpAAc7wN2GGvBlP1ll2G0fAuVD"

URI = API_STRING + API_KEY

#print(URI)

r = requests.get(URI)

print(r.json())
