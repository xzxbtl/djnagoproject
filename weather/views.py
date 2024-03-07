from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Moscow'

    PARAMS = {'units': 'metric'}
    API_KEY = '6729f06f0d02525977c351a5ef99252d'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    SEARCH_ENGINE_ID = 'f6a209dc3572c4772'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")

    try:

        data = requests.get(url, params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weather/weather.html',
                      {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city,
                       'exception_occurred': False})

    except KeyError:
        exception_occurred = True
        messages.error(request, 'Entered data is not available to API')
        # city = 'indore'
        # data = requests.get(url,params=PARAMS).json()

        # description = data['weather'][0]['description']
        # icon = data['weather'][0]['icon']
        # temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weather/weather.html',
                      {'description': 'clear sky', 'icon': '01d', 'temp': 16, 'day': day, 'city': 'moscow',
                       'exception_occurred': exception_occurred})