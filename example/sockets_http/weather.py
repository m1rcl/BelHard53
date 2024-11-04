import asyncio
import time
from aiohttp import ClientSession
import requests

n_step:int = 0



async def aget_weather(city:str, n_city):
    # добавил номер города и номер в каком порядке он возвращается и печатается 
    # чтобы было видно что возврат идет всегда в разном порядке и не зависит 
    # от порядка отправки
    global n_step
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()            
            
            # принт не асинхронный,  но это конечная точка и выполняется очень быстро            
            n_step += 1 
            print(f'{n_step} - {n_city} {city}: {weather_json["weather"][0]["main"]}')
    

def get_weather(city):    
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
        res = requests.get(url,params).json()        
        print(f'{city}: {res["weather"][0]["main"]}')
    


async def async_main(cities_):
    tasks = []
    for i, city in enumerate(cities_):
        tasks.append(asyncio.create_task(aget_weather(city, i)))

    for task in tasks:
        await task
        

def main(cities_):    
    for city in cities_:
        get_weather(city)

    

    
cities = ['Minsk','Grodno','Gomel','Moscow']*40

t = time.time()



asyncio.run(async_main(cities))
#main(cities)

print(time.time() - t)
