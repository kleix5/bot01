import requests

def sutochno(city: str):

    search_city = city
   
    headers = {
      'User-Agent': 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
      'Token': 'Hy6U3z61fflbgT2yJ/VdlQ2719'
    }

    r = requests.get(
        'https://sutochno.ru/api/rest/search/getTermSuggestionsWithBoundingBox?query='
        + search_city, headers=headers
        )

    location_id = r.json()['data']['suggestions'][0]['location']['id']

    lr = requests.get(
        'https://sutochno.ru/api/rest/search/getTotalFound?location_id=' + location_id + '&location_type=city',
        headers=headers
        )

    return lr.json()

city = input('Введите название города:____')
print(sutochno(city))
