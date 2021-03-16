import requests


class NasaImages:
    linksToImagesOfMars = []

    def __init__(self, url, options):
        self.request = requests.get(url=url, params=options)
        self.response = self.request.json()
        self.checking_data()

    def checking_data(self):
        try:
            self.response = self.response['collection']['items']
        except Exception:
            print('No data with yours options')

    def get_links_to_image(self):
        for responseData in self.response:
            for responseDataKeys in responseData:
                if responseDataKeys == 'data':
                    for dataWithLinks in responseData[responseDataKeys]:
                        for description in dataWithLinks:
                            if description == 'description' and dataWithLinks[description].find(
                                    ', 2018') > -1 \
                                    and dataWithLinks[description].find('moon') == -1 \
                                    and dataWithLinks[description].find('MarCO') == -1 \
                                    and dataWithLinks[description].find('Florida') == -1 \
                                    and responseData['links'][0]['href'].find(' ') == -1:
                                if len(self.linksToImagesOfMars) < 5:
                                    self.linksToImagesOfMars.append(responseData['links'][0]['href'])

        self.printing_result()

    def printing_result(self):
        for link in self.linksToImagesOfMars:
            print(link)


nasa = NasaImages('https://images-api.nasa.gov/search', {
        'q': 'mars',
        'year_start': 2018,
        'year_end': 2018,
        'media_type': 'image',
        'keywords': 'mars,2018,surface'
    })
nasa.get_links_to_image()
