"""
Написать веб-приложение на Flask со след ендпоинтами:
    - главная страница
    - /duck/ - отображает заголовок рандомная утка №ххх и картинка утки 
                которую получает по API https://random-d.uk/
                
    - /fox/<int>/ - аналогично утке только с лисой (- https://randomfox.ca), 
                    но количество разных картинок определено int. 
                    если int больше 10 или меньше 1 - вывести сообщение об ошибке
    
    - /weather-minsk/ - показывает погоду в минске
    
    - /weather/<city>/ - показывает погоду в городе указанного в city
    
    - по желанию добавить еще один ендпоинт на любую тему 
    
    
Добавить обработчик ошибки 404. (есть в example)
    

"""


from flask import Flask
import requests

html_start = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Простое веб приложение на Flask</title>   
</head>
<body>
"""


html_main = """
    <p>
        Для просмотра рандомной утки введите в адресной строке /duck/
    </p>

    <p>
        Для просмотра рандомных (от 1 до 10) лис введите в адресной строке /fox/<число лис от 1 до 10>/
    </p>

    <p>
        Для просмотра текущей температуры города Minsk введите в адресной строке /weather-minsk/
    </p>

    <p>
        Для просмотра текущей температуры конкретного города введите в адресной строке /weather/<название города>/
    </p>
    
"""


html_duck = """
    <p>
        Рандомная утка
    </p>
    
"""


html_fox = """
    <p>
        Рандомные лисы
    </p>
    
"""


html_weather_city = """
    <p>
        Текущая температура в городе 
    </p>
    
"""


html_end = """
</body>
</html>
"""


app = Flask(__name__)


@app.route("/")
def index():
    return html_start + html_main + html_end


@app.route("/duck/")
def duck():
    url = "https://random-d.uk/api/v2"
    res = requests.get(f"{url}/random").json()
    rand_duck_url = res["url"]
    return html_start + html_duck + f'<img src="{rand_duck_url}">' + html_end


@app.route("/fox/<int:count>/")
def fox(count):
    if 1 < count < 11:
        text = ""
        for i in range(count):
            url = "https://randomfox.ca/floof/"
            res = requests.get(url).json()
            rand_fox_url = res["image"]
            text += f"<img src={rand_fox_url}>"
        return html_start + html_fox + text + html_end
    else:
        return '<h1 style="color:red">введено неверное количество</h1>'


@app.route("/weather-minsk/")
def weather_minsk():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Minsk",
        "units": "metric",
        "APPID": "7505a3a45c2f09d2e4009d8887ceb17f",
    }
    res = requests.get(url, params).json()
    temp = res["main"]["temp"]

    return (
        html_start + html_weather_city + f"Minsk - {temp} градусов Цельсия" + html_end
    )


@app.route("/weather/<city>/")
def weather_city(city):
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": f"{city}",
            "units": "metric",
            "APPID": "7505a3a45c2f09d2e4009d8887ceb17f",
        }
        res = requests.get(url, params).json()
        temp = res["main"]["temp"]

        return (
            html_start
            + html_weather_city
            + city.capitalize()
            + f" - {temp} градусов Цельсия"
            + html_end
        )
    except:
        return '<h1 style="color:red">введенный город не найден</h1>'


@app.errorhandler(404)
def page_not_found(error):
    return '<h1 style="color:red">такой страницы не существует</h1>'


app.run(port=7777)
