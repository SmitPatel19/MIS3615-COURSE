import urllib.request
import json
import pprint
import pytemperature

APIKEY = '51e01fc87a6f69d3db031cf74510b937'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint.pprint(response_data)

# Can you get the current temperature in Wellesley?


#print(response_data['main'])

#for temp in response_data['main']:
    #print(temp[0])

#print(response_data['main'[temp[0]]])

<<<<<<< HEAD
temp = print(float(response_data['main']['temp']))
print (pytemperature.k2f(275.25)) # a package I found to convert temps!
=======
(0K − 273.15) × 9/5 + 32 = -459.7

>>>>>>> f500684838c123abf84c9b9083af535380809fe9
