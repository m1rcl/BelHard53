import requests



def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'    
    params = {'q':city, 'APPID':'7505a3a45c2f09d2e4009d8887ceb17f'}
    res = requests.get(url, params).json()    
    print(f'{city} - {res['weather'][0]['main']}')
    
    
cities = ['Minsk','Grodno','Gomel','Moscow']

for city in cities:
    get_weather(city)
