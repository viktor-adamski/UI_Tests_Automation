import requests

url, linksToImagesOfMars = 'https://images-api.nasa.gov/search', []
data = {
    'q': 'mars',
    'year_start': 2018,
    'year_end': 2018,
    'media_type': 'image',
    'keywords': 'mars,2018,surface'
}

request = requests.get(url=url, params=data)
response = request.json()

for collection in response:
    for collectionValue in response[collection]:
        if collectionValue == 'items':
            for responseData in response[collection][collectionValue]:
                for responseDataKeys in responseData:
                    if responseDataKeys == 'data':
                        for dataWitLinks in responseData[responseDataKeys]:
                            for description in dataWitLinks:
                                if description == 'description' and dataWitLinks[description].find(', 2018') > -1 \
                                        and dataWitLinks[description].find('moon') == -1 \
                                        and dataWitLinks[description].find('MarCO') == -1 \
                                        and dataWitLinks[description].find('Florida') == -1 \
                                        and responseData['links'][0]['href'].find(' ') == -1:
                                    if len(linksToImagesOfMars) < 5:
                                        linksToImagesOfMars.append(responseData['links'][0]['href'])
for link in linksToImagesOfMars:
    print(link)
